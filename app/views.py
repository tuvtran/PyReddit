from flask import Blueprint, render_template


views_bp = Blueprint('views', __name__)


@views_bp.route('/')
def homepage():
    return render_template('index.html')


@views_bp.route('/subreddits')
def subreddits():
    """
    List all subreddits
    """
    return render_template('subreddits.html')
