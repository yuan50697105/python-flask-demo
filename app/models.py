from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), unique=True)
    pwd = db.Column(db.String(255))

    def __init__(self, id=None, name=None, pwd=None):
        self.id = id
        self.name = name
        self.pwd = pwd

    def __repr__(self):
        return "user:id=%s,name=%s,pwd=%s" % (self.id,self.name,self.pwd)