# -*- coding: utf-8 -*-

"""Functions for creating the PyBEL-Admin Flask app."""

import flask

import pybel
from .admin import build_admin_service

__all__ = [
    'create_app',
]


def create_app(connection=None):
    """Create a Flask app.

    :param connection: Either a connection string or PyBEL manager.
    :rtype: Optional[str or pybel.Manager]
    :rtype: flask.Flask
    """
    app = flask.Flask(__name__)
    manager = pybel.Manager.ensure(connection=connection)
    build_admin_service(app, manager)
    return app
