# from app import db, models
# from flask_restful import Resource, Api, reqparse, abort
# from flask import Flask, session, request,render_template,url_for
# import flask
# from flask_bootstrap import Bootstrap
#
# app = Flask(__name__)
# bootstrap=Bootstrap(app)
# @app.route('/main')
# def test():
#     title="appache"
#     return render_template('/main.html',title=title)

from flask import Flask, session, request

from app import db, models,app
from flask_restful import Resource, Api, reqparse, abort
from flask import Flask, session, request,render_template,url_for
import flask
from flask_bootstrap import Bootstrap
from flask import Blueprint


bo=Blueprint('bo', __name__)


bootstrap=Bootstrap(app)
@bo.route('/ma')
def test():
    plan = models.user.query.filter_by(id='1').first()
    title="appache"
    print(plan.password)
    return render_template('/main.html', title=title)
