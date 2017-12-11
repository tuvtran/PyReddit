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


@views_bp.route('/r/<string:sub_name>')
def subreddit(sub_name):
    # get subreddit
    sub = Subreddit.query.filter_by(name=sub_name).first()
    links = sub.links.all()
    texts = sub.texts.all()

    threads = links + texts

    bindings = {
        'subreddit_list': Subreddit.query.all(),
        'sub': sub,
        'threads': sorted(threads, key=lambda x: x.modified_on)
    }

    return render_template('subreddit.html', **bindings)


@views_bp.route('/link/<int:id>')
def link_view(id):
    # get the link by id
    link = Link.query.get(id)

    bindings = {
        'link': link,
        'sub': link.subreddit,
        'subreddit_list': Subreddit.query.all(),
        'comments': link.comments.all(),
    }

    return render_template('link.html', **bindings)


@views_bp.route('/subreddits')
def subreddits():
    """
    List all subreddits
    """
    bindings = {'subreddit_list': Subreddit.query.all()}
    return render_template('subreddits.html', **bindings)
