import datetime
from app import db
from app.models.user import User


class Comment(db.Model):

    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    content = db.Column(db.Text, nullable=False)
    upvote = db.Column(db.Integer, nullable=False, default=0)
    upvoters = db.relationship('CommentUpvote', backref='comment', lazy='dynamic')
    downvoters = db.relationship('CommentDownvote', backref='comment', lazy='dynamic')
    downvote = db.Column(db.Integer, nullable=False, default=0)
    modified_on = db.Column(
        db.DateTime,
        default=datetime.datetime.now(),
        onupdate=datetime.datetime.now(),
    )

    link_id = db.Column(db.Integer, db.ForeignKey('links.id'), nullable=True)
    text_id = db.Column(db.Integer, db.ForeignKey('texts.id'), nullable=True)
    comment_id = db.Column(db.Integer, db.ForeignKey('comments.id'), nullable=True)

    children = db.relationship(
        'Comment', backref=db.backref('parent', remote_side=[id]),
        lazy='dynamic'
    )

    def __repr__(self):
        return f"{self.content} | {self.id}"

    def get_score(self):
        """Get score of a comment"""
        return self.upvote - self.downvote

    def save(self):
        db.session.add(self)
        db.session.commit()
        CommentUpvote(user_id=self.user_id, comment_id=self.id).save()


class CommentUpvote(db.Model):

    __tablename__ = 'comment_upvotes'
    id = db.Column(db.Integer, primary_key=True)
    comment_id = db.Column(db.Integer, db.ForeignKey('comments.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def save(self):
        db.session.add(self)

        # retrieve user to update karma
        comment = Comment.query.get(self.comment_id)
        user = User.query.get(comment.user_id)
        user.comment_karma += 1

        db.session.commit()


class CommentDownvote(db.Model):

    __tablename__ = 'comment_downvotes'
    id = db.Column(db.Integer, primary_key=True)
    comment_id = db.Column(db.Integer, db.ForeignKey('comments.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def save(self):
        db.session.add(self)

        # retrieve user to update karma
        comment = Comment.query.get(self.comment_id)
        user = User.query.get(comment.user_id)
        user.comment_karma -= 1

        db.session.commit()
