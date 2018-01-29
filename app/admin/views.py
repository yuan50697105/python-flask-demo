from app.admin import admin
from flask import jsonify
from flask import Response
import app.models
import json
from app.models import db
from app.models import User


def getJson(new_user):
    data = []
    d = {'id': new_user.id, 'name': new_user.name, 'pwd': new_user.pwd}
    data.append(d)
    return data


def getJsonList(new_user=[]):
    data = []
    for user in new_user:
        data.append(getJson(user))
    return data


@admin.route("/")
def index():
    new_user = app.models.User(id=1, name='admin', pwd='123456')

    return jsonify(user=getJson(new_user))


@admin.route('/save')
def save():
    new_user = app.models.User(name='admin', pwd='123')
    result = db.session.add(new_user)
    db.session.commit()
    return jsonify(result)


@admin.route("/get/<int:id>")
def get(id):
    user = User.query.get(id)
    return jsonify(getJson(user))


@admin.route("/findall")
def findAll():
    users = User.query.all()
    return jsonify(getJsonList(users))
