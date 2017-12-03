from app import bcrypt
from app.models.user import User
from tests.unit.base import BaseUnitTest


class UserModelTest(BaseUnitTest):

    def test_user_saved_should_have_password_hash(self):
        User(name='test', password='testing', email='test@test.com').save()
        user = User.query.first()
        self.assertTrue(bcrypt.check_password_hash(user.password, 'testing'))
