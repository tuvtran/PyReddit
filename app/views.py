from flask import Blueprint, render_template

# import database models here
from app.models.subreddit import Subreddit
from app.models.thread import Link, Text


views_bp = Blueprint('views', __name__)


@views_bp.route('/')
def homepage():
    links = Link.query.all()
    texts = Text.query.all()
    threads = links + texts

    bindings = {
        'subreddit_list': Subreddit.query.all(),
        'threads': sorted(threads, key=lambda x: x.modified_on)
    }
    return render_template('index.html', **bindings)


@views_bp.route('/subreddits')
def subreddits():
    """
    List all subreddits
    """
    bindings = {'subreddit_list': Subreddit.query.all()}
    return render_template('subreddits.html', **bindings)
