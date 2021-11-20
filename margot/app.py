from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from margot.database.db import initialize_db
from margot.routes import initialize_routes
import os

app = Flask(__name__)
app.config.from_pyfile(os.environ.get('ENV_FILE_NAME', '.env.dev'))
api = Api(app)
jwt = JWTManager(app)

initialize_db(app)
initialize_routes(api)

if __name__ == '__main__':
    app.run()