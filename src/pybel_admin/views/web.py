# -*- coding: utf-8 -*-

from .base_view import ModelView

__all__ = [
    'ReportView',
    'ExperimentView',
    'QueryView',
]


class ReportView(ModelView):
    """View for reports."""

    column_exclude_list = ['source', 'calculations', 'source_hash']
    column_display_pk = True
    column_default_sort = ('created', True)
    page_size = 50
    can_set_page_size = True


class ExperimentView(ModelView):
    """View for experiments."""

    column_exclude_list = ['source', 'result']


class QueryView(ModelView):
    """View for queries."""

    column_exclude_list = ['dump']
    column_default_sort = ('created', True)
    column_display_pk = True
