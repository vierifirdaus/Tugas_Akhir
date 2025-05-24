from flask import Blueprint, request, jsonify
import ast
import os

# Mengganti nama blueprint agar lebih deskriptif
attribute_bp = Blueprint('code_analysis', __name__)

def extract_attributes_from_code(python_code):
    """
    Menganalisis string kode Python dan mengekstrak atribut kelas.
    Fokus pada atribut yang diinisialisasi dalam metode __init__.
    """
    try:
        # Parse kode Python menjadi Abstract Syntax Tree (AST)
        tree = ast.parse(python_code)
    except SyntaxError as e:
        return {"error": f"Syntax error in Python code: {e}"}

    class_attributes = {}

    # Iterasi melalui semua node tingkat atas di AST
    for node in tree.body:
        # Periksa apakah node adalah definisi kelas
        if isinstance(node, ast.ClassDef):
            class_name = node.name
            attributes = set() # Menggunakan set untuk menghindari duplikat jika ada
            
            # Cari metode __init__ di dalam kelas
            for item in node.body:
                if isinstance(item, ast.FunctionDef) and item.name == '__init__':
                    # Di dalam __init__, cari assignment ke self.attribute
                    for stmt in item.body:
                        if isinstance(stmt, ast.Assign):
                            for target in stmt.targets:
                                # Periksa apakah target adalah ast.Attribute (misalnya, self.name)
                                if isinstance(target, ast.Attribute):
                                    # Periksa apakah value dari Attribute adalah 'self'
                                    if isinstance(target.value, ast.Name) and target.value.id == 'self':
                                        attributes.add(target.attr)
            
            if attributes: # Hanya tambahkan kelas jika memiliki atribut yang terdeteksi
                class_attributes[class_name] = sorted(list(attributes))
            elif class_name not in class_attributes : # Tambahkan kelas dengan list kosong jika tidak ada atribut
                 class_attributes[class_name] = []


    return class_attributes

# Mengganti nama route agar lebih deskriptif
@attribute_bp.route('/attributes', methods=['POST'])
def get_class_attributes():
    """
    Endpoint untuk menerima kode Python dan mengembalikan atribut kelasnya.
    """
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    data = request.get_json()
    python_code = data.get('code')

    if not python_code:
        return jsonify({"error": "Missing 'code' field in JSON body"}), 400

    if not isinstance(python_code, str):
        return jsonify({"error": "'code' field must be a string"}), 400

    # Ekstrak atribut menggunakan fungsi yang telah dibuat
    extracted_data = extract_attributes_from_code(python_code)

    if "error" in extracted_data:
        return jsonify(extracted_data), 400
    return jsonify(extracted_data), 200