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
        db.session.commit()


class ThreadDownvote(db.Model):

    __tablename__ = 'thread_downvotes'
    id = db.Column(db.Integer, primary_key=True)
    link_id = db.Column(db.Integer, db.ForeignKey('links.id'), nullable=True)
    text_id = db.Column(db.Integer, db.ForeignKey('texts.id'), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def save(self):
        db.session.add(self)
        db.session.commit()


class Text(Thread):

    __tablename__ = 'texts'
    text = db.Column(db.Text, nullable=False)
    upvoters = db.relationship('ThreadUpvote', backref='text', lazy='dynamic')
    downvoters = db.relationship('ThreadDownvote', backref='text', lazy='dynamic')
    comments = db.relationship('ParentComment', backref='text', lazy='dynamic')

    def __repr__(self):
        return f'<Text: {self.title}>'

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
    comments = db.relationship('ParentComment', backref='link', lazy='dynamic')

    def __repr__(self):
        return f'<Link: {self.title}>'

    @classmethod
    def is_link(self):
        return True

    def save(self):
        super().save()
        ThreadUpvote(user_id=self.user_id, link_id=self.id).save()
