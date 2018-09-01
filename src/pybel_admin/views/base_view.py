# -*- coding: utf-8 -*-

"""This module contains model views for the Flask-Admin interface."""

import os
from typing import Type

from flask import redirect, request
from flask_admin.contrib.sqla import ModelView as BaseModelView

__all__ = [
    'ModelView',
]

PYBEL_WEB_ADMIN_USE_SECURITY = os.environ.get('PYBEL_WEB_ADMIN_USE_SECURITY', False)


def _patch_model_view() -> Type[BaseModelView]:
    if not PYBEL_WEB_ADMIN_USE_SECURITY:
        return BaseModelView

    from flask_security import current_user, url_for_security

    # redefine model view to have some more stuff in it
    class SecureModelView(BaseModelView):
        """Adds plugin for Flask-Security to Flask-Admin model views."""

        def is_accessible(self) -> bool:
            """Check the current user is an admin."""
            return current_user.is_authenticated and current_user.is_admin

        def inaccessible_callback(self, name, **kwargs):
            """Redirect to login page if user doesn't have access."""
            return redirect(url_for_security('login', next=request.url))

    return SecureModelView


ModelView = _patch_model_view()
