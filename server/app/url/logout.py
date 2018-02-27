from app import db, models
from flask_restful import Resource, Api, reqparse, abort
from flask import Flask, session, request
import flask

app = Flask(__name__)
app.secret_key = '~\xc8\xc6\xe0\xf3,\x98O\xa8z4\xfb=\rNd'
