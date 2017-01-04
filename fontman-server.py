""" fontman server

User management, channel management, cache database

Created by Lahiru Pathirage <lpsandaruwan@gmail.com> on 18/12/16
"""

from flask import Flask
from flask_cors import CORS

from blueprint import auth_blueprint
from session import application_root
from utility import initialize

app = Flask(__name__)
app.config["APPLICATION_ROOT"] = application_root
app.register_blueprint(auth_blueprint)

CORS(app, resources=r'/api/*', headers='Content-Type')


if __name__ == '__main__':
    app.run(port=8080, threaded=True)
    # initialize()
