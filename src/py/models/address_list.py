from app import db


class AddressList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    addresses = db.relationship('Address')

