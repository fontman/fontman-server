""" Channel service

Provides high level functions to manipulate channel database

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 18/12/2016
"""
from model import Channel
from session import db_session


class ChannelService:

    def add_new(self, key, name, type):
        new_channel = Channel(key=key, name=name, type=type)

        db_session.add(new_channel)
        db_session.commit()

    def delete_by_id(self, id):
        try:
            self.find_by_id(id).delete()
            db_session.commit()

            return True

        except:
            return False

    def find_all(self):
        return db_session.query(Channel).all()

    def find_by_id(self, id):
        return db_session.query(Channel).filter_by(id=id)

    def find_by_details(self, key, name, type):
        return db_session.query(Channel).filter_by(
            key=key, name=name, type=type
        )

    def update_by_id(self, id, update_list):
        self.find_by_id(id).update(update_list)
        db_session.commit()
