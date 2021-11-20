from .db import db
from flask_bcrypt import generate_password_hash, check_password_hash

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80), unique=True, nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	password = db.Column(db.String(255), nullable=False)

	def hash_password(self):
		self.password = generate_password_hash(self.password).decode('utf8')
    
	def check_password(self, password):
		return check_password_hash(self.password, password)


	def __repr__(self):
		return '<User %r>' % self.username



class Hospital(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(80), nullable=False)
	address = db.Column(db.String(120))

	def __repr__(self):
		return '<Hospital %r>' % self.name