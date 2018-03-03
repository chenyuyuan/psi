from flask import Flask, session, request

from app import db, models,app
from flask_restful import Resource, Api, reqparse, abort
from flask import Flask, session, request,render_template,url_for
from flask_bootstrap import Bootstrap
from flask import Blueprint


btopic=Blueprint('btopic', __name__)

@btopic.route('/topic/<topicid>/<style>')
def test(topicid,style):
    thistopic = models.topic.query.filter_by(id=topicid).first()
    sql = 'select * from question where reltopicid=1'
    answer = list()
    answer = db.session.execute(sql)
    uid = session['uid']
    with open("C://forserver//answer//1.txt","r+") as f:
        h=f.read()

    print(h)

    return render_template('/topic.html', title='话题',topicid=topicid,style=style,thistopic=thistopic,answer=answer)
