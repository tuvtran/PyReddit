from tests.unit.base import BaseUnitTest


class CurrentAppConfigurations(BaseUnitTest):

    def test_app_is_testing(self):
        self.assertTrue(self.app.config['TESTING'])
        self.assertTrue(self.app.config['DEBUG'])
        self.assertEqual(self.app.config['EXP'], 2)
