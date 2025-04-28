from flask import Flask, request, jsonify
from flask_cors import CORS
from py2cfg import CFGBuilder
import os
import tempfile

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/visualize', methods=['POST'])
def visualize_code():
    try:
        # Get code from request
        data = request.get_json()
        code = data.get('code', '')
        
        if not code:
            return jsonify({'error': 'No code provided'}), 400
        
        # Create temp directory if it doesn't exist
        temp_dir = os.path.join(tempfile.gettempdir(), 'cfg_visualizer')
        os.makedirs(temp_dir, exist_ok=True)
        
        # Generate CFG
        cfg_builder = CFGBuilder()
        cfg = cfg_builder.build_from_src("temp", code)
        
        # Save visualization
        output_path = os.path.join(temp_dir, 'cfg')
        cfg.build_visual(output_path, 'svg')
        
        # Read the DOT file
        dot_file = output_path + '.dot'
        with open(dot_file, 'r') as f:
            dot_content = f.read()
        
        # Return both SVG and DOT representations
        svg_file = output_path + '.svg'
        with open(svg_file, 'r') as f:
            svg_content = f.read()
        
        return jsonify({
            'dot': dot_content,
            'svg': svg_content
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)