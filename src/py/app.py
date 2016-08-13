from flask import Flask
from flask_restful import Api
from routes_setup import *
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
app.config.from_object("config.DevelopmentConfig")
db = SQLAlchemy(app)
CORS(app)
