from flask import Blueprint, request, jsonify
import ast

pdg_bp = Blueprint('pdg', __name__)

class PDGVisitor(ast.NodeVisitor):
    # Daftar metode yang dianggap memodifikasi list/dict (bisa diperluas)
    MUTATING_METHODS = {
        'append', 'extend', 'insert', 'remove', 'pop', 'clear', 'sort', 'reverse',
        'update', 'setdefault'
    }

    def __init__(self):
        self.pdg_data = {}
        self.current_class_name = None
        self.current_method_name = None

    def visit_ClassDef(self, node):
        self.current_class_name = node.name
        if self.current_class_name not in self.pdg_data:
            self.pdg_data[self.current_class_name] = []
        self.generic_visit(node)
        self.current_class_name = None

    def visit_FunctionDef(self, node):
        if self.current_class_name:
            self.current_method_name = node.name
            self.generic_visit(node)
            self.current_method_name = None
        else:
            self.generic_visit(node)

    def _record_dependency(self, target_node):
        """
        Helper cerdas untuk mencatat dependensi.
        Sekarang bisa menangani assignment langsung (self.attr) dan via subscript (self.attr[key]).
        """
        if not (self.current_class_name and self.current_method_name):
            return

        attribute_node = None
        
        # Kasus 1: Assignment langsung, contoh: self.total_harga = 0
        if isinstance(target_node, ast.Attribute):
            attribute_node = target_node
        
        # --- PERBAIKAN UTAMA DI SINI ---
        # Kasus 2: Assignment via subscript, contoh: self._items['key'] = value
        elif isinstance(target_node, ast.Subscript) and isinstance(target_node.value, ast.Attribute):
            # Kita tertarik pada objeknya (self._items), bukan subscript-nya ([...])
            attribute_node = target_node.value
        
        # Jika kita berhasil menemukan node atribut yang relevan
        if attribute_node:
            # Pastikan itu adalah atribut dari 'self'
            if isinstance(attribute_node.value, ast.Name) and attribute_node.value.id == 'self':
                attribute_name = attribute_node.attr
                dependency_str = f"{self.current_method_name} -> {attribute_name}"
                if dependency_str not in self.pdg_data[self.current_class_name]:
                    self.pdg_data[self.current_class_name].append(dependency_str)

    def visit_Assign(self, node):
        """Dipanggil untuk assignment seperti `a = b`."""
        for target in node.targets:
            self._record_dependency(target)
        self.generic_visit(node)

    def visit_AugAssign(self, node):
        """Dipanggil untuk assignment seperti `a += b`."""
        self._record_dependency(node.target)
        self.generic_visit(node)

    def visit_Call(self, node):
        """
        Mendeteksi modifikasi atribut melalui pemanggilan metode,
        contoh: self.items.append(product)
        """
        if isinstance(node.func, ast.Attribute):
            method_name = node.func.attr
            if method_name in self.MUTATING_METHODS:
                # `node.func.value` adalah objek tempat metode dipanggil (misalnya, 'self.items')
                self._record_dependency(node.func.value)
        
        self.generic_visit(node)


def extract_pdg_from_code(python_code):
    """
    Menganalisis string kode Python dan mengekstrak PDG.
    """
    try:
        tree = ast.parse(python_code)
        visitor = PDGVisitor()
        visitor.visit(tree)
        # Urutkan hasil untuk konsistensi
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
    Endpoint untuk menerima kode Python dan mengembalikan PDG.
    """
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    data = request.get_json()
    python_code = data.get('code')

    if not python_code or not isinstance(python_code, str):
        return jsonify({"error": "Missing or invalid 'code' field in JSON body"}), 400

    result = extract_pdg_from_code(python_code)
    
    if "error" in result:
        status_code = 400 if "Syntax error" in result["error"] else 500
        return jsonify(result), status_code
    
    return jsonify(result), 200