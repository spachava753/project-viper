from app import app
import random
import hashlib

import login
#import watchlist
import home

if __name__ == "__main__":
    rand_int = str(random.randint(1, 1001))
    app.secret_key = hashlib.sha256(rand_int.encode()).hexdigest()
    app.run(port=8080, debug=True, host='0.0.0.0')
