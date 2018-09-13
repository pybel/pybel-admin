# -*- coding: utf-8 -*-

"""Functions for building the Flask-Admin extension."""

from flask import Flask
from flask_admin import Admin

from pybel import Manager
from pybel.manager.models import Author, Citation, Edge, Evidence, Namespace, NamespaceEntry, Network, Node
from .views import AuthorView, CitationView, EdgeView, EvidenceView, NameView, NamespaceView, NetworkView, NodeView

__all__ = [
    'build_admin_service',
]


def _add_views(admin: Admin, session):
    """Add views for core PyBEL SQLAlchemy models.

    :param admin: A Flask-Admin extension
    :param session: A SQLAlchemy session
    """
    admin.add_view(NetworkView(Network, session))

    admin.add_view(NamespaceView(Namespace, session))
    admin.add_view(NameView(NamespaceEntry, session))

    admin.add_view(EdgeView(Edge, session))
    admin.add_view(NodeView(Node, session))
    admin.add_view(EvidenceView(Evidence, session))

    admin.add_view(CitationView(Citation, session))
    admin.add_view(AuthorView(Author, session))

    return admin


def build_admin_service(app: Flask, manager: Manager, url: str = '/') -> Admin:
    """Add a Flask-Admin database front-end to a Flask app.

    :param app:
    :param manager:
    :param url: The url prefix of the service
    """
    admin = Admin(app, template_mode='bootstrap3', url=url)
    _add_views(admin, manager.session)
    return admin
