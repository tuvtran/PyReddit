from tests.unit.base import BaseUnitTest
from app.models.thread import Link, Text, ThreadUpvote
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

    def test_user_can_upvote_a_link(self):
        Link(
            title='Test text',
            link='http://google.com',
            user_id=2,
            subreddit_id=1
        ).save()
        user = User.query.first()
        link = Link.query.first()

        ThreadUpvote(user_id=user.id, link_id=link.id).save()

        self.assertEqual(user.has_upvoted.count(), 1)
        self.assertEqual(link.upvoters.count(), 1)

    def test_user_can_upvote_a_text(self):
        Text(
            title='Test text',
            text='This is a content',
            user_id=2,
            subreddit_id=1
        ).save()
        user = User.query.first()
        text = Text.query.first()

        ThreadUpvote(user_id=user.id, text_id=text.id).save()

        self.assertEqual(user.has_upvoted.count(), 1)
        self.assertEqual(text.upvoters.count(), 1)
