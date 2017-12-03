from app import bcrypt
from app.models.user import User
from tests.unit.base import BaseUnitTest


class UserModelTest(BaseUnitTest):

    def test_user_saved_should_have_password_hash(self):
        user = User.query.get(1)
        self.assertTrue(bcrypt.check_password_hash(user.password, 'testing'))
