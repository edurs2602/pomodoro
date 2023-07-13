from flask import Flask

app = Flask(__name__)


@app.route("/home")
def index():
    return {
        "name": "Pedro",
        "age": "23",
        "country": "Brazil",
    }


if __name__ == '__main__':
    app.run(debug=True)
