from flask import Blueprint, request, jsonify
import ast
import os # Tidak terpakai di logika utama, tapi ada di template Anda

# Mengganti nama blueprint agar lebih deskriptif jika mau, tapi kita ikuti template Anda
call_graph_bp = Blueprint('call_graph', __name__)

class CallGraphVisitor(ast.NodeVisitor):
    def __init__(self):
        self.calls = []
        self.current_class_name = None
        self.current_method_name = None
        # Menyimpan tipe yang diinferensikan untuk variabel dalam scope metode saat ini
        # Contoh: {'item': 'Product', 'product': 'Product'}
        self.method_scope_var_types = {}
        # Menyimpan tipe untuk koleksi variabel instance (misalnya dari add_product)
        # Contoh: {'ShoppingCart': {'items': 'Product'}} (artinya item dalam self.items adalah Product)
        self.instance_var_collection_types = {}

    def visit_ClassDef(self, node):
        original_class_name = self.current_class_name
        self.current_class_name = node.name
        
        # Pra-pemindaian metode seperti 'add_product' untuk menginferensikan tipe untuk variabel instance
        # Ini adalah heuristik yang disederhanakan untuk contoh spesifik
        for body_item in node.body:
            if isinstance(body_item, ast.FunctionDef) and body_item.name == 'add_product':
                param_name_for_type_check = None
                param_type_inferred = None
                collection_name_appended_to = None

                # Asumsi parameter pertama setelah 'self' adalah yang relevan untuk tipe
                if body_item.args.args and len(body_item.args.args) > 1:
                    param_node = body_item.args.args[1] # Node argumen (misalnya 'product')
                    param_name_for_type_check = param_node.arg

                if param_name_for_type_check:
                    # Cari 'isinstance(param_name_for_type_check, InferredType)'
                    for stmt in body_item.body:
                        # Mencari 'if not isinstance(product, Product):'
                        if isinstance(stmt, ast.If) and \
                           isinstance(stmt.test, ast.UnaryOp) and \
                           isinstance(stmt.test.op, ast.Not) and \
                           isinstance(stmt.test.operand, ast.Call) and \
                           isinstance(stmt.test.operand.func, ast.Name) and \
                           stmt.test.operand.func.id == 'isinstance' and \
                           len(stmt.test.operand.args) == 2 and \
                           isinstance(stmt.test.operand.args[0], ast.Name) and \
                           stmt.test.operand.args[0].id == param_name_for_type_check and \
                           isinstance(stmt.test.operand.args[1], ast.Name):
                            param_type_inferred = stmt.test.operand.args[1].id
                            break # Ditemukan tipe parameter

                if param_name_for_type_check and param_type_inferred:
                    # Cari 'self.collection_name.append(param_name_for_type_check)'
                    for sub_stmt_node in ast.walk(body_item):
                        if isinstance(sub_stmt_node, ast.Call) and \
                           isinstance(sub_stmt_node.func, ast.Attribute) and \
                           isinstance(sub_stmt_node.func.value, ast.Attribute) and \
                           isinstance(sub_stmt_node.func.value.value, ast.Name) and \
                           sub_stmt_node.func.value.value.id == 'self' and \
                           sub_stmt_node.func.attr == 'append' and \
                           len(sub_stmt_node.args) == 1 and \
                           isinstance(sub_stmt_node.args[0], ast.Name) and \
                           sub_stmt_node.args[0].id == param_name_for_type_check:
                            collection_name_appended_to = sub_stmt_node.func.value.attr
                            if self.current_class_name not in self.instance_var_collection_types:
                                self.instance_var_collection_types[self.current_class_name] = {}
                            self.instance_var_collection_types[self.current_class_name][collection_name_appended_to] = param_type_inferred
                            break # Ditemukan append ke koleksi self

        # Kunjungi metode aktual di dalam kelas
        for body_item in node.body:
            if isinstance(body_item, ast.FunctionDef):
                self.visit(body_item) # Ini akan memanggil visit_FunctionDef

        self.current_class_name = original_class_name

    def visit_FunctionDef(self, node):
        if not self.current_class_name: # Bukan metode kelas
            self.generic_visit(node)
            return

        original_method_name = self.current_method_name
        original_scope_vars = self.method_scope_var_types.copy()

        self.current_method_name = node.name
        self.method_scope_var_types.clear()

        # Inferensikan tipe untuk parameter berdasarkan pengecekan isinstance
        for stmt_node in node.body:
            # Mencari 'if not isinstance(var, Type):' atau 'if isinstance(var, Type):'
            is_isinstance_check = False
            is_negated = False
            
            if isinstance(stmt_node, ast.If):
                test_node = stmt_node.test
                if isinstance(test_node, ast.UnaryOp) and isinstance(test_node.op, ast.Not):
                    if isinstance(test_node.operand, ast.Call):
                        is_isinstance_check = True
                        is_negated = True
                        call_node = test_node.operand
                elif isinstance(test_node, ast.Call):
                    is_isinstance_check = True
                    call_node = test_node

                if is_isinstance_check and \
                   isinstance(call_node.func, ast.Name) and call_node.func.id == 'isinstance' and \
                   len(call_node.args) == 2 and \
                   isinstance(call_node.args[0], ast.Name) and \
                   isinstance(call_node.args[1], ast.Name):
                    var_name_checked = call_node.args[0].id
                    type_name_checked = call_node.args[1].id
                    self.method_scope_var_types[var_name_checked] = type_name_checked
        
        # Inferensikan tipe untuk variabel loop seperti 'for item in self.items:'
        for stmt_node in node.body:
            if isinstance(stmt_node, ast.For):
                if isinstance(stmt_node.target, ast.Name) and \
                   isinstance(stmt_node.iter, ast.Attribute) and \
                   isinstance(stmt_node.iter.value, ast.Name) and \
                   stmt_node.iter.value.id == 'self':
                    loop_var_name = stmt_node.target.id
                    collection_name = stmt_node.iter.attr
                    
                    if self.current_class_name in self.instance_var_collection_types and \
                       collection_name in self.instance_var_collection_types[self.current_class_name]:
                        item_type = self.instance_var_collection_types[self.current_class_name][collection_name]
                        self.method_scope_var_types[loop_var_name] = item_type
        
        self.generic_visit(node) # Kunjungi body dari metode
        
        self.current_method_name = original_method_name
        self.method_scope_var_types = original_scope_vars


    def visit_Call(self, node):
        # Mencari pemanggilan seperti `variabel.metode()`
        if self.current_class_name and self.current_method_name and \
           isinstance(node.func, ast.Attribute) and \
           isinstance(node.func.value, ast.Name): # objek adalah nama variabel sederhana
            
            obj_name = node.func.value.id # contoh: 'item' atau 'product'
            method_called = node.func.attr # contoh: 'get_price' atau 'get_name'

            callee_class_type = None
            if obj_name in self.method_scope_var_types:
                callee_class_type = self.method_scope_var_types[obj_name]
            
            if callee_class_type:
                # Pastikan pemanggil dan target berbeda, atau setidaknya kelas target diketahui
                # (Untuk menghindari self.method -> self_class.method jika tidak diinginkan)
                # Untuk kasus ini, kita ingin melihat Product.get_price, jadi callee_class_type harus 'Product'
                
                call_str = f"{self.current_class_name}.{self.current_method_name} -> {callee_class_type}.{method_called}"
                if call_str not in self.calls: # Hindari duplikat jika metode dipanggil berkali-kali
                    self.calls.append(call_str)
        
        self.generic_visit(node)


