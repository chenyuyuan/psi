from flask import Flask, session, request

from app import db, models,app
from flask_restful import Resource, Api, reqparse, abort
from flask import Flask, session, request,render_template,url_for
import flask
from flask_bootstrap import Bootstrap
from flask import Blueprint


btopicSquare=Blueprint('btopicSquare', __name__)

@btopicSquare.route('/topicSquare')
def test():
    user = models.user.query.filter_by(id='1').first()
    print(user.password)
    return render_template('/main.html', title=user.password)
