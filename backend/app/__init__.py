from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)

    from .routes.visualize import visualize_bp
    from .routes.source import source_bp
    from .routes.parse import parse_bp
    from .routes.method import method_bp
    from .routes.attribute import attribute_bp
    from .routes.call_graph import call_graph_bp
    from .routes.pdg import pdg_bp
    from .routes.hello import hello_bp

    app.register_blueprint(visualize_bp)
    app.register_blueprint(source_bp)
    app.register_blueprint(parse_bp)
    app.register_blueprint(method_bp)
    app.register_blueprint(attribute_bp)
    app.register_blueprint(call_graph_bp)
    app.register_blueprint(pdg_bp)
    app.register_blueprint(hello_bp)
    
    return app
