from flask import Flask, session, request
import time,datetime
from app import db, models,app
from flask_restful import Resource, Api, reqparse, abort
from flask import Flask, session, request,render_template,url_for,redirect
from flask_bootstrap import Bootstrap
from flask import Blueprint
import json,time


bpeople=Blueprint('bpeople', __name__)

@bpeople.route('/people/me/myask',methods=['GET','POST'])
def people():
    uid=session["uid"]
    users=models.user.query.all()
    user={}
    question=[]
    for key in users:
        if key.id==uid:
            user=key
    questions=models.question.query.all()
    for key in questions:
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
                "time":time.strftime("%m-%d %H:%M:%S", time.localtime(key.time)),
                "reltopicid":key.reltopicid,
                "followerCount":key.followerCount,
                "queContent":key.queContent
            })
    return render_template('/pageofmine/pageofmine.html', title='我的主页',mine="1",type="question", users=users,user=user,question=question)

@bpeople.route('/people/edit',methods=['GET','POST'])
def edit():

    return json.dumps({"msg":"good"})
@bpeople.route('/people/changepassword',methods=['GET','POST'])
def changepassword():
    req=request.get_json()
    password=req["password"]
    oldpassword=req["oldpassword"]
    uid=session["uid"]
    user=models.user.query.filter_by(id=uid).first()
    if oldpassword==user.password:
        user.password=password
        db.session.commit()
        return json.dumps({"msg":"good"})
    else:
        return json.dumps({"msg":"no"})
@bpeople.route('/people/editinfo',methods=['GET','POST'])
def editinfo():
    req=request.get_json()
    shortIntro=req["shortIntro"]
    major=req["major"]
    grade=req["grade"]
    uid=session["uid"]
    user=models.user.query.filter_by(id=uid).first()
    if user:
        user.shortIntro=shortIntro
        user.major=major
        user.grade=grade
        db.session.commit()
        return json.dumps({"msg":"good"})
    else:
        return json.dumps({"msg":"no"})

@bpeople.route('/people/<id>/ask')
def others(id):
    uid=int(id)
    users=models.user.query.all()
    user={}
    mine="0"
    myid=session["uid"]
    if uid==session["uid"]:
        mine="1"
    starhim="0"
    if models.follow.query.filter_by(uid=myid,fid=uid).first():
        starhim="1"
    question=[]
    print(uid)
    user=models.user.query.filter_by(id=uid).first()
    questions=models.question.query.all()
    print(questions[1].uid)
    for key in questions:
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
                "time":time.strftime("%m-%d %H:%M:%S", time.localtime(key.time)),
                "reltopicid":key.reltopicid,
                "followerCount":key.followerCount,
                "queContent":key.queContent
            })
    print(question)
    return render_template('/pageofmine/pageofmine.html', title='我的主页',starhim=starhim,fid=uid,mine="0",type="question", users=users,user=user,question=question)
@bpeople.route('/people/<id>/answer',methods=['GET','POST'])
def peopleanswer(id):
    uid=int(id)
    users=models.user.query.all()
    user={}
    myid = session["uid"]
    mine="0"
    if uid==session["uid"]:
        mine="1"
    starhim="0"
    if models.follow.query.filter_by(uid=myid,fid=uid).first():
        starhim="1"
    answer=[]
    print(uid)
    user=models.user.query.filter_by(id=uid).first()
    questions=models.answer.query.all()
    print(questions[1].uid)
    for key in questions:
        if key.uid==uid:
            flag="0"
            if models.ansLike.query.filter_by(uid=uid, ansid=key.id).first():
                print("查到")
                flag = "1"
            answer.append({
                "id":key.id,
                "qid":key.qid,
                "answer":key.answer,
                "comCount":key.comCount,
                "uid":key.uid,
                "like":key.like,
                "ilike":flag,
                "queTitle":key.queTitle,
                "topicid":key.topicid,
                "time":time.strftime("%m-%d %H:%M:%S", time.localtime(key.time)),
            })
            count=0
            for key in answer:
                with open("C://Users//梅西//Desktop//forserver//answer//" + str(key['id']) + ".txt", "r+") as f:
                    h = f.read()
                answer[count]["content"] = h
                count = count + 1
    return render_template('/pageofmine/pageofmineanswer.html', title='我的主页',mine=mine,starhim=starhim,fid=uid,type="question", users=users,user=user,answer=answer)
@bpeople.route('/people/<id>/answerstar',methods=['GET','POST'])
def peopleanswerstar(id):
    uid=int(id)
    users=models.user.query.all()
    user={}
    myid = session["uid"]
    mine="0"
    if uid==session["uid"]:
        mine="1"
    starhim="0"
    if models.follow.query.filter_by(uid=myid,fid=uid).first():
        starhim="1"
    answer=[]
    print(uid)
    user=models.user.query.filter_by(id=uid).first()
    answers=models.answer.query.all()
    for key in answers:
        if models.ansStar.query.filter_by(uid=uid, ansid=key.id).first():
            answer.append({
                "id":key.id,
                "qid":key.qid,
                "answer":key.answer,
                "comCount":key.comCount,
                "uid":key.uid,
                "like":key.like,
                "queTitle":key.queTitle,
                "topicid":key.topicid,
                "time":time.strftime("%m-%d %H:%M:%S", time.localtime(key.time)),
            })
    count=0
    for key in answer:
        with open("C://Users//梅西//Desktop//forserver//answer//" + str(key['id']) + ".txt", "r+") as f:
            h = f.read()
        answer[count]["content"] = h
        count = count + 1
    return render_template('/pageofmine/pageofmineanswerstar.html', title='我的主页',fid=uid,starhim=starhim,mine=mine,type="question", users=users,user=user,answer=answer)
