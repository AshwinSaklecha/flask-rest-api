import os
from flask import Flask

app = Flask(__name__)

# Use PostgreSQL in production (Render), SQLite in development
if os.environ.get('RENDER'):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('DATABASE_URL')
else:
    project_dir = os.path.dirname(os.path.abspath(__file__))
    database_file = "sqlite:///{}".format(os.path.join(project_dir, "db/flask-api.db"))
    app.config["SQLALCHEMY_DATABASE_URI"] = database_file

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

from app.module.controller import *