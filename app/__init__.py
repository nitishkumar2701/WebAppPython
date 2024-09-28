from flask import Flask

def create_app():
    # Create and configure the Flask app
    app = Flask(__name__)
    
    # Import and register the routes blueprint
    from .routes import bp as main_bp
    app.register_blueprint(main_bp)
    
    return app
