# -*- coding: utf-8 -*-

"""Tests for PyBEL-Admin."""

import logging
import os
import tempfile
import unittest

from pybel import Manager
from pybel.manager.models import Network
from pybel_admin import create_app

log = logging.getLogger(__name__)

test_connection = os.environ.get('PYBEL_ADMIN_TEST_CONNECTION')


class TemporaryCacheMixin(unittest.TestCase):
    """A test case with a connection and manager."""

    def setUp(self):
        """Set up the connection and manager."""
        if test_connection:
            self.connection = test_connection
        else:
            self.fd, self.path = tempfile.mkstemp()
            self.connection = 'sqlite:///' + self.path
            log.info('Test generated connection string %s', self.connection)

        self.manager = Manager(connection=self.connection)
        self.manager.create_all()

    def tearDown(self):
        """Tear down the connection and manager."""
        self.manager.session.close()

        if not test_connection:
            os.close(self.fd)
            os.remove(self.path)
        else:
            self.manager.drop_all()


class TestAdmin(TemporaryCacheMixin):
    """Tests for the PyBEL-Admin interface."""

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
