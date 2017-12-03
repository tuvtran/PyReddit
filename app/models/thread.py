import abc
from app import db
from sqlalchemy.ext.declarative import declared_attr


class Thread(db.Model):

    __abstract__ = True
    __metaclass__ = abc.ABCMeta

    @declared_attr
    def user_id(cls):
        """Foreign key to User table"""
        return db.Column(db.Integer, db.ForeignKey('users.id'))

    @declared_attr
    def subreddit_id(cls):
        """Foreign key to Subreddit table"""
        return db.Column(db.Integer, db.ForeignKey('subreddits.id'))

    @declared_attr
    def get_score(cls):
        """Get score of a thread"""
        return cls.upvote - cls.downvote

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    upvote = db.Column(db.Integer, nullable=False, default=0)
    downvote = db.Column(db.Integer, nullable=False, default=0)
    modified_on = db.Column(
        db.DateTime,
        default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp()
    )

    @abc.abstractclassmethod
    def link_or_text(cls):
        """Return 0 for link, 1 for text"""
        ...

    def save(self):
        db.session.add(self)
        db.session.commit()
