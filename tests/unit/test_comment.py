from tests.unit.base import BaseUnitTest
from app.models.thread import Link, Text, ThreadUpvote, ThreadDownvote
from app.models.comment import Comment
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
        Comment(
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
        Comment(
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
        Comment(
            content="This is a test comment",
            user_id=1,
            text_id=1
        ).save()
        user = User.query.get(1)
        self.assertEqual(user.comments.count(), 1)

    def test_user_has_comment_to_a_comment(self):
        Comment(
            content="This is a test comment",
            user_id=2,
            text_id=1
        ).save()
        pcomment = Comment.query.first()
        Comment(
            content='This is a child comment',
            user_id=1,
            comment_id=pcomment.id
        ).save()
        user = User.query.get(1)
        self.assertEqual(user.comments.count(), 1)

    def test_a_comment_to_a_comment_to_a_comment(self):
        c1 = Comment(
            content="This is a test comment",
            user_id=2,
            text_id=1
        )
        c1.save()

        c2 = Comment(
            content='This is a child comment',
            user_id=1,
            comment_id=c1.id
        )
        c2.save()

        c3 = Comment(
            content='This is a child comment to a child comment',
            user_id=2,
            comment_id=c2.id
        )
        c3.save()

        self.assertEqual(c1.children.count(), 1)
        self.assertEqual(c2.children.count(), 1)
        self.assertEqual(c3.comment_id, c2.id)
        self.assertEqual(c2.comment_id, c1.id)