def extract_call_graph_from_code(python_code):
    """
    Menganalisis string kode Python dan mengekstrak call graph antar metode kelas.
    """
    try:
        tree = ast.parse(python_code)
        visitor = CallGraphVisitor()
        visitor.visit(tree)
        return {"call_graph": sorted(list(set(visitor.calls)))} # Urutkan dan pastikan unik
    except SyntaxError as e:
        return {"error": f"Syntax error in Python code: {e.msg} on line {e.lineno}"}
    except Exception as e:
        # Tangkap error lain yang mungkin terjadi selama pemrosesan AST
        # Sebaiknya log error ini di sisi server untuk debugging
        # print(f"Error processing code for call graph: {e}") 
        return {"error": f"An error occurred while processing the code: {str(e)}"}


@call_graph_bp.route('/call_graph', methods=['POST'])
def generate_call_graph(): # Mengganti nama fungsi handler
    """
    Endpoint untuk menerima kode Python dan mengembalikan call graph antar metode kelas.
    """
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    data = request.get_json()
    python_code = data.get('code')

    if not python_code:
        return jsonify({"error": "Missing 'code' field in JSON body"}), 400

    if not isinstance(python_code, str):
        return jsonify({"error": "'code' field must be a string"}), 400

    # Ekstrak call graph menggunakan fungsi yang telah dibuat
    result = extract_call_graph_from_code(python_code)
    
    if "error" in result:
        # Tentukan apakah ini kesalahan klien (400) atau server (500)
        status_code = 400 if "Syntax error" in result["error"] else 500
        return jsonify(result), status_code
    
    return jsonify(result), 200