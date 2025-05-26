from flask import Blueprint, request, jsonify
import ast
import os # Sesuai template Anda

# current_directory = os.getcwd() # Sesuai template Anda, tidak digunakan di logika ini
pdg_bp = Blueprint('pdg', __name__)

class PDGVisitor(ast.NodeVisitor):
    def __init__(self):
        # Struktur data: {"ClassName": ["method1 -> attrA", "method2 -> attrB"], ...}
        self.pdg_data = {}
        self.current_class_name = None
        self.current_method_name = None

    def visit_ClassDef(self, node):
        original_class_name = self.current_class_name
        self.current_class_name = node.name
        if self.current_class_name not in self.pdg_data:
            self.pdg_data[self.current_class_name] = []
        
        # Kunjungi semua node di dalam body kelas (termasuk metode, dll.)
        self.generic_visit(node)
        
        self.current_class_name = original_class_name # Kembalikan konteks kelas sebelumnya

    def visit_FunctionDef(self, node):
        # Hanya proses jika kita berada di dalam konteks kelas (yaitu, ini adalah metode)
        if self.current_class_name:
            original_method_name = self.current_method_name
            self.current_method_name = node.name
            
            # Kunjungi body dari metode
            self.generic_visit(node)
            
            self.current_method_name = original_method_name # Kembalikan konteks metode sebelumnya
        else:
            # Jika ini fungsi di luar kelas, kita bisa memilih untuk mengabaikannya atau memprosesnya secara berbeda
            # Untuk PDG ini, kita fokus pada metode kelas
            self.generic_visit(node)


    def visit_Assign(self, node):
        # Pastikan kita berada di dalam metode sebuah kelas
        if self.current_class_name and self.current_method_name:
            for target in node.targets:
                # Cari assignment ke atribut instance (misalnya, self.attribute = value)
                if isinstance(target, ast.Attribute):
                    # Pastikan basis dari atribut adalah 'self'
                    if isinstance(target.value, ast.Name) and target.value.id == 'self':
                        attribute_name = target.attr
                        dependency_str = f"{self.current_method_name} -> {attribute_name}"
                        
                        # Tambahkan dependensi jika belum ada (untuk menghindari duplikat string yang sama)
                        if dependency_str not in self.pdg_data[self.current_class_name]:
                            self.pdg_data[self.current_class_name].append(dependency_str)
        
        # Penting untuk tetap mengunjungi node anak dari assignment, 
        # karena value yang di-assign bisa jadi memiliki struktur yang kompleks.
        # Namun, untuk PDG spesifik "metode mengubah atribut", kita hanya tertarik pada target.
        self.generic_visit(node)


def extract_pdg_from_code(python_code):
    """
    Menganalisis string kode Python dan mengekstrak PDG (method -> attribute modified).
    """
    try:
        tree = ast.parse(python_code)
        visitor = PDGVisitor()
        visitor.visit(tree)
        # Mengurutkan dependensi di dalam setiap kelas untuk output yang konsisten (opsional)
        for class_name in visitor.pdg_data:
            visitor.pdg_data[class_name].sort()
        return visitor.pdg_data
    except SyntaxError as e:
        return {"error": f"Syntax error in Python code: {e.msg} on line {e.lineno}"}
    except Exception as e:
        # Untuk error lain selama pemrosesan AST
        # print(f"Error processing code for PDG: {e}") # Untuk debugging di server
        return {"error": f"An error occurred while processing the code: {str(e)}"}


@pdg_bp.route('/pdg', methods=['POST'])
def generate_pdg(): # Mengganti nama fungsi handler agar lebih deskriptif
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

    # Ekstrak PDG menggunakan fungsi yang telah dibuat
    result = extract_pdg_from_code(python_code)
    
    if "error" in result:
        # Tentukan status code berdasarkan jenis error
        status_code = 400 if "Syntax error" in result["error"] else 500
        return jsonify(result), status_code
    
    return jsonify(result), 200