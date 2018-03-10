from flask import Flask, session, request
import time,datetime
from app import db, models,app
from flask import Flask, session, request,render_template,url_for
from flask import Blueprint
import json
import time

btopic=Blueprint('btopic', __name__)

@btopic.route('/topic/<topicid>/hotanswer')
def test(topicid):
    answercontent = []
    thistopic = models.topic.query.filter_by(id=topicid).first()
    sql = "select *  from answer where topicid="+topicid
    answer = list()
    answered=[]
    answer = db.session.execute(sql)
    uid =session['uid']
    user=models.user.query.filter_by(id=uid).first()
    username=user.account
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
    answered=answered[::-1]
    # for i in range(0,len(answered)):
    #     print(answered[i]['id'])
    # for key in answered:
    #     print(key['uid'])
    for key in answered:
        with open("C://Users//梅西//Desktop//forserver//answer//"+str(key['id'])+".txt","r+") as f:
            h=f.read()
        answered[count]["content"]=h
        count=count+1
    topicstar = models.topicStar.query.filter_by(uid=uid,topicid=topicid).first()
    thisstar=False
    if topicstar:
        thisstar=True
    print(thisstar)
    print(str(uid)+"+"+str(topicid))
    return render_template('/topic.html', title='话题',thisstar=thisstar,username=username,uid=uid,users=users,topicid=topicid,thistopic=thistopic,answered=answered,answercontent=answercontent)

@btopic.route('/topic/<topicid>/question',methods=['GET','POST'])
def topicquestion(topicid):
    answercontent = []
    thistopic = models.topic.query.filter_by(id=topicid).first()
    sql = "select *  from question where reltopicid="+topicid
    answer = list()
    question=[]
    question0 = db.session.execute(sql)
    uid =session['uid']
    user=models.user.query.filter_by(id=uid).first()
    username=user.account
    users=models.user.query.all()
    count=0
    for key in question0:
        question.append({
            "id": key.id,
            "question": key.question,
            "like": key.like,
            "ansCount": key.ansCount,
            "uid": key.uid,
            "time": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(key.time)),
            "score": key.score,
            "watch":key.watch,
            "reltopicid": key.reltopicid,
            "followerCount":key.followerCount,
            "queContent":key.queContent,
            "delete": key.delete
        })

    print(question)
    question=question[::-1]
    topicstar = models.topicStar.query.filter_by(uid=uid,topicid=topicid).first()
    thisstar=False
    if topicstar:
        thisstar=True
    print(thisstar)
    print(str(uid)+"+"+str(topicid))
    return render_template('/topicquestion.html',title='话题',thisstar=thisstar,username=username,uid=uid,users=users,topicid=topicid,thistopic=thistopic,question=question)

@btopic.route('/topic/star',methods=['GET','POST'])
def staringtopic():
    req=request.get_json()
    flag=req["flag"]
    topicid=int(req["topicid"])
    #flag=1进行关注话题
    topictitle=models.topic.query.filter_by(id=topicid).first()
    title=topictitle.topic
    print(title)
    alltopicstar=models.topicStar.query.all()
    maxid=alltopicstar[len(alltopicstar)-1].id+1
    uid=session['uid']
    if flag=='1':
        topicstar=models.topicStar()
        topicstar.id=maxid
        topicstar.uid=uid
        topicstar.topicid=topicid
        topicstar.topic=title
        db.session.add(topicstar)
        db.session.commit()
        thistopic=models.topic.query.filter_by(id=topicid).first()
        thistopic.starCount=thistopic.starCount+1
        db.session.commit()
        return json.dumps({"msg":"starok"})
    elif flag=="0":
        thistopic=models.topic.query.filter_by(id=topicid).first()
        thistopic.starCount=thistopic.starCount-1
        topicstar=models.topicStar.query.filter_by(uid=uid,topicid=topicid).first()
        if topicstar:
            topicstar.uid = 0
        db.session.commit()
        return json.dumps({"msg":"cancelok"})
@btopic.route('/answer/star', methods=['GET', 'POST'])
def answerstar():
    req=request.get_json()
    ansid=req["ansid"]
    uid=session["uid"]
    ansstarall=models.ansStar.query.all()
    maxid=ansstarall[len(ansstarall)-1].id+1
    ansstar=models.ansStar()
    ansstar.id=maxid
    ansstar.uid=uid
    ansstar.ansid=ansid
    db.session.add(ansstar)
    db.session.commit()
    return json.dumps({"msg":"ok"})


