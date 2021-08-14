# coding: utf-8

from __future__ import absolute_import
from datetime import datetime  # noqa: F401

from swagger_server.config import db


class GroupModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    timestamp = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )

    def __repr__(self):
        return '<Group %r>' % self.name
