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
            "isupport":flag0,
            "topicIntro":key.topicIntro,
            "support":key.support,
            "time": time.strftime("%m-%d %H:%M:%S", time.localtime(key.time))
        })
    temptopic=temptopic[::-1]
    answers=models.answer.query.all()
    

    return render_template('/home.html',user=user,temptopic=temptopic)
@bhome.route('/homeadmin')
def homeadmin():
    return render_template('/homeadmin.html')

@bhome.route('/home/applyingtopic',methods=['GET','POST'])
def applyingtopic():
    thistime=int(time.time())
    req=request.get_json()
    topic=req["topic"]
    topicintro=req["topicintro"]
    uid=session["uid"]
    if models.tempTopic.query.filter_by(topic=topic).first():
        return json.dumps({"msg":"existing"})
    else:
        temptopics=models.tempTopic.query.all()
        maxid=temptopics[len(temptopics)-1].id+1
        temptopic=models.tempTopic()
        temptopic.id=maxid
        temptopic.topic=topic
        temptopic.uid=uid
        temptopic.topicIntro=topicintro
        temptopic.support=0
        temptopic.time=thistime
        db.session.add(temptopic)
        db.session.commit()
        return json.dumps({"msg":"good"})
@bhome.route('/home/supporting',methods=['GET','POST'])
def supporting():
    thistime=int(time.time())
    req=request.get_json()
    flag=req["flag"]
    temptopicid=req["temptopicid"]
    uid=session["uid"]
    #flag=0要支持
    if flag=="0":
        temptopicsupport=models.tempTopicSupport()
        temptopicsupports=models.tempTopicSupport.query.all()
        maxid=temptopicsupports[len(temptopicsupports)-1].id+1
        temptopicsupport.id=maxid
        temptopicsupport.uid=uid
        temptopicsupport.temptopicid=temptopicid
        db.session.add(temptopicsupport)
        db.session.commit()
        temptopic=models.tempTopic.query.filter_by(id=temptopicid).first()
        if temptopic:
            if temptopic.support==9:
                topic=models.topic()
                topics=models.topic.query.all()
                maxid=topics[len(topics)-1].id+1
                topic.id=maxid
                topic.topic=temptopic.topic
                topic.starCount=0
                topic.time=thistime
                topic.topicIntro=temptopic.topicIntro
                topic.queCount=0
                topic.picture=0
                db.session.add(topic)
                db.session.commit()
                db.session.delete(temptopic)
                db.session.commit()
                return json.dumps({"msg":"finished"})
            elif temptopic.support!=9:
                temptopic.support=temptopic.support+1
                db.session.commit()
                return json.dumps({"msg":"supported"})
    elif flag=="1":
        temptopicsupport=models.tempTopicSupport.query.filter_by(uid=uid,temptopicid=temptopicid).first()
        temptopicsupport.uid=0
        db.session.commit()
        temptopic = models.tempTopic.query.filter_by(id=temptopicid).first()
        temptopic.support=temptopic.support-1
        db.session.commit()
        return json.dumps({"msg":"canceled"})
