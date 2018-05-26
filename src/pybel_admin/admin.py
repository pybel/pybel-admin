# -*- coding: utf-8 -*-

"""Functions for building the Flask-Admin extension."""

from flask_admin import Admin

from pybel.manager.models import (
    Annotation, AnnotationEntry, Author, Citation, Edge, Evidence, Namespace,
    NamespaceEntry, Network, Node,
)
from .views import AnnotationView, CitationView, EdgeView, EvidenceView, ModelView, NamespaceView, NetworkView, NodeView

__all__ = [
    'build_admin_service',
]


def _add_views(admin, session):
    """Add views for core PyBEL SQLAlchemy models.

    :param flask_admin.Admin admin:
    :param session:
    """
    admin.add_view(NetworkView(Network, session))
    admin.add_view(EdgeView(Edge, session))
    admin.add_view(NodeView(Node, session))
    admin.add_view(EvidenceView(Evidence, session))

    admin.add_view(CitationView(Citation, session))
    admin.add_view(ModelView(Author, session))

    admin.add_view(NamespaceView(Namespace, session, category='Namespace'))
    admin.add_view(ModelView(NamespaceEntry, session, category='Namespace', name='Entry'))

    admin.add_view(AnnotationView(Annotation, session, category='Annotation'))
    admin.add_view(ModelView(AnnotationEntry, session, category='Annotation', name='Entry'))

    return admin


def build_admin_service(app, manager, url='/'):
    """Add a Flask-Admin database front-end to a Flask app.

    :param flask.Flask app:
    :param pybel.Manager manager:
    :param str url: The url prefix of the service
    :rtype: flask_admin.Admin
    """
    admin = Admin(app, template_mode='bootstrap3', url=url)
    _add_views(admin, manager.session)
    return admin
