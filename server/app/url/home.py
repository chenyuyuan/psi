from flask import Flask, session, request
import time,datetime
from app import db, models,app
from flask_restful import Resource, Api, reqparse, abort
from flask import Flask, session, request,render_template,url_for
from flask_bootstrap import Bootstrap
from flask import Blueprint
import time,json


bhome=Blueprint('bhome', __name__)

@bhome.route('/home')
def home():
    uid=session["uid"]
    user=[]
    temptopic=[]
    users=models.user.query.all()
    temptopics=models.tempTopic.query.all()
    for key in users:
        if key.id==uid:
            user=key
    for key in temptopics:
        flag0="0"
        if models.tempTopicSupport.query.filter_by(uid=uid,temptopicid=key.id).first():
            flag0="1"
        temptopic.append({
            "id":key.id,
            "uid":key.uid,
            "topic":key.topic,
            "topicIntro":key.topicIntro,
            "support":key.support,
            "time": time.strftime("%m-%d %H:%M:%S", time.localtime(key.time))
        })



    return render_template('/home.html',user=user,temptopic=temptopic)
@bhome.route('/homeadmin')
def homeadmin():
    return render_template('/homeadmin.html')