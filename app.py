from flask import Flask
from routes.site import site
from routes.mensajes import mensajes
from database.db import db
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)



app.config.from_object("config.BaseConfig")

SQLAlchemy(app)


app.register_blueprint(site)
app.register_blueprint(mensajes)