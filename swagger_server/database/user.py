# coding: utf-8

from __future__ import absolute_import
from swagger_server.config import db
from swagger_server.models import user


friends = db.Table('friends',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('friend_id', db.Integer, db.ForeignKey('user.id'), primary_key=True)
)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    password = db.Column(db.String(100))
    email = db.Column(db.String(32))
    photo_url = db.Column(db.String(255))
    status = db.Column(db.String(32))
    friends = db.relationship('User',
                           secondary=friends,
                           primaryjoin=id==friends.c.user_id,
                           secondaryjoin=id==friends.c.friend_id)

    def befriend(self, friend):
        if friend not in self.friends:
            self.friends.append(friend)
            friend.friends.append(self)

    def unfriend(self, friend):
        if friend in self.friends:
            self.friends.remove(friend)
            friend.friends.remove(self)

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
    
    def get_friends(self, id):
        user = User.query.get(id)
        friends = []
        for friend in user.friends:
            friends.append(self.data_to_model(friend))
        return friends

    def add_friend(self, user, friend_id):
        logged_in_user = User.query.get(user)
        friend = User.query.get(friend_id)
        logged_in_user.befriend(friend)
        db.session.commit()

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
