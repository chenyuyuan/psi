from app import db

class user(db.Model):
    __tablename__='user'
    id=db.Column(primary_key=True)
    account=db.Column()
    password=db.Column()
    grade=db.Column()
    shortIntro=db.Column()
    head=db.Column()
class follow(db.Model):
    __tablename__='follow'
    id=db.Column(primary_key=True)
    uid=db.Column()
    fid=db.Column()