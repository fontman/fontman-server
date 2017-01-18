""" Users service

Provides high level functions to manipulate user database

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 18/12/2016
"""

import uuid

from model import User
from session import db_session


class UserService:

    def add_new(self, email, name, password):
        new_user = User(
            email=email,
            name=name,
            password=password,
            token = uuid.uuid4().hex
        )

        db_session.add(new_user)
        db_session.commit()

        return new_user

    def delete_by_email(self, email):
        self.find_by_email(email).delete()
        db_session.commit()

    def find_all(self):
        return db_session.query(User.user_id)

    def find_by_email(self, email):
        return db_session.query(User).filter_by(email=email)

    def find_by_user_id(self, user_id):
        return db_session.query(User).filter_by(user_id=user_id)

    def find_token_by_email(self, email):
        return self.find_by_email(email).uuid

    def update_by_email(self, email, update_data):
        if "password" in update_data:
            update_data["token"] = uuid.uuid4().hex
            self.find_by_email(email).update(update_data)
        else:
            self.find_by_email(email).update(update_data)
        db_session.commit()
