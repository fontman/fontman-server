""" Ratings service

High level functions to manipulate ratings table.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 4/1/2017
"""

from model import Rating
from session import DBSession


class RatingService:
    
    def __init__(self):
        self.__db_session = DBSession()

    def add_new(self, entity, entity_id, user_id, value, comment):
        new_rating = Rating(
            comment=comment,
            entity=entity,
            entity_id=entity_id,
            user_id=user_id,
            value=value
        )

        self.__db_session.add(new_rating)
        self.__db_session.commit()

        return new_rating

    def delete_by_entity(self, entity):
        self.find_by_entity(entity).delete()
        self.__db_session.commit()

    def delete_by_entity_id(self, entity, entity_id):
        self.find_by_entity_id(entity, entity_id).delete()
        self.__db_session.commit()

    def delete_by_user_id(self, user_id):
        self.find_by_user_id(user_id).delete()
        self.__db_session.commit()

    def delete_rating(self, entity, entity_id, user_id):
        self.find_rating(entity, entity_id, user_id).delete()
        self.__db_session.commit()

    def find_all(self):
        return self.__db_session.query(Rating).all()

    def find_by_entity(self, entity):
        return self.__db_session.query(Rating).filter_by(entity=entity)

    def find_by_entity_id(self, entity, entity_id):
        return self.__db_session.query(Rating).filter_by(
            entity=entity, entity_id=entity_id
        )

    def find_by_rating_id(self, rating_id):
        return self.__db_session.query(Rating).filter_by(rating_id=rating_id)

    def find_by_user_id(self, user_id):
        return self.__db_session.query(Rating).filter_by(user_id=user_id)

    def find_rating(self, entity, entity_id, user_id):
        return self.__db_session.query(Rating).filter_by(
            entity=entity, entity_id=entity_id, user_id=user_id
        )

    def update_by_rating_id(self, rating_id, update_data):
        self.find_by_rating_id(rating_id).update(update_data)
        self.__db_session.commit()
