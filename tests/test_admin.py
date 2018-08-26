# -*- coding: utf-8 -*-

"""Tests for PyBEL-Admin."""

import logging

from pybel.manager.models import Network
from pybel.testing.cases import TemporaryCacheMixin
from pybel_admin import create_app

log = logging.getLogger(__name__)


class TestAdmin(TemporaryCacheMixin):
    """Tests for the PyBEL-Flask-Admin interface."""

    def setUp(self):
        """Set up a test application and client."""
        super(TestAdmin, self).setUp()

        self.app = create_app(connection=self.manager)
        self.client = self.app.test_client()

    def test_find_network(self):
        """Check a network is present."""
        n = Network(name='test network', version='1.0.0')
        self.manager.session.add(n)
        self.manager.session.commit()

        with self.app.app_context():
            response = self.client.get('/network', follow_redirects=True)
            self.assertIn('test network', response.data.decode('utf8'))
