""" Users service

Provides high level functions to manipulate user database

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 18/12/2016
"""

from model import User
from session import db_session


class UserService:

    def add_new(self,email, name, password, username):
        new_user = User(
            email=email, name=name, password=password, username=username
        )

        db_session.add(new_user)
        db_session.commit()

    def delete_by_username(self, username):
        self.find_by_username(username).delete()
        db_session.commit()

    def find_all(self):
        return db_session.query(User).all()

    def find_by_email(self, email):
        return db_session.query(User).filter_by(email=email)

    def find_by_username(self, username):
        return db_session.query(User).filter_by(username=username)

    def update_by_email(self, email, update_data):
        self.find_by_email(email).update(update_data)
        db_session.commit()

    def update_by_username(self, username, update_data):
        self.find_by_username(username).update(update_data)
        db_session.commit()
