from flask import Blueprint, request, jsonify
import uuid, os, graphviz
from py2cfg import CFGBuilder
from ..parsers import GraphParser

current_directory = os.getcwd()
method_bp = Blueprint('method', __name__)

import ast
def parse_code(code):
    tree = ast.parse(code)
    result = {'class': [], 'function': [], 'main': ''}

    main_code = []
    for node in tree.body:
        if isinstance(node, ast.FunctionDef):
            result['function'].append(node.name)
        elif isinstance(node, ast.ClassDef):
            class_data = {
                'classname': node.name,
                'method': []
            }
            for class_node in node.body:
                if isinstance(class_node, ast.FunctionDef):
                    class_data['method'].append(class_node.name)
            result['class'].append(class_data)
        else:
            main_code.append(ast.unparse(node))

    result['main'] = "\n".join(main_code)
    return result


@method_bp.route('/method', methods=['POST'])
def method():
    try:
        data = request.get_json()
        code = data.get('code', '')
        
        if not code:
            return jsonify({'error': 'No code provided'}), 400
        
        unique_id_code = uuid.uuid4().hex
        base_filename_code = f'cfg_{unique_id_code}'
        output_path_code = os.path.join(current_directory, "backend", "public", base_filename_code)
        
        unique_id_main = uuid.uuid4().hex
        base_filename_main = f'cfg_{unique_id_main}'
        output_path_main = os.path.join(current_directory, "backend", "public", base_filename_main)

        try:
            cfg_builder = CFGBuilder()
            cfg = cfg_builder.build_from_src(base_filename_code, code)
            
            cfg.build_visual(output_path_code, 'dot', show=False)
            dot_file = output_path_code + '.dot'
            with open(dot_file, 'r', encoding='utf-8') as f:
                dot_content_code = f.read()
            types = parse_code(code)
            parser = GraphParser.GraphParser(dot_content_code,types=types)

            # print("check parsing result")
            # parser.print()

            collectionMethod = parser.collectionMethod()
            collectionFunction = parser.collectionFunction()
            
            mainCode = types['main']
            print("Main code:", mainCode)
            cfg_builder_main = CFGBuilder()
            cfg_main = cfg_builder_main.build_from_src(base_filename_main, mainCode)
            
            cfg_main.build_visual(output_path_main, 'dot', show=False)
            dot_file_main = output_path_main + '.dot'
            with open(dot_file_main, 'r', encoding='utf-8') as f:
                dot_content_main = f.read()
            parserMain = GraphParser.GraphParser(dot_content_main,types=None)
            parserMain.print()
            parserMain = parserMain.graphViz()
            collectionMain = graphviz.Source(parserMain, format='svg').pipe().decode('utf-8')

            return jsonify({
                'class': collectionMethod,
                'function': collectionFunction,
                'mainCode': collectionMain,
            })
            
        except Exception as e:
            return jsonify({
                'error': f'Failed to process code: {str(e)}',
                'details': 'The code might contain syntax that cannot be visualized'
            }), 400
            
    except Exception as e:
        return jsonify({'error': str(e)}), 500
