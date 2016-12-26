""" Users service

Provides high level functions to manipulate user database

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 18/12/2016
"""

import uuid

from model import User
from session import db_session


class UserService:

    def add_new(self, email, name, secret):
        try:
            key = self.generate_random_key()

            new_user = User(
                email=email,
                name=name,
                key=key,
                secret=secret
            )
            db_session.add(new_user)

        except:
            self.add_new(email, name, secret)

        db_session.commit()

    def find_all(self):
        return db_session.query(User).all()

    def find_by_email(self, email):
        return db_session.query(User).filter_by(email=email)

    def generate_random_key(self):
        return uuid.uuid4()

    def update_by_email(self, email, update_list):
        self.find_by_email(email).update(update_list)
        db_session.commit()
