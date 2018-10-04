# -*- coding: utf-8 -*-

"""Models for PyBEL-Flask-Security."""

from typing import Mapping

from flask_security import RoleMixin, UserMixin
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, Table, Text
from sqlalchemy.orm import backref, relationship

from pybel.manager.models import Base

__all__ = [
    'Role',
    'User',
    'roles_users',
]

ROLE_TABLE_NAME = 'pybel_role'
USER_TABLE_NAME = 'pybel_user'
ROLE_USER_TABLE_NAME = 'pybel_roles_users'

roles_users = Table(
    ROLE_USER_TABLE_NAME,
    Base.metadata,
    Column('user_id', Integer, ForeignKey('{}.id'.format(USER_TABLE_NAME)), primary_key=True),
    Column('role_id', Integer, ForeignKey('{}.id'.format(ROLE_TABLE_NAME)), primary_key=True)
)


class Role(Base, RoleMixin):
    """Represents a role."""

    __tablename__ = ROLE_TABLE_NAME

    id = Column(Integer, primary_key=True)
    name = Column(String(80), unique=True, nullable=False)
    description = Column(Text)

    def __str__(self):  # noqa: D105
        return self.name

    def to_json(self) -> Mapping:
        """Output this role as a JSON dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
        }


class User(Base, UserMixin):
    """Represents a user."""

    __tablename__ = USER_TABLE_NAME

    id = Column(Integer, primary_key=True)

    email = Column(String(255), unique=True, doc="The user's email")
    password = Column(String(255))
    name = Column(String(255), doc="The user's name")
    active = Column(Boolean)
    confirmed_at = Column(DateTime)

    roles = relationship(Role, secondary=roles_users, backref=backref('users', lazy='dynamic'))

    @property
    def is_admin(self) -> bool:
        """Check if this user is an administrator."""
        return self.has_role('admin')

    def __str__(self):  # noqa: D105
        return self.email

    def to_json(self, include_id: bool = True) -> Mapping:
        """Output this User as a JSON dictionary."""
        result = {
            'email': self.email,
            'roles': [
                role.name
                for role in self.roles
            ],
        }

        if include_id:
            result['id'] = self.id

        if self.name:
            result['name'] = self.name

        return result
