from app import db

class user(db.Model):
    __tablename__='user'
    id=db.Column(primary_key=True)
    account=db.Column()
    password=db.Column()
    grade=db.Column()
    shortIntro=db.Column()
    head=db.Column()
    follow=db.Column()
    follower=db.Column()
    major=db.Column()
    time=db.Column()
    sex=db.Column()
    likeCount=db.Column()
    starCount=db.Column()

class question(db.Model):
    __tablename__='question'
    id = db.Column(primary_key=True)
    question=db.Column()
    like=db.Column()
    ansCount=db.Column()
    uid=db.Column()
    picture=db.Column()
    time=db.Column()
    watch=db.Column()
    reltopicid=db.Column()
    followerCount=db.Column()
    score=db.Column()
    ansCount=db.Column()
    delete=db.Column()

class answer(db.Model):
    __tablename__='answer'
    id=db.Column(primary_key=True)
    qid=db.Column()
    like=db.Column()
    answer=db.Column()
    comCount=db.Column()
    uid=db.Column()
    picture=db.Column()
    time=db.Column()
    score=db.Column()
    queTitle=db.Column()
    topicid=db.Column()
    delete=db.Column()

class userAdmin(db.Model):
    __tablename__='useradmin'
    id=db.Column(primary_key=True)
    account=db.Column()
    password=db.Column()
    time=db.Column()
    head=db.Column()

class queStar(db.Model):
    __tablename__='questar'
    id=db.Column(primary_key=True)
    uid=db.Column()
    queid=db.Column()

class ansStar(db.Model):
    __tablename__='ansstar'
    id=db.Column(primary_key=True)
    uid=db.Column()
    ansid=db.Column()

class artStar(db.Model):
    __tablename__='artstar'
    id=db.Column(primary_key=True)
    uid=db.Column()
    artid=db.Column()

class follow(db.Model):
    __tablename__='follow'
    id=db.Column(primary_key=True)
    uid=db.Column()
    fid=db.Column()

class topicStar(db.Model):
    __tablename__='topicstar'
    id=db.Column(primary_key=True)
    uid=db.Column()
    topicid=db.Column()
    topic=db.Column()

class topic(db.Model):
    __tablename__='topic'
    id=db.Column(primary_key=True)
    topic=db.Column()
    starCount=db.Column()
    time=db.Column()
    topicIntro=db.Column()
    queCount=db.Column()
    picture=db.Column()

class message(db.Model):
    __tablename__='message'
    id=db.Column(primary_key=True)
    uid=db.Column()
    fid=db.Column()
    content=db.Column()
    time=db.Column()
    type=db.Column()
    delete=db.Column()

class article(db.Model):
    __tablename__='article'
    id=db.Column(primary_key=True)
    title=db.Column()
    address=db.Column()
    uid=db.Column()
    comCount=db.Column()
    like=db.Column()
    watch=db.Column()
    time=db.Column()
    topic=db.Column()
    delete=db.Column()

class queComment(db.Model):
    __tablename__='quecomment'
    id=db.Column(primary_key=True)
    uid=db.Column()
    fid=db.Column()
    like=db.Column()
    pid=db.Column()
    content=db.Column()
    time=db.Column()
    queid=db.Column()
    delete=db.Column()

class ansComment(db.Model):
    __tablename__='anscomment'
    id=db.Column(primary_key=True)
    uid=db.Column()
    fid=db.Column()
    like=db.Column()
    pid=db.Column()
    content=db.Column()
    time=db.Column()
    ansid=db.Column()
    delete=db.Column()

class artComment(db.Model):
    __tablename__='artcomment'
    id=db.Column(primary_key=True)
    uid=db.Column()
    fid=db.Column()
    like=db.Column()
    pid=db.Column()
    content=db.Column()
    time=db.Column()
    artid=db.Column()
    delete=db.Column()

class tempTopic(db.Model):
    __tablename__='temptopic'
    id=db.Column(primary_key=True)
    uid=db.Column()
    topic=db.Column()
    topicIntro=db.Column()
    support=db.Column()
    time=db.Column()

class hotTopic(db.Model):
    __tablename__='hottopic'
    id=db.Column(primary_key=True)
    topic=db.Column()
    picture=db.Column()
    starCount=db.Column()
    time=db.Column()
    topicIntro=db.Column()






































































