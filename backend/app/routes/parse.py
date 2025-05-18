from flask import Blueprint, request, jsonify
import ast

parse_bp = Blueprint('parse', __name__)

def parse_code(code):
    tree = ast.parse(code)
    result = {'class': [], 'function': [], 'main': ''}

    main_code = []
    for node in tree.body:
        # print("Node:", ast.unparse(node))  # Uncomment for debugging
        if isinstance(node, ast.FunctionDef):
            func_data = {
                'id': len(result['function']) + 1,
                'functionName': node.name,
                'code': ast.unparse(node)
            }
            result['function'].append(func_data)
        elif isinstance(node, ast.ClassDef):
            class_data = {
                'id': len(result['class']) + 1,
                'classname': node.name,
                'method': []
            }
            for class_node in node.body:
                if isinstance(class_node, ast.FunctionDef):
                    method_data = {
                        'methodName': class_node.name,
                        'code': ast.unparse(class_node)
                    }
                    class_data['method'].append(method_data)
            result['class'].append(class_data)
        else:
            main_code.append(ast.unparse(node))

    result['main'] = "\n".join(main_code)
    return result

@parse_bp.route('/parse', methods=['POST'])
def parse():
    data = request.get_json()
    code = data.get('code') if data else None
    if not code:
        return jsonify({'error': 'No code provided'}), 400

    try:
        parsed_data = parse_code(code)
        return jsonify(parsed_data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
