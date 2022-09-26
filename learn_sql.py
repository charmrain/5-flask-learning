from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlit:///' + '/Users/anrui/Desktop/database/test.db'
# the content after + is the location of db

