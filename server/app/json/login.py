from app import db, models
from flask_restful import Resource, Api, reqparse, abort
from flask import Flask, session, request
import flask

app = Flask(__name__)
app.secret_key = '~\xc8\xc6\xe0\xf3,\x98O\xa8z4\xfb=\rNd'
class planHotel(Resource):
    def get(self):
        uid = request.args.get('uid')
        psw = request.args.get('psw')
        if uid and psw:
            session['uid'] = uid
            session['_login'] = True
            return '<h1>login succeed!</h1>'
        return '<h1>login failed</h1>'