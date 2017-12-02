from flask_testing import TestCase
from app import create_app, db


class BaseUnitTest(TestCase):

    def create_app(self):
        return create_app(config_name='testing')

    def setUp(self):
        db.create_all()
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
