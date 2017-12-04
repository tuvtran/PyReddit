from tests.unit.base import BaseUnitTest
from app.models.thread import Thread, Link, Text
from app.models.subreddit import Subreddit
from app.models.user import User


class ThreadModelTest(BaseUnitTest):

    def test_a_link_is_tied_to_a_user(self):
        Link(
            title='Test link',
            link='http://google.com',
            user_id=1,
            subreddit_id=1
        ).save()
        user = User.query.get(1)

        self.assertEqual(user.links.count(), 1)
        self.assertEqual(user.texts.count(), 0)

    def test_a_post_is_tied_to_a_user(self):
        Text(
            title='Test text',
            text='This is a content',
            user_id=1,
            subreddit_id=1
        ).save()
        user = User.query.get(1)

        self.assertEqual(user.links.count(), 0)
        self.assertEqual(user.texts.count(), 1)

    def test_a_post_is_tied_to_a_subreddit(self):
        Text(
            title='Test text',
            text='This is a content',
            user_id=1,
            subreddit_id=1
        ).save()
        subr = Subreddit.query.get(1)

        self.assertEqual(subr.links.count(), 0)
        self.assertEqual(subr.texts.count(), 1)

    def test_a_link_is_tied_to_a_subreddit(self):
        Link(
            title='Test text',
            link='http://google.com',
            user_id=1,
            subreddit_id=1
        ).save()
        subr = Subreddit.query.get(1)

        self.assertEqual(subr.links.count(), 1)
        self.assertEqual(subr.texts.count(), 0)
