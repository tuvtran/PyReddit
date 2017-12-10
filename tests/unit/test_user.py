from app import bcrypt
from app.models.user import User
from app.models.thread import Link, ThreadUpvote
from app.models.comment import Comment, CommentUpvote
from tests.unit.base import BaseUnitTest


class UserModelTest(BaseUnitTest):

    def test_user_saved_should_have_password_hash(self):
        user = User.query.get(1)
        self.assertTrue(bcrypt.check_password_hash(user.password, 'testing'))

    def test_user_has_1_karma_after_posting(self):
        Link(
            title='Test link',
            link='http://google.com',
            user_id=1,
            subreddit_id=1
        ).save()

        self.assertEqual(User.query.get(1).post_karma, 1)

    def test_user_has_1_karma_after_commenting(self):
        c1 = Comment(
            content="This is a test comment",
            user_id=2,
            text_id=1
        )
        c1.save()

        self.assertEqual(User.query.get(2).comment_karma, 1)

    def test_user_has_n_karma_after_commenting_n_times(self):
        for _ in range(10):
            Comment(
                content="This is a test comment",
                user_id=1,
                comment_id=2
            ).save()

        self.assertEqual(User.query.get(1).comment_karma, 10)

    def test_user_has_karma_after_being_upvoted_post(self):
        l = Link(
            title='Test link',
            link='http://google.com',
            user_id=1,
            subreddit_id=1
        )
        l.save()

        for i in range(10):
            ThreadUpvote(link_id=l.id, user_id=i*10).save()

        self.assertEqual(User.query.get(1).post_karma, 11)

    def test_user_has_karma_after_being_upvoted_comment(self):
        c = Comment(
            content="This is a test comment",
            user_id=1,
            link_id=1
        )
        c.save()

        for i in range(10):
            CommentUpvote(comment_id=c.id, user_id=i*10).save()

        self.assertEqual(User.query.get(1).comment_karma, 11)
