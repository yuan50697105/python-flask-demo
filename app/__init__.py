from flask import Flask
from app.models import db
from app.admin import admin
from app.config import Config
from flask_bootstrap import Bootstrap

app = Flask(__name__)
# app.config.from_object(Config)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+mysqlconnector://root:root@localhost:3306/pymovie'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
app.config['DEBUG']=True
app.register_blueprint(admin, url_prefix="/admin")
from app.models import *

db.init_app(app=app)
app.app_context().push()
