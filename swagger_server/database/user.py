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
        user_objects = User.query.all()
        users = []

        for user_object in user_objects:
            users.append(
                self.data_to_model(user_object)
            )

        return users

    def get_user(self, id):
        user_object = User.query.get(id)

        return self.data_to_model(user_object)

    def create_user(self, model):
        user = self.model_to_data(model)
        db.session.add(user)
        db.session.commit()

        return self.data_to_model(user)
    
    def update_user(self, id, model):
        user = User.query.get(id)
        if model.name:
            user.name = model.name
        if model.email:
            user.email = model.email
        if model.status:
            user.status = model.status
        if model.photo_url:
            user.photo_url = model.photo_url
        db.session.commit()

        return self.data_to_model(user)

    def data_to_model(self, data):
        return user.User(
            id=data.id,
            name=data.name,
            email=data.email,
            photo_url=data.photo_url,
            status=data.status
        )

    def model_to_data(self, model):
        return User(
            name=model.name,
            email=model.email,
            photo_url=model.photo_url,
            status=model.status
        )
