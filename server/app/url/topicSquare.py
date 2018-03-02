from flask import Flask, session, request

from app import db, models,app
from flask_restful import Resource, Api, reqparse, abort
from flask import Flask, session, request,render_template,url_for
import flask
from flask_bootstrap import Bootstrap
from flask import Blueprint


btopicSquare=Blueprint('btopicSquare', __name__)

@btopicSquare.route('/topicSquare')
def test():
    alltopic = models.topic.query.all()
    sql='select * from topicstar where uid=1'
    mystartopic = list()
    mystartopic = db.session.execute(sql)
    uid=session['uid']
    # for key in mystartopic:
    #     print(key.topic)
    for key in alltopic:
        print(key.topic+':'+key.topicIntro)
    return render_template('/topicSquare.html', title='首页首页首页',mystartopic=mystartopic)
