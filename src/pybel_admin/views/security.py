# -*- coding: utf-8 -*-

from .base_view import ModelView

__all__ = [
    'UserView',
]


class UserView(ModelView):
    """View for users."""

    column_exclude_list = ['password']
