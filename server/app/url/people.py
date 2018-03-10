from flask import Flask, session, request
import time,datetime
from app import db, models,app
from flask_restful import Resource, Api, reqparse, abort
from flask import Flask, session, request,render_template,url_for
from flask_bootstrap import Bootstrap
from flask import Blueprint


bpeople=Blueprint('bpeople', __name__)

@bpeople.route('/people/me/')
def people():
    uid=session["uid"]
    users=models.user.query.all()
    return render_template('/pageofmine.html', title='我的主页', users=users)