from app import app

from flask import Flask, session, request
app = Flask(__name__)
app.secret_key = '~\xc8\xc6\xe0\xf3,\x98O\xa8z4\xfb=\rNd'


@app.route('/login')
def login():
    uid =  request.args.get('uid')
    psw = request.args.get('psw')
    if uid and psw:
        session['uid'] = uid
        session['_login'] = True
        return '<h1>login succeed!</h1>'
    return '<h1>login failed</h1>'

@app.route('/logout')
def logout():
    if 'uid' in session:
        session.pop('uid')
    if '_login' in session:
        session.pop('_login')
        return '<h1>logout succeed</h1>'
    return '<h1>logout failed<h1>'


@app.route('/test_login')
def tst():
    if 'uid' in session:
        return '<h1>you are still in</h1>'
    else:
        return '<h1>you have logouted</h1>'

@app.route('/a')
def a():
    return '<h1>Goooooood</h1>'

@app.route('/who')
def who():
    return session['uid']


if __name__ == '__main__':
    app.run(host='0.0.0.0')
