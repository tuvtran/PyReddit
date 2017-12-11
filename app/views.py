from flask import Blueprint, render_template, redirect
from flask import request
# import database models here
from app.models.subreddit import Subreddit
from app.models.thread import Link, Text
from app.models.comment import Comment


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


@views_bp.route('/r/<string:sub_name>/submit', methods=['POST', 'GET'])
def subreddit_submit(sub_name):
    # get subreddit
    sub = Subreddit.query.filter_by(name=sub_name).first()

    if request.method == 'POST':
        # handle form data here
        data = request.form
        if data['type'] == 'linkOption':
            Link(
                title=data['title'],
                link=data['url'],
                subreddit_id=sub.id,
                user_id=2
            ).save()
        else:
            Text(
                title=data['title'],
                text=data['text'],
                subreddit_id=sub.id,
                user_id=2
            ).save()

        return redirect(f'/r/{sub.name}')

    bindings = {
        'sub': sub,
        'subreddit_list': Subreddit.query.all(),
    }

    return render_template('submit.html', **bindings)


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


@views_bp.route('/link/<int:id>/reply', methods=['POST'])
def reply_link(id):
    data = request.form

    Comment(
        content=data['content'],
        user_id=2,
        link_id=id
    ).save()

    return redirect(f'/link/{id}')


@views_bp.route('/text/<int:id>')
def text_view(id):
    # get the link by id
    text = Text.query.get(id)

    bindings = {
        'text': text,
        'sub': text.subreddit,
        'subreddit_list': Subreddit.query.all(),
        'comments': text.comments.all(),
    }

    return render_template('text.html', **bindings)


@views_bp.route('/text/<int:id>/reply', methods=['POST'])
def reply_text(id):
    data = request.form

    Comment(
        content=data['content'],
        user_id=2,
        text_id=id
    ).save()

    return redirect(f'/text/{id}')
