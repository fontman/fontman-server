""" Team service

High level functions to manipulate teams table.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 4/1/2017
"""

from model import Team
from session import DBSession


class TeamService:
    
    def __init__(self):
        self.__db_session = DBSession()

    def add_new(self, name, type):
        new_team = Team(name=name, type=type)

        self.__db_session.add(new_team)
        self.__db_session.commit()

        return new_team

    def delete_by_team_id(self, team_id):
        self.find_by_team_id(team_id).delete()
        self.__db_session.commit()

    def find_all(self):
        return self.__db_session.query(Team.team_id)

    def find_by_team_id(self, team_id):
        self.__db_session.query(Team).filter_by(team_id=team_id)

    def find_by_type(self, type):
        return self.__db_session.query(Team).filter_by(type=type)

    def update_by_team_id(self, team_id, update_data):
        self.find_by_team_id(team_id).update(update_data)
        self.__db_session.commit()
