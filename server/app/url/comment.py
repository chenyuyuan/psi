from flask import Flask, session, request
import time,datetime
from app import db, models,app
from flask_restful import Resource, Api, reqparse, abort
from flask import Flask, session, request,render_template,url_for
from flask_bootstrap import Bootstrap
from flask import Blueprint
import json
import time

bcomment=Blueprint('bcomment', __name__)

@bcomment.route('/comment/answer',methods=['GET','POST'])
def answer():
    thistime=int(time.time())
    anscomment=models.ansComment.query.filter_by(ansid=11).all()
    print(anscomment[1].content)
    datas=[]
    for key in anscomment:
        datas.append({
            "id":key.id,
            "uid":key.uid,
            "fid":key.fid,
            "pid":key.pid,
            "like":key.like,
            "content":key.content,
            "time":key.time,
            "ansid":key.ansid
        })
    return json.dumps({"msg":"1","data":datas})
