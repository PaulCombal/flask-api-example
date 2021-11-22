#!/bin/env python

from margot.app import app
from margot.database.models import User
from margot.database.db import db

from flask_fixtures import FixturesMixin

with app.app_context():
    db.session.remove()
    db.drop_all()
    db.create_all()

