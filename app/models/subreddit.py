from app import db


class Subreddit(db.Model):

    __tablename__ = 'subreddits'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True)
    subscriber = db.Column(db.Integer, default=0)
    description = db.Column(db.Text(10000), unique=False)
    created_on = db.Column(
        db.DateTime, nullable=False, default=db.func.current_timestamp()
    )

    def __repr__(self):
        return f"<Subreddit: {self.name} | " + \
            f"Description: {self.description[:50]}>"

    def save(self):
        db.session.add(self)
        db.session.commit()
