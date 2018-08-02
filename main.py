from flask import Flask
from flask import render_template
from flask import request
from flask import make_response
from quote_provider import get_all_quotes

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def home():
    symbol = request.form.get("symbol")
    print(symbol)
    return make_response(render_template("home.html", quotes=get_all_quotes([symbol])))


if __name__ == "__main__":
    app.run(port=8080, debug=True)
