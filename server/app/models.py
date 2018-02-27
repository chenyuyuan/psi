from app import db

class plan(db.Model):
    __tablename__ = 'plan'
    id = db.Column(primary_key=True)
    name = db.Column()
    key = db.Column()
    date = db.Column()
    wechat = db.Column()
    activity_one = db.Column()
    activity_two = db.Column()
    activity_three = db.Column()
    activity_four = db.Column()
    activity_five = db.Column()
    activity_six = db.Column()
    hotel = db.Column()
    restaurant_one = db.Column()
    restaurant_two = db.Column()
    restaurant_three = db.Column()
    restaurant_four = db.Column()

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