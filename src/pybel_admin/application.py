# -*- coding: utf-8 -*-

"""Functions for creating the PyBEL-Admin Flask app."""

from typing import Optional

from flask import Flask
from pybel import Manager

from .admin import build_admin_service

__all__ = [
    'create_app',
]


def create_app(manager: Optional[Manager] = None) -> Flask:
    """Create a Flask app.

    :param manager: Either a connection string or PyBEL manager.
    """
    app = Flask(__name__)

    if manager is None:
        manager = Manager()

    build_admin_service(app, manager)
    return app
