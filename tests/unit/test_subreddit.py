from tests.unit.base import BaseUnitTest
from app.models import Subreddit


class SubredditModelTest(BaseUnitTest):

    def test_can_create_subreddit_instance(self):
        sbr = {
            'name': 'random',
            'desc': 'This is a testing and random subreddit'
        }

        new_subreddit = Subreddit(
            name=sbr['name'],
            description=sbr['desc']
        )

        self.assertEqual(new_subreddit.name, sbr['name'])
        self.assertEqual(new_subreddit.description, sbr['desc'])

    def test_can_save_subreddit_instance(self):
        sbr = {
            'name': 'random',
            'desc': 'This is a testing and random subreddit'
        }

        new_subreddit = Subreddit(
            name=sbr['name'],
            description=sbr['desc']
        )
        new_subreddit.save()

        self.assertEqual(Subreddit.query.count(), 4)
