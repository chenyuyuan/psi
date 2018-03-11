from flask import Flask, session, request
import time,datetime
from app import db, models,app
from flask_restful import Resource, Api, reqparse, abort
from flask import Flask, session, request,render_template,url_for
from flask_bootstrap import Bootstrap
from flask import Blueprint


bhome=Blueprint('bhome', __name__)

@bhome.route('/home')
def home():
    title='home'
    return render_template('/home.html',title=title)
@bhome.route('/homeadmin')
def homeadmin():
    return render_template('/homeadmin.html')