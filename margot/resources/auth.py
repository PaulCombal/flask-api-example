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
        
        seconds_in_7_days = 7 * 24 * 60 * 60
        expires = datetime.timedelta(seconds=seconds_in_7_days)
        access_token = create_access_token(identity=str(user.id), expires_delta=expires)
        cookie = {'Set-Cookie': f'token={access_token}; expires={seconds_in_7_days}; HttpOnly' }
        return {'message': 'ok'}, 200, cookie