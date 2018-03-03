from app import app

from app.url.bootstrap import bo
from app.url.upload import upload
from app.url.login import blogin
from app.url.topicSquare import btopicSquare
from app.url.topic import btopic

app.register_blueprint(btopicSquare)
app.register_blueprint(blogin)
app.register_blueprint(upload)
app.register_blueprint(bo,url_prefix='/bb')
app.register_blueprint(btopic)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=3000)
