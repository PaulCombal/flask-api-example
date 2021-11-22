from margot.database.models import Hospital, User
from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource

# Placeholder!
# TODO implement & check for roles

class HospitalApi(Resource):
    @jwt_required()
    def put(self, id):
        # user_id = get_jwt_identity()
        # user = User.query.get(user_id)
        # if not user.is_admin():
        #     return '', 401
        
        # body = request.get_json()
        # Hospital.query.filter_by(id=id).update(**body)
        return {'message': 'ok'}, 200
    
    @jwt_required()
    def delete(self, id):
        # user_id = get_jwt_identity()
        # hospital = Hospital.objects.get(id=id)
        # hospital.delete()
        return '', 200

    @jwt_required()
    def get(self, id):
        print("test" + str(id))
        hospital = Hospital.query.get(id)
        if hospital is None:
            return {'message': 'not_found'}, 404
        
        return {
            'id': hospital.id,
            'name': hospital.name,
            'address': hospital.address
        }