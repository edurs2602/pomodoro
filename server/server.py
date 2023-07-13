from flask import Flask
from src import app, db


@app.route('/')
def hello():
    return "Hello World!"


if __name__ == '__main__':
    with app.app_context():
        app.run()
