from app import *
import os
import pytest


@pytest.fixture()
def reset_db(request):
    """ setup any state specific to the execution of the given class (which
    usually contains tests).
    """
    if os.path.exists('../viper.db'):
        os.remove('../viper.db')
    db.app = app
    db.create_all()
    os.system('sqlite3 viper.db < create.sql')

    app_context = app.app_context()
    app_context.push()

    def teardown():
        app_context.pop()

    request.addfinalizer(teardown)
    return app
