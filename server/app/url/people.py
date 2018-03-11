from flask import Flask, session, request
import time,datetime
from app import db, models,app
from flask_restful import Resource, Api, reqparse, abort
from flask import Flask, session, request,render_template,url_for,redirect
from flask_bootstrap import Bootstrap
from flask import Blueprint


bpeople=Blueprint('bpeople', __name__)

@bpeople.route('/people/me/myask')
def people():
    uid=session["uid"]
    users=models.user.query.all()
    user={}
    for key in users:
        if key.id==uid:
            user=key
    question=models.question.query.all()
    return render_template('/pageofmine.html', title='我的主页', users=users,user=user)
@bpeople.route('/people/<uid>/ask')
def others(uid):
    # myid=session["uid"]
    # if myid==uid:
    #     return redirect('http://127.0.0.1:3000/people/me/myask')
    return render_template('/pageofothers.html')