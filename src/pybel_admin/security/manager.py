# -*- coding: utf-8 -*-

"""Manager for PyBEL-Flask-Security."""

from flask_security import SQLAlchemyUserDatastore

from pybel import Manager
from pybel.manager.models import Base
from .models import Role, User

__all__ = [
    'SecurityManager',
]


class SecurityManager(Manager, SQLAlchemyUserDatastore):
    """A wrapper around the PyBEL manager and :class:`flask_security.SQLAlchemyUserDatastore`."""

    def __init__(self, connection=None, engine=None, session=None, user_model=User, role_model=Role):
        super(Manager, self).__init__(connection=connection, engine=engine, session=session)

        Base.metadata.bind = self.engine
        Base.query = self.session.query_property()

        SQLAlchemyUserDatastore.__init__(self, db=self, user_model=user_model, role_model=role_model)

    def count_users(self) -> int:
        """Count the number of users."""
        return self.session.query(User).count()

    def count_roles(self) -> int:
        """Count the number of roles."""
        return self.session.query(Role).count()
