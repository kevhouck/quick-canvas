from flask_restful import Resource
from app import db


class Ping(Resource):
    def post(self):
        db.drop_all()
        db.create_all()
        return 'pong'
