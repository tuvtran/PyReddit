import os
from flask_testing import TestCase
from selenium import webdriver
from app import create_app


class BaseFunctionalTest(TestCase):

    def create_app(self):
        return create_app(config_name='testing')

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.staging_server = os.environ.get('STAGING_SERVER')
        self.live_server_url = self.staging_server or 'http://localhost:5000'

    def tearDown(self):
        self.browser.quit()
