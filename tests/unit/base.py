from flask_testing import TestCase
from app import create_app, db
from app.models.user import User
from app.models.subreddit import Subreddit


class BaseUnitTest(TestCase):

    def create_app(self):
        return create_app(config_name='testing')

    def setUp(self):
        db.drop_all()
        db.create_all()
        db.session.commit()

        # Create some test data in database
        self._create_test_user()
        self._create_test_subreddits()

    def _create_test_user(self):
        User(
            name='tester',
            email='tester@test.com',
            password='testing'
        ).save()
        return User.query.first()

    def _create_test_subreddits(self):
        Subreddit(name='test1', description='For testing 1').save()
        Subreddit(name='test2', description='For testing 2').save()
        Subreddit(name='test3', description='For testing 3').save()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
