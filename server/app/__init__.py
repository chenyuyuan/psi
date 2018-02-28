from flask import Flask, request
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, session, request

app = Flask(__name__)

app.config.from_object('config')
api = Api(app)
db = SQLAlchemy(app)
app.secret_key = '~\xc8\xc6\xe0\xf3,\x98O\xa8z4\xfb=\rNd'

from app import models, router,url