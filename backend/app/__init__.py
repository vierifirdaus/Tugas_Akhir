from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)

    # Register blueprints/routes
    from .routes.visualize import visualize_bp
    from .routes.source import source_bp
    from .routes.parse import parse_bp

    app.register_blueprint(visualize_bp)
    app.register_blueprint(source_bp)
    app.register_blueprint(parse_bp)

    return app
