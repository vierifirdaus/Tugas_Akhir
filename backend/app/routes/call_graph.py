# routes/call_graph_routes.py
from flask import Blueprint, request, jsonify
import ast
from typing import Dict, Any, List

call_graph_bp = Blueprint('call_graph', __name__)

# Daftar fungsi built-in yang umum untuk diabaikan
BUILTIN_FUNCTIONS_TO_IGNORE = {
    'print', 'range', 'isinstance', 'len', 'super', 'str', 'int', 'float', 'list', 'dict', 'set',
    'ValueError', 'TypeError', 'Exception'
}


class CallGraphVisitor(ast.NodeVisitor):
    def __init__(self):
        self.calls = set()
        self.scope_stack: List[str] = []
        self.current_method_var_types: Dict[str, str] = {}
        self.instance_var_collection_types: Dict[str, Dict[str, str]] = {}
        self.scope_stack: List[str] = ["main"]
        self.variable_types: Dict[str, str] = {}

    def get_current_scope(self) -> str:
        return self.scope_stack[-1] if self.scope_stack else None
        
    def get_current_class_scope(self) -> str:
        if self.scope_stack and '.' in self.scope_stack[-1]:
            return self.scope_stack[-1].split('.')[0]
        if self.scope_stack and '.' not in self.scope_stack[-1]:
             return self.scope_stack[-1]
        return None

    def visit_Assign(self, node: ast.Assign):
        # Hanya menangani assignment sederhana seperti `var = ClassName()`
        if len(node.targets) == 1 and isinstance(node.targets[0], ast.Name) and isinstance(node.value, ast.Call):
            var_name = node.targets[0].id
            # Dapatkan nama kelas yang dipanggil
            if isinstance(node.value.func, ast.Name):
                class_name = node.value.func.id
                self.variable_types[var_name] = class_name
        
        # Tetap kunjungi node di dalamnya (penting untuk menangani pemanggilan constructor)
        self.generic_visit(node)

    def visit_ClassDef(self, node: ast.ClassDef):
        self.scope_stack.append(node.name)
        
        for body_item in node.body:
            if isinstance(body_item, ast.FunctionDef) and len(body_item.args.args) > 1:
                param_name = body_item.args.args[1].arg
                inferred_type = None
                for stmt in body_item.body:
                    if isinstance(stmt, ast.If) and isinstance(stmt.test, (ast.UnaryOp, ast.Call)):
                        call_node = stmt.test.operand if isinstance(stmt.test, ast.UnaryOp) else stmt.test
                        if isinstance(call_node, ast.Call) and isinstance(call_node.func, ast.Name) and \
                           call_node.func.id == 'isinstance' and len(call_node.args) == 2 and \
                           isinstance(call_node.args[0], ast.Name) and call_node.args[0].id == param_name and \
                           isinstance(call_node.args[1], ast.Name):
                            inferred_type = call_node.args[1].id
                            break
                if not inferred_type: continue
                
                for sub_node in ast.walk(body_item):
                    if isinstance(sub_node, ast.Call) and isinstance(sub_node.func, ast.Attribute) and \
                       sub_node.func.attr == 'append' and isinstance(sub_node.func.value, ast.Attribute) and \
                       isinstance(sub_node.func.value.value, ast.Name) and sub_node.func.value.value.id == 'self':
                        
                        collection_name = sub_node.func.value.attr
                        if node.name not in self.instance_var_collection_types:
                            self.instance_var_collection_types[node.name] = {}
                        self.instance_var_collection_types[node.name][collection_name] = inferred_type
                        break

        self.generic_visit(node)
        self.scope_stack.pop()

    def visit_FunctionDef(self, node: ast.FunctionDef):
        parent_scope = self.get_current_scope()

        if parent_scope == "main":
            current_scope_name = node.name
        else:
            current_scope_name = f"{parent_scope}.{node.name}"

        self.scope_stack.append(current_scope_name)

        original_var_types = self.current_method_var_types.copy()
        self.current_method_var_types.clear()
        for param in node.args.args:
            param_name = param.arg
            if param_name == 'self': continue
            for stmt in node.body:
                 if isinstance(stmt, ast.If) and isinstance(stmt.test, (ast.UnaryOp, ast.Call)):
                    call_node = stmt.test.operand if isinstance(stmt.test, ast.UnaryOp) else stmt.test
                    if isinstance(call_node, ast.Call) and isinstance(call_node.func, ast.Name) and \
                       call_node.func.id == 'isinstance' and len(call_node.args) == 2 and \
                       isinstance(call_node.args[0], ast.Name) and call_node.args[0].id == param_name and \
                       isinstance(call_node.args[1], ast.Name):
                        inferred_type = call_node.args[1].id
                        self.current_method_var_types[param_name] = inferred_type
                        break

        current_class = self.get_current_class_scope()
        if current_class:
            for stmt_node in node.body:
                if isinstance(stmt_node, ast.For) and isinstance(stmt_node.target, ast.Name) and \
                   isinstance(stmt_node.iter, ast.Attribute) and isinstance(stmt_node.iter.value, ast.Name) and \
                   stmt_node.iter.value.id == 'self':
                    
                    loop_var_name = stmt_node.target.id
                    collection_name = stmt_node.iter.attr
                    if current_class in self.instance_var_collection_types and \
                       collection_name in self.instance_var_collection_types[current_class]:
                        item_type = self.instance_var_collection_types[current_class][collection_name]
                        self.current_method_var_types[loop_var_name] = item_type

        self.generic_visit(node)
        self.scope_stack.pop()
        self.current_method_var_types = original_var_types

    def visit_Call(self, node: ast.Call):
        caller = self.get_current_scope()

        callee_full_name = None
        
        if isinstance(node.func, ast.Attribute) and isinstance(node.func.value, ast.Name) and node.func.value.id == 'self':
            class_name = self.get_current_class_scope()
            if class_name:
                callee_full_name = f"{class_name}.{node.func.attr}"

        # Kasus 2: Pemanggilan pada variabel lain -> product.get_name()
        elif isinstance(node.func, ast.Attribute) and isinstance(node.func.value, ast.Name):
            var_name = node.func.value.id
            inferred_class_type = None
            
            # Cek tipe variabel di scope metode saat ini
            if var_name in self.current_method_var_types:
                inferred_class_type = self.current_method_var_types[var_name]
            # Jika tidak ada, cek tipe variabel di scope global/modul
            elif var_name in self.variable_types:
                inferred_class_type = self.variable_types[var_name]
            
            if inferred_class_type:
                method_called = node.func.attr
                callee_full_name = f"{inferred_class_type}.{method_called}"


        elif isinstance(node.func, ast.Name):
            if node.func.id not in BUILTIN_FUNCTIONS_TO_IGNORE:
                callee_full_name = node.func.id

        if callee_full_name:
            # Pastikan caller bukan nama metode jika pemanggilan berasal dari metode lain
            if '.' in caller:
                 caller_name = caller
            # Jika caller adalah kelas, gunakan nama kelas saja
            elif self.get_current_class_scope() and self.get_current_class_scope() in caller:
                 caller_name = self.get_current_class_scope()
            else:
                 caller_name = "main"

            # Koreksi jika caller adalah nama fungsi di dalam kelas
            if '.' in caller:
                caller_name = caller
            else:
                current_class_scope = self.get_current_class_scope()
                if current_class_scope and caller != "main":
                    caller_name = f"{current_class_scope}.{caller}"
                else:
                    caller_name = caller
            
            self.calls.add(f"{caller_name} -> {callee_full_name}")

        self.generic_visit(node)

def extract_call_graph_from_code(python_code: str) -> dict:
    """Menganalisis kode dan mengekstrak call graph."""
    try:
        tree = ast.parse(python_code)
        visitor = CallGraphVisitor()
        visitor.visit(tree)
        return {"call_graph": sorted(list(visitor.calls))}
    except Exception as e:
        print(f"Error processing code for call graph: {e}")
        return {"error": f"An error occurred while processing the code: {str(e)}"}

@call_graph_bp.route('/call_graph', methods=['POST'])
def generate_call_graph():
    """Endpoint untuk call graph."""
    data = request.get_json()
    python_code = data.get('code')
    if not python_code: return jsonify({"error": "Missing 'code'"}), 400
    result = extract_call_graph_from_code(python_code)
    if "error" in result: return jsonify(result), 400
    return jsonify(result), 200