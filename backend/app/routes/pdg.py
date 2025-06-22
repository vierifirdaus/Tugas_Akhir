from flask import Blueprint, request, jsonify
import ast
import os

pdg_bp = Blueprint('pdg', __name__)

class PDGVisitor(ast.NodeVisitor):
    MUTATING_LIST_METHODS = {
        'append', 'extend', 'insert', 'remove', 'pop', 'clear', 'sort', 'reverse'
    }

    def __init__(self):
        self.pdg_data = {}
        self.current_class_name = None
        self.current_method_name = None

    def visit_ClassDef(self, node):
        original_class_name = self.current_class_name
        self.current_class_name = node.name
        if self.current_class_name not in self.pdg_data:
            self.pdg_data[self.current_class_name] = []
        self.generic_visit(node)
        self.current_class_name = original_class_name

    def visit_FunctionDef(self, node):
        if self.current_class_name:
            original_method_name = self.current_method_name
            self.current_method_name = node.name
            self.generic_visit(node)
            self.current_method_name = original_method_name
        else:
            self.generic_visit(node)

    def _record_dependency(self, target_node):
        """Helper untuk mencatat dependensi saat atribut 'self' dimodifikasi."""
        if self.current_class_name and self.current_method_name:
            if isinstance(target_node, ast.Attribute):
                if isinstance(target_node.value, ast.Name) and target_node.value.id == 'self':
                    attribute_name = target_node.attr
                    dependency_str = f"{self.current_method_name} -> {attribute_name}"
                    if dependency_str not in self.pdg_data[self.current_class_name]:
                        self.pdg_data[self.current_class_name].append(dependency_str)

    def visit_Assign(self, node):
        for target in node.targets:
            self._record_dependency(target)
        self.generic_visit(node)

    def visit_AugAssign(self, node):
        self._record_dependency(node.target)
        self.generic_visit(node)

    # --- PERBAIKAN BARU ADA DI SINI ---
    def visit_Call(self, node):
        """
        Mendeteksi modifikasi atribut melalui pemanggilan metode, 
        contoh: self.items.append(product)
        """
        # `node.func` adalah fungsi yang dipanggil.
        # Kita cari pola: self.attribute.method()
        # Ini berarti `node.func` harus berupa `ast.Attribute` (e.g., '... .append')
        if isinstance(node.func, ast.Attribute):
            # Cek apakah nama metodenya ada di dalam daftar metode mutasi kita
            method_name = node.func.attr
            if method_name in self.MUTATING_LIST_METHODS:
                # `node.func.value` adalah objek tempat metode dipanggil (e.g., 'self.items')
                # Kita bisa teruskan ini ke helper kita untuk memeriksa apakah itu `self.attribute`
                self._record_dependency(node.func.value)
        
        # Selalu panggil generic_visit untuk memastikan kita mengunjungi semua node anak
        self.generic_visit(node)


def extract_pdg_from_code(python_code):
    """
    Menganalisis string kode Python dan mengekstrak PDG (method -> attribute modified).
    """
    try:
        tree = ast.parse(python_code)
        visitor = PDGVisitor()
        visitor.visit(tree)
        for class_name in visitor.pdg_data:
            visitor.pdg_data[class_name].sort()
        return visitor.pdg_data
    except SyntaxError as e:
        return {"error": f"Syntax error in Python code: {e.msg} on line {e.lineno}"}
    except Exception as e:
        return {"error": f"An error occurred while processing the code: {str(e)}"}


@pdg_bp.route('/pdg', methods=['POST'])
def generate_pdg():
    """
    Endpoint untuk menerima kode Python dan mengembalikan PDG
    (metode mana yang memodifikasi atribut instance).
    """
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    data = request.get_json()
    python_code = data.get('code')

    if not python_code:
        return jsonify({"error": "Missing 'code' field in JSON body"}), 400

    if not isinstance(python_code, str):
        return jsonify({"error": "'code' field must be a string"}), 400

    result = extract_pdg_from_code(python_code)
    
    if "error" in result:
        status_code = 400 if "Syntax error" in result["error"] else 500
        return jsonify(result), status_code
    
    return jsonify(result), 200