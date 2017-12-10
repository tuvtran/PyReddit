import abc
from app import db
from sqlalchemy.ext.declarative import declared_attr


class Comment(db.Model):

    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    content = db.Column(db.Text, nullable=False)
    upvote = db.Column(db.Integer, nullable=False, default=0)
    downvote = db.Column(db.Integer, nullable=False, default=0)
    modified_on = db.Column(
        db.DateTime,
        default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp()
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
