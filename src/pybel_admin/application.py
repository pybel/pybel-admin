# -*- coding: utf-8 -*-

"""Functions for creating the PyBEL-Admin Flask app."""

import flask

from pybel import Manager
from .admin import build_admin_service
from typing import Optional
__all__ = [
    'create_app',
]


def create_app(connection:Optional[str]=None):
    """Create a Flask app.

    :param connection: Either a connection string or PyBEL manager.
    :rtype: flask.Flask
    """
    app = flask.Flask(__name__)
    manager = Manager(connection=connection)
    build_admin_service(app, manager)
    return app
