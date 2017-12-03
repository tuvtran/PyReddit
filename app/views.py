from flask import Blueprint, render_template

# import database models here
from app.models.subreddit import Subreddit


views_bp = Blueprint('views', __name__)


@views_bp.route('/')
def homepage():
    return render_template('index.html')


@views_bp.route('/subreddits')
def subreddits():
    """
    List all subreddits
    """
    bindings = {'subreddit_list': Subreddit.query.all()}
    return render_template('subreddits.html', **bindings)
