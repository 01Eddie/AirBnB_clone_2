from flask import Flask
from sqlalchemy.sql.expression import text

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    """ Display: Hello HBNB """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ Display: HBNB """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def C(text):
    """ Display: HBNB """
    return "C " + text.replace('_', ' ')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)