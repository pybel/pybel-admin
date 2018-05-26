# -*- coding: utf-8 -*-

"""This module contains model views for the Flask-admin interface."""

import os

from flask_admin.contrib.sqla import ModelView as BaseModelView

PYBEL_WEB_ADMIN_USE_SECURITY = os.environ.get('PYBEL_WEB_ADMIN_USE_SECURITY', False)


def _patch_model_view():
    if not PYBEL_WEB_ADMIN_USE_SECURITY:
        return BaseModelView

    try:
        from flask_security import current_user, url_for_security
    except ImportError:
        return BaseModelView

    # import flask security
    from flask import redirect, request

    # redefine model view to have some more stuff in it
    class SecureModelView(BaseModelView):
        """Adds plugin for Flask-Security to Flask-Admin model views."""

        def is_accessible(self):
            """Check the current user is an admin."""
            return current_user.is_authenticated and current_user.is_admin

        def inaccessible_callback(self, name, **kwargs):
            """Redirect to login page if user doesn't have access."""
            return redirect(url_for_security('login', next=request.url))

    return SecureModelView


ModelView = _patch_model_view()
del _patch_model_view


class NetworkView(ModelView):
    """View for PyBEL networks."""

    column_exclude_list = ['blob', 'sha512', 'authors', 'description', 'copyright', 'disclaimer', 'licenses']


class AnnotationView(ModelView):
    """View for PyBEL annotations."""

    column_exclude_list = ['type', 'usage', 'author', 'license', 'citation_description']


class NamespaceView(ModelView):
    """View for PyBEL namespaces."""

    column_exclude_list = ['query_url', 'description', 'author', 'license', 'citation_description']


class ReportView(ModelView):
    """View for reports."""

    column_exclude_list = ['source', 'calculations', 'source_hash']
    column_display_pk = True
    column_default_sort = ('created', True)
    page_size = 50
    can_set_page_size = True


class _ExcludeBlobAndHashView(ModelView):
    column_exclude_list = ['blob', 'sha512']


class NodeView(_ExcludeBlobAndHashView):
    """View for PyBEL nodes."""


class EdgeView(_ExcludeBlobAndHashView):
    """View for PyBEL edges."""


class CitationView(_ExcludeBlobAndHashView):
    """View for PyBEL citations."""


class EvidenceView(_ExcludeBlobAndHashView):
    """View for PyBEL evidences."""


class ExperimentView(ModelView):
    """View for experiments."""

    column_exclude_list = ['source', 'result']


class UserView(ModelView):
    """View for users."""

    column_exclude_list = ['password']


class QueryView(ModelView):
    """View for queries."""

    column_exclude_list = ['dump']
    column_default_sort = ('created', True)
    column_display_pk = True
