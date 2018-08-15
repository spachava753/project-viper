#import login
#import watchlist
#import home
from app import *
from tabledef import *
import os

if __name__ == "__main__":
    if os.path.exists('viper.db'):
        os.remove('viper.db')
    db.create_all()
    db.app = app
    os.system('sqlite3 viper.db < create.sql')

    app_context = app.app_context()
    app_context.push()
    app.run(port=8080, debug=False, host='0.0.0.0')
