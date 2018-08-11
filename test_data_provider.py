from data_provider import *
from app import *
import pytest
import subprocess


@pytest.fixture()
def reset_db(request):
    """ setup any state specific to the execution of the given class (which
    usually contains tests).
    """
    subprocess.run('./reset.sh')
    db.app = app
    db.create_all()
    app_context = app.app_context()
    app_context.push()

    def teardown():
        app_context.pop()

    request.addfinalizer(teardown)
    return app


@pytest.mark.usefixtures("reset_db")
class TestUsers(object):

    def test_get_users(self):
        users = get_users()
        print("users:", users)
        assert len(users) == 3
        assert isinstance(users, list)
        for user in users:
            print(user.id, user.password, user.watchlists, sep=', ')

    def test_get_user_with_user_id(self):
        user = get_users(user_id=41)
        assert isinstance(user, object)
        print("user: ", user)
        assert user.username == 'admin41'

    def test_get_user_with_username(self):
        user = get_users(username='admin41')
        assert isinstance(user, object)
        print("user: ", user)
        assert user.id == '41'

    def test_add_user(self):
        original_len = len(get_users())
        username = 'python'
        password = 'pythonpass'
        add_users(username, password)
        assert len(get_users()) == original_len + 1

    def test_delete_user_with_username(self):
        original_len = len(get_users())
        username = 'user21'
        delete_users(username=username)
        assert len(get_users()) == original_len - 1

    def test_delete_user_with_username(self):
        original_len = len(get_users())
        user_id = 21
        delete_users(user_id=user_id)
        assert len(get_users()) == original_len - 1

    def test_update_user_with_username(self):
        original_len = len(get_users())

        user_id = 41
        new_username = 'admin-guy'

        num_watchlists = len(get_users(user_id=user_id).watchlists)
        assert num_watchlists > 0

        update_user(user_id=user_id, username=new_username)
        assert len(get_users()) == original_len

        updated_user = get_users(username=new_username)
        print(updated_user.id)
        assert updated_user.id == str(user_id)
        assert len(updated_user.watchlists) == num_watchlists

    def test_update_user_with_password(self):
        original_len = len(get_users())

        user_id = 41
        new_password = 'Pa55word'

        num_watchlists = len(get_users(user_id=user_id).watchlists)
        assert num_watchlists > 0

        update_user(user_id=user_id, password=new_password)
        assert len(get_users()) == original_len

        updated_user = get_users(user_id=user_id)
        print(updated_user.id)
        assert updated_user.id == str(user_id)
        assert len(updated_user.watchlists) == num_watchlists
        assert updated_user.password == new_password

    def test_update_user(self):
        original_len = len(get_users())

        user_id = 41
        new_password = 'Pa55word'
        new_username = 'admin-guy'

        num_watchlists = len(get_users(user_id=user_id).watchlists)
        assert num_watchlists > 0

        update_user(user_id=user_id, password=new_password, username=new_username)
        assert len(get_users()) == original_len

        updated_user = get_users(user_id=user_id)
        print(updated_user.id)
        assert updated_user.id == str(user_id)
        assert len(updated_user.watchlists) == num_watchlists
        assert updated_user.password == new_password
        assert updated_user.username == new_username
