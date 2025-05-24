from flask import Blueprint, request, jsonify
import uuid, os, graphviz
from py2cfg import CFGBuilder
from ..parsers import GraphParser

current_directory = os.getcwd()
method_bp = Blueprint('method', __name__)

@method_bp.route('/method', methods=['POST'])
def method():
    try:
        data = request.get_json()
        code = data.get('code', '')
        
        if not code:
            return jsonify({'error': 'No code provided'}), 400
        
        unique_id = uuid.uuid4().hex
        base_filename = f'cfg_{unique_id}'
        output_path = os.path.join(current_directory, "backend", "public", base_filename)
        
        try:
            cfg_builder = CFGBuilder()
            cfg = cfg_builder.build_from_src(base_filename, code)
            
            cfg.build_visual(output_path, 'dot', show=False)
            dot_file = output_path + '.dot'
            with open(dot_file, 'r', encoding='utf-8') as f:
                dot_content = f.read()

            parser = GraphParser.GraphParser(dot_content)

            print("check parsing result")
            # parser.print()

            collectionMethod = parser.collectionMethod()
            
            return jsonify({
                'result': collectionMethod,
            })
            
        except Exception as e:
            return jsonify({
                'error': f'Failed to process code: {str(e)}',
                'details': 'The code might contain syntax that cannot be visualized'
            }), 400
            
    except Exception as e:
        return jsonify({'error': str(e)}), 500
