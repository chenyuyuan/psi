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
    question=models.question.query.filter_by(id=data.qid).first()
    answer=models.answer()
    # print(data['anscontent'])
    # print(data['qid'])
    return json.dumps({'msg':True,'id':'1'})