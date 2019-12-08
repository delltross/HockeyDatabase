from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import app

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///example.sqlite"
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first = db.Column(db.String, unique=True, nullable=False)
    last = db.Column(db.String, unique=False, nullable=True)
    special = db.Column(db.String, unique=False, nullable=True)
    number = db.Column(db.String, unique=False, nullable=True)
    position = db.Column(db.String, unique=False, nullable=True)
    shoots = db.Column(db.String, unique=False, nullable=True)
    weight = db.Column(db.String, unique=False, nullable=True)
    height = db.Column(db.String, unique=False, nullable=True)


if __name__ == '__main__':
    # db.create_all()