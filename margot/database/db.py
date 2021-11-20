from flask.app import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def initialize_db(app : Flask):
    db.init_app(app)

    if os.environ.get('FLASK_ENV') == 'development':
        with app.app_context():
            db.drop_all()
            db.create_all()