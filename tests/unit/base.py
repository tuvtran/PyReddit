from flask_testing import TestCase
from app import create_app


class BaseUnitTest(TestCase):

    def create_app(self):
        return create_app(config_name='testing')

    def setUp(self):
        pass

    def tearDown(self):
        pass
