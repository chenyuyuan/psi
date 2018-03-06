from app import db, models
from flask_restful import Resource, Api, reqparse, abort
from flask import Flask, session, request,render_template,url_for
from flask_bootstrap import Bootstrap
from app import app
from flask import Blueprint


blogin=Blueprint('blogin', __name__)

bootstrap=Bootstrap(app)
app.secret_key = '~\xc8\xc6\xe0\xf3,\x98O\xa8z4\xfb=\rNd'

@blogin.route('/login')
def login():
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

@blogin.route('/logout')
def logout():
    if 'uid' in session:
        session.pop('uid')
    if '_login' in session:
        session.pop('_login')
        return '<h1>logout succeed</h1>'
    return '<h1>logout failed<h1>'

@blogin.route('/test_login')
def test_login():
    if 'uid' in session:
        return '<h1>you are still in</h1>'
    else:
        return '<h1>you have logouted</h1>'

@blogin.route('/who')
def who():
    if session['uid']:
        return session['uid']
    else:
        return '<h1>you are no login!</h1>'

@blogin.route('/bootstrap')
def bootstrap(Resource):
    title='Bootstrap'
    return render_template('/main.html',title=title)