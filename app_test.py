import unittest

from margot.app import app
from margot.database.models import User, Hospital
from margot.database.db import db

from flask_fixtures import FixturesMixin

# Configure the app with the testing configuration
app.config.from_object('margot.config.TestConfig')


# Make sure to inherit from the FixturesMixin class
class TestAll(unittest.TestCase, FixturesMixin):

    # SQLALCHEMY_DATABASE_URI = "sqlite://"
    TESTING = True


    # Specify the fixtures file(s) you want to load.
    fixtures = ['fixtures.json']

    # Specify the Flask app and db we want to use for this set of tests
    app = app
    db = db

    # Test user creation
    def test_users_creation(self):
        users = User.query.all()
        assert len(users) == User.query.count() == 2

    # Test user password hashing
    def test_users_pw_hashing(self):
        users = User.query.all()
        for user in users:
            user.hash_password()
            db.session.add(user)

        db.session.commit()
        assert User.query.filter_by(password='admin').first() is None

    

    def test_hospital_creation(self):
        hospitals = Hospital.query.all()
        assert len(hospitals) == Hospital.query.count() == 1




    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()