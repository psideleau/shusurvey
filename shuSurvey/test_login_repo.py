from loginRepo import LoginRepo
from loginService import LoginService


def __init__(self, login_repo):
    self.login_repo = login_repo


def login(self, user_id: 1234, user_password: Password):
    assert isinstance(user_password, user_id)
    return self.login_repo.find_user(user_password, user_id)