from flask import Blueprint, request, jsonify
import uuid, os, graphviz
from py2cfg import CFGBuilder
from ..parsers import GraphParser

visualize_bp = Blueprint('visualize', __name__)
current_directory = os.getcwd()
@visualize_bp.route('/visualize', methods=['POST'])
def visualize_code():
    try:
        data = request.get_json()
        code = data.get('code', '')
        
        if not code:
            return jsonify({'error': 'No code provided'}), 400
        
        unique_id = uuid.uuid4().hex
        base_filename = f'cfg_{unique_id}'
        output_path = os.path.join(current_directory+"\\backend\\public\\", base_filename)
        
        cfg_builder = CFGBuilder()
        cfg = cfg_builder.build_from_src(base_filename, code)
        
        cfg.build_visual(output_path, 'svg')
        svg_file = output_path + '.svg'
        with open(svg_file, 'r') as f:
            svg_content = f.read()
        
        return jsonify({
            'svg': svg_content
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500
