#import login
#import watchlist
#import home
from app import app, db

if __name__ == "__main__":
    import subprocess
    subprocess.run('./reset.sh')
    db.create_all()
    app.run(port=8080, debug=False, host='0.0.0.0')
