import os
from app import db, bcrypt


class User(db.Model):

    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    registered_on = db.Column(
        db.DateTime, nullable=False, default=db.func.current_timestamp()
    )

    texts = db.relationship('Text', backref='user', lazy='dynamic')
    links = db.relationship('Link', backref='user', lazy='dynamic')

    comments = db.relationship('Comment', backref='user', lazy='dynamic')

    post_karma = db.Column(db.Integer, nullable=False, default=0)
    comment_karma = db.Column(db.Integer, nullable=False, default=0)

    has_upvoted = db.relationship('ThreadUpvote', backref='user', lazy='dynamic')
    has_downvoted = db.relationship('ThreadDownvote', backref='user', lazy='dynamic')

    has_upvoted_comment = db.relationship(
        'CommentUpvote', backref='user', lazy='dynamic'
    )
    has_downvoted_comment = db.relationship(
        'CommentDownvote', backref='user', lazy='dynamic'
    )

    def __repr__(self):
        return f'<User: {self.name}>'

    def save(self):
        # generate a hash in the database
        self.password = bcrypt.generate_password_hash(
            self.password, os.environ.get('BCRYPT_LOG_ROUNDS', 4)
        ).decode()

        db.session.add(self)
        db.session.commit()
