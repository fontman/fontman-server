""" Consumer package

Contains link generations and API consuming functions for GitHub API

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 31/12/2016
"""

import requests


class GitHubConsumer:

    def __init__(self, branch, repository, user):
        self.__branch = branch
        self.__repository = repository
        self.__user = user

    def get_cdn_link(self, file_path):
        return "https://cdn.rawgit.com/"\
               + self.__user + "/"\
               + self.__repository + "/"\
               + self.__branch + "/"\
               + file_path

    def get_latest_release_info(self):
        return requests.get(
            "https://api.github.com/repos/"
            + self.__user + '/'
            + self.__repository + '/'
            + 'releases/latest'
        ).json()

    def get_release_info_url(self, rel_id):
        return "https://api.github.com/repos/"\
               + self.__user \
               + self.__repository + '/releases/'\
               + str(rel_id)

    def get_tags_url(self):
        return "https://api.github.com/repos/"\
               + self.__user\
               + self.__repository + '/releases'

    def list_contents(self, location=""):
        return requests.get(
            "https://api.github.com/repos/"
            + self.__user + "/"
            + self.__repository + "/contents/"
            + location + "?ref="
            + self.__branch
        ).json()

    def list_tags(self):
        return requests.get(
            "https://api.github.com/repos/"
            + self.__user
            + self.__repository + '/tags'
        ).json()
