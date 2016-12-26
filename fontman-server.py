""" fontman server

User management, channel management, cache database

Created by Lahiru Pathirage <lpsandaruwan@gmail.com> on 18/12/16
"""

from flask import Flask
from flask_cors import CORS, cross_origin
import os

from blueprint import channel_blueprint
from blueprint import font_blueprint
from blueprint import language_blueprint
from blueprint import user_blueprint

from utility import Initialize

app = Flask(__name__)
app.register_blueprint(channel_blueprint)
app.register_blueprint(font_blueprint)
app.register_blueprint(language_blueprint)
app.register_blueprint(user_blueprint)

CORS(app, resources=r'/api/*', headers='Content-Type')

if __name__ == '__main__':
    app.run(port=8080, threaded=True)
    # Initialize()
