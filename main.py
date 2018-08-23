from app import *
from tabledef import *
from rest_api import *
import os
from rest_api.api_config import *

if __name__ == "__main__":
    if os.path.exists('viper.db'):
        os.remove('viper.db')
    db.create_all()
    db.app = app
    os.system('sqlite3 viper.db < create.sql')

    app_context = app.app_context()
    app_context.push()
    app.run(port=8080, debug=False, host='0.0.0.0')
