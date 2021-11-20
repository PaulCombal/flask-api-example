from margot.database.models import Hospital
from flask import Response, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource

# Placeholder!
# TODO implement & check for roles

class HospitalApi(Resource):
    @jwt_required
    def put(self, id):
        user_id = get_jwt_identity()
        body = request.get_json()
        Hospital.query.filter_by(id=id).update(**body)
        return '', 200
    
    @jwt_required
    def delete(self, id):
        user_id = get_jwt_identity()
        hospital = Hospital.objects.get(id=id)
        hospital.delete()
        return '', 200

    @jwt_required
    def get(self, id):
        hospital = Hospital.query.get(id)
        return hospital