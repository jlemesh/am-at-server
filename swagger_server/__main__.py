#!/usr/bin/env python3

import connexion
import os

from flask_sqlalchemy import SQLAlchemy
from swagger_server.config import app, db
from swagger_server import encoder


class Application:
    def __init__(self):
        basedir = os.path.abspath(os.path.dirname(__file__))
        self.app = connexion.App(__name__, specification_dir='./swagger/')

        self.app.app.json_encoder = encoder.JSONEncoder
        self.app.add_api('swagger.yaml', arguments={'title': 'Simple Am@ API'}, pythonic_params=True)

        connex_app = self.app.app
        sqlite_url = "sqlite:///" + os.path.join(basedir, "swagger.db")

        connex_app.config["SQLALCHEMY_ECHO"] = True
        connex_app.config["SQLALCHEMY_DATABASE_URI"] = sqlite_url
        connex_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

        self.db = SQLAlchemy(connex_app)

    def run(self):
        self.app.run(port=8080, debug=True)


if __name__ == '__main__':
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'Simple Am@ API'}, pythonic_params=True)
    app.run(port=8080, debug=True)
