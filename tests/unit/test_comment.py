from tests.unit.base import BaseUnitTest
from app.models.thread import Link, Text, ThreadUpvote, ThreadDownvote
from app.models.comment import ParentComment
from app.models.subreddit import Subreddit
from app.models.user import User


class CommentModelTest(BaseUnitTest):

    def test_can_create_a_comment_for_a_link(self):
        Link(
            title='Test link',
            link='http://google.com',
            user_id=1,
            subreddit_id=1
        ).save()
        link = Link.query.first()
        ParentComment(
            content="This is a test comment",
            user_id=1,
            link_id=link.id
        ).save()
        self.assertEqual(link.comments.count(), 1)

    def test_can_create_a_comment_for_a_post(self):
        Text(
            title='Test text',
            text='This is a content',
            user_id=1,
            subreddit_id=1
        ).save()
        text = Text.query.first()
        ParentComment(
            content="This is a test comment",
            user_id=1,
            text_id=text.id
        ).save()
        self.assertEqual(text.comments.count(), 1)

    def test_user_has_comment(self):
        Text(
            title='Test text',
            text='This is a content',
            user_id=1,
            subreddit_id=1
        ).save()
        ParentComment(
            content="This is a test comment",
            user_id=1,
            text_id=1
        ).save()
        user = User.query.get(1)
        self.assertEqual(user.thread_comments.count(), 1)
