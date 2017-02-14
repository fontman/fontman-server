""" Users service

Provides high level functions to manipulate user database

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 18/12/2016
"""

from model import User
from session import DBSession

import uuid


class UserService:
    
    def __init__(self):
        self.__db_session = DBSession()

    def add_new(self, email, name, password):
        new_user = User(
            email=email,
            name=name,
            password=password,
            token = uuid.uuid4().hex
        )

        self.__db_session.add(new_user)
        self.__db_session.commit()

        return new_user

    def delete_by_email(self, email):
        self.find_by_email(email).delete()
        self.__db_session.commit()

    def find_all(self):
        return self.__db_session.query(User.user_id)

    def find_by_email(self, email):
        return self.__db_session.query(User).filter_by(email=email)

    def find_by_user_id(self, user_id):
        return self.__db_session.query(User).filter_by(user_id=user_id)

    def update_by_email(self, email, update_data):
        update_data["token"] = uuid.uuid4().hex

        self.find_by_email(email).update(update_data)
        self.__db_session.commit()
