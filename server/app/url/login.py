from app import db, models
from flask_restful import Resource, Api, reqparse, abort
from flask import Flask, session, request,render_template,redirect,url_for
from flask_bootstrap import Bootstrap
from app import app
from flask import Blueprint
import json
import time

blogin=Blueprint('blogin', __name__)

bootstrap=Bootstrap(app)
app.secret_key = '~\xc8\xc6\xe0\xf3,\x98O\xa8z4\xfb=\rNd'

@blogin.route('/logingin',methods=['GET','POST'])
def logingin():
    req=request.get_json()
    account=req["account"]
    password=req["password"]
    users=models.user.query.all()
    uid=''
    for key in users:
        if key.account==account:
            if key.password==password:
                uid=key.id
                session['uid']=uid
                session['_login']=True
                return json.dumps({"msg":"canlogin"})
            else:
                return json.dumps({"msg":"wrongpassword"})
    return json.dumps({"msg":"nosuchaccount"})
@blogin.route('/registering',methods=['GET','POST'])
def registering():
    thistime = int(time.time())
    req=request.get_json()
    account=req["account"]
    password=req["password"]
    users=models.user.query.all()
    maxid = users[len(users) - 1].id
    maxid = maxid + 1
    for key in users:
        if key.account==account:
            return json.dumps({"msg":"accountexisting"})
    user=models.user()
    user.id=maxid
    user.account=account
    user.password=password
    user.grade=''
    user.shortIntro=''
    user.head=''
    user.follow=0
    user.follower=0
    user.major=''
    user.time=thistime
    user.sex=''
    user.likeCount=0
    user.starCount=0
    db.session.add(user)
    db.session.commit()
    return json.dumps({"msg":"registered"})
@blogin.route('/login',methods=['GET','POST'])
def login():
    return render_template('login.html')
@blogin.route('/register',methods=['GET','POST'])
def register():

    return render_template('register.html')
@blogin.route('/logout',methods=['GET','POST'])
def logout():
    if 'uid' in session:
        session.pop('uid')
    if '_login' in session:
        session.pop('_login')
        return render_template('login.html')
    return redirect(url_for('bhome.home'))


@blogin.route('/signin')
def signin():
    uid = request.args.get('uid')
    psw = request.args.get('psw')
    if uid and psw:
        session['uid'] = uid
        session['_login'] = True
        return '<h1>login succeed!</h1><a href="http://127.0.0.1:3000/topicSquare">话题广场</a><br/>' \
               '<a href="http://127.0.0.1:3000/topic/1/hotanswer">话题</a><br/>' \
               '<a href="http://127.0.0.1:3000/question/1/hotanswer">问题</a><br/>' \
               '<a href="http://127.0.0.1:3000/home">主页</a><br/>' \
               '<a href="http://127.0.0.1:3000/articling">写文章</a><br/>' \
               '<a href="http://127.0.0.1:3000/people">我的主页</a><br/>'
    return '<h1>login failed</h1>'

@blogin.route('/signout')
def signout():
    if 'uid' in session:
        session.pop('uid')
    if '_login' in session:
        session.pop('_login')
        return '<h1>logout succeed</h1>'
    return '<h1>logout failed<h1>'

@blogin.route('/test/test_login')
def test_login():
    if 'uid' in session:
        return '<h1>you are still in</h1>'
    else:
        return '<h1>you have logouted</h1>'

@blogin.route('/test/who')
def who():
    if session['uid']:
        return session['uid']
    else:
        return '<h1>you are no login!</h1>'

@blogin.route('/test/bootstrap')
def bootstrap(Resource):
    title='Bootstrap'
    return render_template('/main.html',title=title)