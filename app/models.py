from flask_sqlalchemy import SQLAlchemy
from app import app 

db = SQLAlchemy()

db.init_app(app)

class Person(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(30))