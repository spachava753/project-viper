#import login
#import watchlist
#import home

if __name__ == "__main__":
    import subprocess
    subprocess.run('./reset.sh')
    from app import app
    app.run(port=8080, debug=True, host='0.0.0.0')
