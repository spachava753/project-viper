from flask import Flask
from flask import render_template
from flask import request
from flask import make_response
from quote_provider import get_all_quotes
import datetime
import random
import hashlib

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
@app.route("/<symbol>", methods=["POST", "GET"])
def home(symbol=""):
    if not symbol:
        print("Add Symbol")
        symbol = request.form.get("symbol")
        symbols = request.cookies.get("symbols")

        if symbols:
            if symbol:
                symbol = symbol.upper()
                symbols = symbols.split(',')
                symbols.append(symbol)
                symbols = set(symbols)
        elif symbol:
            symbols = [symbol]
        else:
            symbols = []

        response = make_response(render_template("home.html", quotes=get_all_quotes(symbols)))

        if symbols:
            cookie_symbols = ','.join(symbols)
            expires = datetime.datetime.now() + datetime.timedelta(365)
            response.set_cookie("symbols", cookie_symbols, expires=expires)
            print(cookie_symbols)

        return response
    else:
        print("Remove Symbol")
        symbols = request.cookies.get("symbols")
        if symbols:
            symbol = symbol.upper()
            if ',' in symbols:
                symbols = symbols.split(',')
                symbols.remove(symbol)
                symbols = set(symbols)
            else:
                symbols = []

            response = make_response(render_template("home.html", quotes=get_all_quotes(symbols)))

            if symbols:
                cookie_symbols = ','.join(symbols)
                print(cookie_symbols)
            else:
                cookie_symbols = ""

            expires = datetime.datetime.now() + datetime.timedelta(365)
            response.set_cookie("symbols", cookie_symbols, expires=expires)
        else:
            response = make_response(render_template("home.html", quotes=get_all_quotes(symbols)))

        return response


if __name__ == "__main__":
    rand_int = str(random.randint(1, 1001))
    app.secret_key = hashlib.sha256(rand_int.encode()).hexdigest()
    app.run(port=8080, debug=True)
