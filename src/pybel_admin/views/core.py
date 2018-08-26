# -*- coding: utf-8 -*-

"""Views for PyBEL-Flask-Admin."""

from .base_view import ModelView

__all__ = [
    'NetworkView',
    'NamespaceView',
    'NodeView',
    'EdgeView',
    'CitationView',
    'EvidenceView',
    'NameView',
    'AuthorView',
]


class NetworkView(ModelView):
    """View for PyBEL networks."""

    column_exclude_list = ['blob', 'sha512', 'authors', 'description', 'copyright', 'disclaimer', 'licenses']
    column_searchable_list = ['name']


class NamespaceView(ModelView):
    """View for namespaces."""

    column_exclude_list = [
        'uploaded',
        'query_url',
        'description',
        'author',
        'license',
        'citation',
        'citation_version',
        'citation_url',
        'citation_description',
        'citation_published',
        'contact',
        'created',
        'domain',
        'miriam_id',
        'miriam_uri',
        'miriam_description',
        'miriam_namespace',
        'miriam_name',
        'species',
    ]
    column_searchable_list = ['name']


class NameView(ModelView):
    """View for names."""

    column_searchable_list = ['name', 'identifier']


class AuthorView(ModelView):
    """View for authors."""

    column_exclude_list = ['sha512']
    column_searchable_list = ['name']


class _ExcludeBlobAndHashView(ModelView):
    """Views that share excluding a BLOB and SHA512 hash field."""

    column_exclude_list = ['blob', 'sha512']


class NodeView(_ExcludeBlobAndHashView):
    """View for PyBEL nodes."""

    column_searchable_list = ['bel']


class EdgeView(_ExcludeBlobAndHashView):
    """View for PyBEL edges."""

    column_searchable_list = ['bel']


class CitationView(_ExcludeBlobAndHashView):
    """View for PyBEL citations."""

    column_searchable_list = ['reference']


class EvidenceView(_ExcludeBlobAndHashView):
    """View for PyBEL evidences."""

    column_searchable_list = ['text']