@bpeople.route('/people/<id>/questionstar',methods=['GET','POST'])
def peoplequestionstar(id):
    uid=int(id)
    users=models.user.query.all()
    user={}
    myid = session["uid"]
    mine="0"
    if uid==session["uid"]:
        mine="1"
    starhim="0"
    if models.follow.query.filter_by(uid=myid,fid=uid).first():
        starhim="1"
    question=[]
    print(uid)
    user=models.user.query.filter_by(id=uid).first()
    questions=models.question.query.all()
    for key in questions:
        flag = "0"
        if models.queLike.query.filter_by(uid=uid, queid=key.id).first():
            print("查到")
            flag = "1"
        if models.queStar.query.filter_by(uid=uid, queid=key.id).first():
            question.append({
                "id": key.id,
                "question": key.question,
                "like": key.like,
                "ilike": flag,
                "ansCount": key.ansCount,
                "time": time.strftime("%m-%d %H:%M:%S", time.localtime(key.time)),
                "reltopicid": key.reltopicid,
                "followerCount": key.followerCount,
                "queContent": key.queContent
            })
    return render_template('/pageofmine/pageofminequestionstar.html', title='我的主页',fid=uid,starhim=starhim,mine=mine,type="question", users=users,user=user,question=question)
@bpeople.route('/people/<id>/comment',methods=['GET','POST'])
def peoplecomment(id):
    uid=int(id)
    users=models.user.query.all()
    user={}
    myid = session["uid"]
    mine="0"
    if uid==session["uid"]:
        mine="1"
    starhim="0"
    if models.follow.query.filter_by(uid=myid,fid=uid).first():
        starhim="1"
    comment=[]
    print(uid)
    user=models.user.query.filter_by(id=uid).first()
    comments=models.ansComment.query.all()
    questions=models.question.query.all()
    for key in comments:
        if key.uid==uid:
            ans=models.answer.query.filter_by(id=key.ansid).first()
            que=models.question.query.filter_by(id=ans.qid).first()
            comment.append({
                "id": key.id,
                "ansid":ans.id,
                "qid":que.id,
                "comcontent":key.content,
                "time":time.strftime("%m-%d %H:%M:%S", time.localtime(key.time)),
                "question":que.question,
                })
    count=0
    for key in comment:
        with open("C://Users//梅西//Desktop//forserver//answer//" + str(key['id']) + ".txt", "r+") as f:
            h = f.read()
        comment[count]["content"] = h
        count = count + 1
    return render_template('/pageofmine/pageofminecomment.html', title='我的主页',fid=uid,starhim=starhim,mine=mine,type="question", users=users,user=user,comment=comment)
@bpeople.route('/people/deletecomment',methods=['GET','POST'])
def deletecomment():
    pass
@bpeople.route('/people/follow',methods=['GET','POST'])
def peoplefollow():
    req=request.get_json()
    flag=req["flag"]
    fid=req["fid"]
    uid=session["uid"]
    if flag=="0":
        follow=models.follow()
        follows=models.follow.query.all()
        maxid=follows[len(follows)-1].id+1
        follow.id=maxid
        follow.uid=uid
        follow.fid=fid
        db.session.add(follow)
        db.session.commit()
        i=models.user.query.filter_by(id=uid).first()
        f=models.user.query.filter_by(id=fid).first()
        i.follow=i.follow+1
        f.follower=f.follower+1
        db.session.commit()
        return json.dumps({"msg":"good"})
    if flag=="1":
        follow=models.follow.query.filter_by(uid=uid,fid=fid).first()
        if follow:
            follow.uid=0
        db.session.commit()
        i = models.user.query.filter_by(id=uid).first()
        f = models.user.query.filter_by(id=fid).first()
        i.follow = i.follow - 1
        f.follower = f.follower - 1
        db.session.commit()
        return json.dumps({"msg":"good"})

@bpeople.route('/people/send', methods=['GET', 'POST'])
def peoplesend():
    thistime=int(time.time())
    req=request.get_json()
    msg=req["msg"]
    uid=session["uid"]
    fid=session["uid"]
    message=models.message()
    messages=models.message.query.all()
    maxid=messages[len(messages)-1].id+1
    message.id=maxid
    message.uid=uid
    message.fid=fid
    message.content=msg
    message.time=thistime
    message.type=0
    message.delete=0
    db.session.add(message)
    db.session.commit()
    return json.dumps({"msg":"good"})