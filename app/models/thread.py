import abc
import datetime
import timeago
from app import db
from app.models.user import User
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

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    upvote = db.Column(db.Integer, nullable=False, default=0)
    downvote = db.Column(db.Integer, nullable=False, default=0)
    modified_on = db.Column(
        db.DateTime,
        default=datetime.datetime.now(),
        onupdate=datetime.datetime.now()
    )

    @abc.abstractclassmethod
    def is_link(cls):
        """Return 0 for link, 1 for text"""
        ...

    def save(self):
        db.session.add(self)
        db.session.commit()


class ThreadUpvote(db.Model):

    __tablename__ = 'thread_upvotes'
    id = db.Column(db.Integer, primary_key=True)
    link_id = db.Column(db.Integer, db.ForeignKey('links.id'), nullable=True)
    text_id = db.Column(db.Integer, db.ForeignKey('texts.id'), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def save(self):
        db.session.add(self)

        # retrieve user to update karma
        if self.link_id:
            link = Link.query.get(self.link_id)
            _id = link.user_id
            link.upvote += 1
        else:
            text = Text.query.get(self.text_id)
            _id = text.user_id
            text.upvote += 1
        user = User.query.get(_id)
        user.post_karma += 1

        db.session.commit()


class ThreadDownvote(db.Model):

    __tablename__ = 'thread_downvotes'
    id = db.Column(db.Integer, primary_key=True)
    link_id = db.Column(db.Integer, db.ForeignKey('links.id'), nullable=True)
    text_id = db.Column(db.Integer, db.ForeignKey('texts.id'), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def save(self):
        db.session.add(self)

        # retrieve user to update karma
        if self.link_id:
            link = Link.query.get(self.link_id)
            _id = link.user_id
            link.downvote += 1
        else:
            text = Text.query.get(self.text_id)
            _id = text.user_id
            text.downvote += 1
        user = User.query.get(_id)
        user.post_karma -= 1

        db.session.commit()


class Text(Thread):

    __tablename__ = 'texts'
    text = db.Column(db.Text, nullable=False)
    upvoters = db.relationship('ThreadUpvote', backref='text', lazy='dynamic')
    downvoters = db.relationship('ThreadDownvote', backref='text', lazy='dynamic')
    comments = db.relationship('Comment', backref='text', lazy='dynamic')

    def __repr__(self):
        return f'<Text: {self.title}>'

    def get_score(self):
        return self.upvote - self.downvote

    def get_time(self):
        now = datetime.datetime.now()
        return timeago.format(now, self.modified_on)

    @classmethod
    def is_link(self):
        return False

    def save(self):
        super().save()
        ThreadUpvote(user_id=self.user_id, text_id=self.id).save()


class Link(Thread):

    __tablename__ = 'links'
    link = db.Column(db.String(255), nullable=False)
    upvoters = db.relationship('ThreadUpvote', backref='link', lazy='dynamic')
    downvoters = db.relationship('ThreadDownvote', backref='link', lazy='dynamic')
    comments = db.relationship('Comment', backref='link', lazy='dynamic')

    def __repr__(self):
        return f'<Link: {self.title}>'

    def get_score(self):
        return self.upvote - self.downvote

    def get_time(self):
        now = datetime.datetime.now()
        return timeago.format(now, self.modified_on)

    @classmethod
    def is_link(self):
        return True

    def save(self):
        super().save()
        ThreadUpvote(user_id=self.user_id, link_id=self.id).save()
