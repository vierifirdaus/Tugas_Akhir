from flask import Blueprint, request, jsonify
import uuid, os, graphviz
from py2cfg import CFGBuilder
from ..parsers import GraphParser

current_directory = os.getcwd()

# Ganti ke source_bp
source_bp = Blueprint('source', __name__)

@source_bp.route('/source', methods=['POST'])
def source():
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
            
            cfg.build_visual(output_path, 'dot')
            dot_file = output_path + '.dot'
            
            with open(dot_file, 'r', encoding='utf-8') as f:
                dot_content = f.read()
            
            parser = GraphParser.GraphParser(dot_content)
            graphviz_output = parser.graphViz()
            print("resssss ", graphviz_output)

            svg_string = graphviz.Source(graphviz_output, format='svg').pipe().decode('utf-8')
            
            return jsonify({
                'svg': svg_string
            })
            
        except Exception as e:
            return jsonify({
                'error': f'Failed to process code: {str(e)}',
                'details': 'The code might contain syntax that cannot be visualized'
            }), 400
            
    except Exception as e:
        return jsonify({'error': str(e)}), 500
