# coding: utf-8

from __future__ import absolute_import
from swagger_server.config import db
from swagger_server.models import user


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    email = db.Column(db.String(32))
    photo_url = db.Column(db.String(32))
    status = db.Column(db.String(32))

    def __repr__(self):
        return '<User %r>' % self.name


class UserDataProvider:
    def get_users(self):
        user_objets = User.query.all()
        data = []

        for user_object in user_objets:
            data.append(
                user.User(
                    id=user_object.id,
                    name=user_object.name,
                    email=user_object.email,
                    photo_url=user_object.photo_url,
                    status=user_object.status
                )
            )

        return data
    
    def get_user(self, id):
        user_object = User.query.get(id)

        return user.User(
            id=user_object.id,
            name=user_object.name,
            email=user_object.email,
            photo_url=user_object.photo_url,
            status=user_object.status
        )
