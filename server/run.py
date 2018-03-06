from app import app

from app.url.upload import upload
from app.url.login import blogin
from app.url.topicSquare import btopicSquare
from app.url.topic import btopic
from app.url.question import bquestion
from app.url.submit import bsubmit
from app.url.home import bhome
from app.url.articling import barticling
from app.url.people import bpeople
from app.url.topicapplying import btopicapplying
from app.url.comment import bcomment

app.register_blueprint(btopicSquare)
app.register_blueprint(blogin)
app.register_blueprint(upload)
app.register_blueprint(btopic)
app.register_blueprint(bquestion)
app.register_blueprint(bsubmit)
app.register_blueprint(bhome)
app.register_blueprint(barticling)
app.register_blueprint(bpeople)
app.register_blueprint(btopicapplying)
app.register_blueprint(bcomment)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=3000)
