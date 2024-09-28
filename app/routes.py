from flask import Blueprint, render_template

# Define a blueprint
bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')  # Render the home page template

@bp.route('/about')
def about():
    return "<h2>This is the about page</h2>"
