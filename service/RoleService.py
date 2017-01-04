""" Roles service

High level functions to manipulate roles table.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 4/1/2017
"""

from model import Role
from session import db_session


class RoleService:

    def add_new(self, entity, entity_id, role, user_id):
        new_role = Role(
            entity=entity,
            entity_id=entity_id,
            role=role,
            user_id=user_id
        )

        db_session.add(new_role)
        db_session.commit()

        return new_role

    def delete_by_entity(self, entity):
        self.find_by_entity(entity).delete()
        db_session.commit()

    def delete_by_role_id(self, role_id):
        self.find_by_role_id(role_id).delete()
        db_session.commit()

    def delete_by_user_id(self, user_id):
        self.find_by_user_id(user_id).delete()
        db_session.commit()

    def delete_role(self, entity, entity_id, user_id):
        self.find_role(entity, entity_id, user_id).delete()
        db_session.commit()

    def find_all(self):
        return db_session.query(Role).all()

    def find_by_entity(self, entity):
        return db_session.query(Role).filter_by(entity=entity)

    def find_by_entity_id(self, entity, entity_id):
        return db_session.query(Role).filter_by(
            entity=entity, entity_id=entity_id
        )

    def find_by_role_id(self, role_id):
        return db_session.query(Role).filter_by(role_id=role_id)

    def find_by_user_id(self, user_id):
        return db_session.query(Role).filter_by(user_id=user_id)

    def find_role(self, entity, entity_id, user_id):
        return db_session.query(Role).filter_by(
            entity=entity, entity_id=entity_id, user_id=user_id
        )

    def update_by_role_id(self, role_id, update_data):
        self.find_by_role_id(role_id).update(update_data)
