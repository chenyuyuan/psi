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

@bsubmit.route('/submit',methods=['GET','POST'])
def test():
    thistime=int(time.time())
    data=request.get_json()
    question=models.question.query.filter_by(id=data['qid']).first()
    sql='select * from answer order by id desc limit 1'
    maxid = db.session.execute(sql)
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
    print(data['anscontent'])
    print(data['qid'])
    return json.dumps({'msg':True,'id':'1'})