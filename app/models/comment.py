import abc
from app import db
from sqlalchemy.ext.declarative import declared_attr


class BaseComment(db.Model):

    __abstract__ = True
    __metaclass__ = abc.ABCMeta

    @declared_attr
    def user_id(cls):
        """Foreign key to User table"""
        return db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    @declared_attr
    def get_score(cls):
        """Get score of a comment"""
        return cls.upvote - cls.downvote

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    upvote = db.Column(db.Integer, nullable=False, default=0)
    downvote = db.Column(db.Integer, nullable=False, default=0)
    modified_on = db.Column(
        db.DateTime,
        default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp()
    )

    def save(self):
        db.session.add(self)
        db.session.commit()


class ParentComment(BaseComment):
    """
        Comment to a Thread
    """

    __tablename__ = 'parent_comments'
    link_id = db.Column(db.Integer, db.ForeignKey('links.id'), nullable=True)
    text_id = db.Column(db.Integer, db.ForeignKey('texts.id'), nullable=True)

    @classmethod
    def is_link(self):
        return self.text_id is None


class ChildComment(BaseComment):
    """
        Comment to a Comment
    """

    __tablename__ = 'child_comments'
    comment_id = db.Column(db.Integer, db.ForeignKey('parent_comments.id'))
