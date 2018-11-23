from app import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String())
    lastname = db.Column(db.String())
    username = db.Column(db.String())
    password = db.Column(db.String())

class FeatureRequest(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)