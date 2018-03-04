from flask import Flask, session, request
import time,datetime
from app import db, models,app
from flask_restful import Resource, Api, reqparse, abort
from flask import Flask, session, request,render_template,url_for
from flask_bootstrap import Bootstrap
from flask import Blueprint
import json


bsubmit=Blueprint('bsubmit', __name__)

@bsubmit.route('/submit',methods=['GET','POST'])
def test():
    data=request.get_json()
    print(data['questionid'])
    return json.dumps({'msg':True,'id':'1'})


