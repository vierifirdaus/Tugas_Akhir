from flask import Blueprint, request, jsonify
import uuid
import os
import graphviz
from py2cfg import CFGBuilder
from ..parsers import GraphParser
import ast

method_bp = Blueprint('method', __name__)

def parse_code(code):
    """Parse Python code and extract class, function, and main code information."""
    tree = ast.parse(code)
    result = {'class': [], 'function': [], 'main': ''}
    main_code = []

    for node in tree.body:
        if isinstance(node, ast.FunctionDef):
            result['function'].append(node.name)
        elif isinstance(node, ast.ClassDef):
            class_data = {
                'classname': node.name,
                'method': [n.name for n in node.body if isinstance(n, ast.FunctionDef)]
            }
            result['class'].append(class_data)
        else:
            main_code.append(ast.unparse(node))

    result['main'] = "\n".join(main_code)
    return result

def generate_graphviz(code, base_filename, output_dir):
    cfg_builder = CFGBuilder()
    cfg = cfg_builder.build_from_src(base_filename, code)
    output_path = os.path.join(output_dir, base_filename)
    cfg.build_visual(output_path, 'dot', show=False)
    
    dot_file = output_path + '.dot'
    with open(dot_file, 'r', encoding='utf-8') as f:
        return f.read()

@method_bp.route('/method', methods=['POST'])
def method():
    try:
        data = request.get_json()
        code = data.get('code', '')
        
        if not code:
            return jsonify({'error': 'No code provided'}), 400
        
        public_dir = os.path.join(os.getcwd(), "backend", "public")
        files_to_delete = []

        try:
            unique_id = uuid.uuid4().hex
            base_filename = f'cfg_{unique_id}'
            dot_file_path = os.path.join(public_dir, base_filename + '.dot')
            files_to_delete.append(dot_file_path)

            dot_content = generate_graphviz(code, base_filename, public_dir)
            types = parse_code(code)
            parser = GraphParser.GraphParser(dot_content, types=types)
            
            collection_method = parser.collectionMethod()
            collection_function = parser.collectionFunction()
            collection_main = None
            if types['main'].strip():
                print("types main",types['main'])
                main_filename_base = f'cfg_{uuid.uuid4().hex}'
                main_dot_path = os.path.join(public_dir, main_filename_base + '.dot')
                files_to_delete.append(main_dot_path)

                main_dot = generate_graphviz(types['main'], main_filename_base, public_dir)
                parser_main = GraphParser.GraphParser(main_dot, types=None)
                collection_main = graphviz.Source(parser_main.graphViz(), format='svg').pipe().decode('utf-8')

            return jsonify({
                'class': collection_method,
                'function': collection_function,
                'mainCode': collection_main,
            })
            
        except Exception as e:
            return jsonify({
                'error': 'Failed to process code',
                'details': str(e)
            }), 400
            
        finally:
            for file_path in files_to_delete:
                try:
                    if os.path.exists(file_path):
                        print(f"Successfully deleted file: {file_path}")
                except Exception as e:
                    print(f"Error deleting file {file_path}: {e}")
            
    except Exception as e:
        return jsonify({'error': str(e)}), 500