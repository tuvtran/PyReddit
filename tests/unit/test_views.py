from flask import url_for
from tests.unit.base import BaseUnitTest


class HomePageTest(BaseUnitTest):

    def test_get_homepage_200(self):
        response = self.client.get(url_for('views.homepage'))
        self.assert200(response)


class SubredditListPageTest(BaseUnitTest):

    def test_get_subreddit_list_200(self):
        response = self.client.get(url_for('views.subreddit', sub_name='test1'))
        self.assert200(response)
