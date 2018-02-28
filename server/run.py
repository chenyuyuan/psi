from app import app


from app.url.bootstrap import bo
from app.url.upload import upload

app.register_blueprint(upload)
app.register_blueprint(bo,url_prefix='/bb')

if __name__ == '__main__':
    app.run(debug='True')
