from db import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(60))
    lastname = db.Column(db.String(60))
    username = db.Column(db.String(50))
    password = db.Column(db.String(100))
    session_token = db.Column(db.String(50))

class FeatureRequest(db.Model):
    __tablename__ = 'feature_requests'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.String(500))
    client = db.Column(db.String(20))
    priority = db.Column(db.Integer)
    target_date = db.Column(db.DateTime)
    product_area = db.Column(db.String(20))