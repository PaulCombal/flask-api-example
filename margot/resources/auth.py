from flask import request
import sqlalchemy
from margot.database.models import User
from margot.database.db import db
from flask_restful import Resource
from flask_jwt_extended import create_access_token
import datetime

class SignupApi(Resource):
    def post(self):
        body = request.get_json()
        user = User(**body)
        user.hash_password()

        try:
            db.session.add(user)
            db.session.commit()
            id = user.id
            return {'id': id}, 200
        except sqlalchemy.exc.IntegrityError as e:
            return {'message': 'username_unavailable'}, 409

class LoginApi(Resource):
    def post(self):
        body = request.get_json()
        user = User.query.filter_by(username=body.get('username')).first()
        if user is None:
            return {'error': 'invalid_credentials'}, 401
        
        authorized = user.check_password(body.get('password'))
        if not authorized:
            return {'error': 'invalid_credentials'}, 401
        
        expires = datetime.timedelta(days=7)
        access_token = create_access_token(identity=str(user.id), expires_delta=expires)
        return {'token': access_token}, 200