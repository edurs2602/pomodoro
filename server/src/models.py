from flask_bcrypt import bcrypt
from . import db, app


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True),
    username = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = bcrypt.hashpw(
            password.encode('utf-8'), bcrypt.gensalt())

    def check_password(self, pwd):
        return bcrypt.checkpw(pwd.encode('utf-8'), self.password)
