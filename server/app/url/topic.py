from flask import Flask, session, request
import time,datetime
from app import db, models,app
from flask_restful import Resource, Api, reqparse, abort
from flask import Flask, session, request,render_template,url_for
from flask_bootstrap import Bootstrap
from flask import Blueprint


btopic=Blueprint('btopic', __name__)

@btopic.route('/topic/<topicid>/hotanswer')
def test(topicid):
    answercontent = []
    thistopic = models.topic.query.filter_by(id=topicid).first()
    sql = "select *  from answer where topicid=1"
    answer = list()
    answered=[]
    answer = db.session.execute(sql)
    # uid = session['uid']
    # user=models.user.query.filter_by(id=uid).first()
    users=models.user.query.all()
    count=0
    for key in answer:
        for k in users:
            if k.id==key.uid:
                answered.append({
                    "id":key.id,
                    "qid":key.qid,
                    "like":key.like,
                    "comCount":key.comCount,
                    "uid":key.uid,
                    "account":k.account,
                    "shortIntro":k.shortIntro,
                    "time":time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(key.time)),
                    "score":key.score,
                    "queTitle":key.queTitle,
                    "topicid":key.topicid,
                    "delete":key.delete
                })
                break
    print(answered)
    for i in range(0,len(answered)):
        print(answered[i]['id'])
    for key in answered:
        print(key['uid'])
    for key in answered:
        with open("C://Users//梅西//Desktop//forserver//answer//"+str(key['id'])+".txt","r+") as f:
            h=f.read()
        answered[count]["content"]=h
        count=count+1
    # for key in answercontent:
    #      print('qq'+key+'\n')
    return render_template('/topic.html', title='话题',users=users,topicid=topicid,thistopic=thistopic,answered=answered,answercontent=answercontent)
