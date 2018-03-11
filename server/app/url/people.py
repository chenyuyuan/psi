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
    question=[]
    for key in users:
        if key.id==uid:
            user=key
    questions=models.question.query.all()
    for key in question:
        if key.uid==uid:
            flag="0"
            if models.queLike.query.filter_by(uid=uid, queid=key.id).first():
                print("查到")
                flag = "1"
            question.append({
                "id":key.id,
                "question":key.question,
                "like":key.like,
                "ilike":flag,
                "ansCount":key.ansCount,
                "time":key.time,
                "reltopicid":key.reltopicid,
                "followerCount":key.followerCount,
                "queContent":key.queContent
            })
    return render_template('/pageofmine.html', title='我的主页',type="question", users=users,user=user,question=question)
@bpeople.route('/people/<uid>/ask')
def others(uid):
    # myid=session["uid"]
    # if myid==uid:
    #     return redirect('http://127.0.0.1:3000/people/me/myask')
    return render_template('/pageofothers.html')