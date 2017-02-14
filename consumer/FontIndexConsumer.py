""" Consumer package

Contains link generations and API consuming functions for GitHub API

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 31/12/2016
"""

import requests
from flask import json


class FontIndexConsumer:

    def __init__(self):
        self.__font_index = "https://raw.githubusercontent.com/" \
                            "fontman/font-index/master/index.json"

    def load_font_index(self):
        return json.loads(requests.get(self.__font_index).text)
