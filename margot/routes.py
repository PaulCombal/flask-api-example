from flask_restful import Api
from margot.resources.auth import LoginApi, SignupApi
from margot.resources.hospital import HospitalApi


def initialize_routes(api : Api):
    api.add_resource(SignupApi, '/api/auth/signup')
    api.add_resource(LoginApi, '/api/auth/login')

    api.add_resource(HospitalApi, '/api/hospital/<int:id>', '/api/hospital')