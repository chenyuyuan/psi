from flask import Flask, session, request
import time,datetime
from app import db, models,app
from flask_restful import Resource, Api, reqparse, abort
from flask import Flask, session, request,render_template,url_for
from flask_bootstrap import Bootstrap
from flask import Blueprint
import json
import time

bsubmit=Blueprint('bsubmit', __name__)

@bsubmit.route('/submit/answering',methods=['GET','POST'])
def test():
    thistime=int(time.time())
    data=request.get_json()
    question=models.question.query.filter_by(id=data['qid']).first()
    sql='select *  from answer order by id desc limit 1'
    maxid = db.session.execute(sql).first()
    print(maxid)
    maxid=int(maxid['id'])+1
    answer=models.answer()
    answer.id=maxid
    answer.qid=question.id
    answer.uid=1
    answer.time=thistime
    answer.queTitle=question.question
    answer.topicid=question.reltopicid
    answer.like=0
    answer.answer=0
    answer.comCount=0
    answer.picture=0
    answer.score=0
    answer.delete=0
    db.session.add(answer)
    db.session.commit()
    with open("C://Users//梅西//Desktop//forserver//answer//"+str(maxid)+".txt", "w+") as f:
        f.write(data['anscontent'])
    print(data['anscontent'])
    print(data['qid'])
    return json.dumps({'msg':True,'id':'1'})

@bsubmit.route('/submit/topicstar',methods=['GET','POST'])
def topicstar():
    data=request.get_json()
    topicid=data["topicid"]
    uid=session["uid"]
    intable=models.topicStar.query.filter_by(uid=uid,topicid=topicid).first()
    if intable:
        return json.dumps({'msg':'already in'})
    else:
        topic=models.topic.query.filter_by(id=topicid).first()
        sql='select *  from topicstar order by id desc limit 1'
        maxid = db.session.execute(sql).first()
        print(maxid)
        maxid=int(maxid['id'])+1
        topicstar=models.topicStar()
        topicstar.id=maxid
        topicstar.uid=uid
        topicstar.topicid=topicid
        topicstar.topic=topic.topic
        db.session.add(topicstar)
        db.session.commit()
        print('chenggong')
        return json.dumps({'msg':True,'id':'1'})


