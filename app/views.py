from flask import Blueprint, render_template, redirect
from flask import request, jsonify
# import database models here
from app.models.subreddit import Subreddit
from app.models.thread import Link, Text, ThreadUpvote, ThreadDownvote
from app.models.comment import Comment


views_bp = Blueprint('views', __name__)


@views_bp.route('/')
def homepage():
    links = Link.query.all()
    texts = Text.query.all()
    threads = links + texts

    bindings = {
        'subreddit_list': Subreddit.query.all(),
        'threads': sorted(threads, key=lambda x: x.get_score(), reverse=True)
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
        'threads': sorted(threads, key=lambda x: x.get_score(), reverse=True)
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


@views_bp.route('/comment/<int:id>/reply', methods=['GET', 'POST'])
def reply_comment(id):
    comment = Comment.query.get(id)
    print(comment)

    if request.method == 'POST':
        data = request.form
        Comment(
            content=data['content'],
            user_id=2,
            comment_id=id
        ).save()

        while comment.parent and comment.id:
            comment = comment.parent

        if comment.link_id:
            return redirect(f'/link/{comment.link_id}')
        else:
            return redirect(f'/text/{comment.text_id}')

    bindings = {
        'comment': comment,
        'subreddit_list': Subreddit.query.all(),
    }

    return render_template('comment.html', **bindings)


@views_bp.route('/link/<int:id>/upvote', methods=['POST'])
def upvote_link(id):
    data = request.json
    ThreadUpvote(user_id=data['user_id'], link_id=id).save()
    return jsonify({'message': 'upvoted successfully'})


@views_bp.route('/text/<int:id>/upvote', methods=['POST'])
def upvote_text(id):
    data = request.json
    ThreadUpvote(user_id=data['user_id'], text_id=id).save()
    return jsonify({'message': 'upvoted successfully'})


@views_bp.route('/link/<int:id>/downvote', methods=['POST'])
def downvote_link(id):
    data = request.json
    ThreadDownvote(user_id=data['user_id'], link_id=id).save()
    return jsonify({'message': 'downvoted successfully'})


@views_bp.route('/text/<int:id>/downvote', methods=['POST'])
def downvote_text(id):
    data = request.json
    ThreadDownvote(user_id=data['user_id'], text_id=id).save()
    return jsonify({'message': 'downvoted successfully'})
