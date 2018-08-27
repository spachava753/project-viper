from app import *
import os
import pytest


@pytest.fixture()
def reset_db(request):
    """ setup any state specific to the execution of the given class (which
    usually contains tests).
    """
    if os.path.exists('/home/shashank/working/dev/projects/py/web_apps/project_viper/viper.db'):
        os.remove('/home/shashank/working/dev/projects/py/web_apps/project_viper/viper.db')
    else:
        print("viper.db doesn't exist")
    db.app = app
    db.create_all()
    os.chdir('/home/shashank/working/dev/projects/py/web_apps/project_viper')
    os.system('sqlite3 viper.db < create.sql')

    app_context = app.app_context()
    app_context.push()

    def teardown():
        app_context.pop()

    request.addfinalizer(teardown)
    return app
