from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Note(db.Model): #Layout for an object that will be stored in data base
    id = db.Column(db.Integer, primary_key = True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone = True), default = func.now()) #func gets the current date and time and stores it as default value for date
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) #1 user that has many nodes
        

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True) #primary_key is a unique identifier, no same emails
    email = db.Column(db.String(150), unique = True) #no user can have the same email as another user
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')