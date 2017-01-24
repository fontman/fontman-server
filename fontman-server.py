""" fontman server

User management, channel management, cache database

Created by Lahiru Pathirage <lpsandaruwan@gmail.com> on 18/12/16
"""

import sys
from flask import Flask
from flask_cors import CORS

from blueprint import auth_blueprint
from blueprint import channels_blueprint
from blueprint import collections_blueprint
from blueprint import fontfaces_blueprint
from blueprint import fonts_blueprint
from blueprint import ratings_blueprint
from blueprint import roles_blueprint
from blueprint import teams_blueprint
from blueprint import users_blueprint
from session import application_root

from utility import initialize

app = Flask(__name__)

app.register_blueprint(auth_blueprint, url_prefix=application_root)
app.register_blueprint(channels_blueprint, url_prefix=application_root)
app.register_blueprint(collections_blueprint, url_prefix=application_root)
app.register_blueprint(fontfaces_blueprint, url_prefix=application_root)
app.register_blueprint(fonts_blueprint, url_prefix=application_root)
app.register_blueprint(ratings_blueprint, url_prefix=application_root)
app.register_blueprint(roles_blueprint, url_prefix=application_root)
app.register_blueprint(teams_blueprint, url_prefix=application_root)
app.register_blueprint(users_blueprint, url_prefix=application_root)

app.register_blueprint(auth_blueprint)

CORS(app, resources=r'/api/*', headers='Content-Type')


def main(argv):
    if "init" in argv:
        initialize()

    if "run" in argv:
        app.run(host='0.0.0.0', port=8080, threaded=True)


if __name__ == '__main__':
    main(sys.argv[1:])
