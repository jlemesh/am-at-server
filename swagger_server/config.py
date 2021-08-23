import os
import connexion
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))
app = connexion.App(__name__, specification_dir='./swagger/')

connex_app = app.app
sqlite_url = "sqlite:///" + os.path.join(basedir, "swagger.db")

connex_app.config["SQLALCHEMY_ECHO"] = True
connex_app.config["SQLALCHEMY_DATABASE_URI"] = sqlite_url
connex_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(connex_app)

db.create_all()
