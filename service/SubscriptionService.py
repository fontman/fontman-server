""" Subscription service

Provides high level functions to manipulate subscriptions table.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 27/12/2016
"""

from model import Subscription
from session import db_session


class SubscriptionService:

    def add_new(self, current_revision, end_date, font_id, start_date, user_id):
        new_subscription = Subscription(
            current_revision=current_revision,
            end_date=end_date,
            font_id=font_id,
            start_date=start_date,
            user_id=user_id
        )

        db_session.add(new_subscription)
        db_session.commit()

    def delete_by_font_id(self, font_id):
        self.find_by_font_id(font_id).delete()
        db_session.commit()

    def delete_by_user_id(self, user_id):
        self.find_by_user_id(user_id).delete()
        db_session.commit()

    def find_by_font_id(self, font_id):
        return db_session.query(Subscription).filter_by(font_id=font_id)

    def find_by_user_id(self, user_id):
        return db_session.query(Subscription).filter_by(user_id=user_id)

    def find_subscription(self, font_id, user_id):
        return db_session.query(Subscription).filter_by(
            font_id=font_id,
            user_id=user_id
        )

    def update_by_font_id(self, font_id, update_data):
        self.find_by_font_id(font_id).update(update_data)
        db_session.commit()

    def update_subscription(self, font_id, user_id, update_data):
        self.find_subscription(font_id, user_id).update(update_data)
        db_session.commit()
