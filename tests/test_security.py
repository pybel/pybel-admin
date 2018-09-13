# -*- coding: utf-8 -*-

"""Tests for PyBEL-Flask-Security."""

from pybel.testing.cases import TemporaryCacheMixin
from pybel_admin.security import SecurityManager


class TestSecurity(TemporaryCacheMixin):

    def setUp(self):
        """Set up this class with a security manager."""
        super().setUp()
        self.manager = SecurityManager(connection=self.connection)

    def test_one(self):
        """Test proper integration of the user datastore."""
        self.assertEqual(0, self.manager.count_users())
        self.assertEqual(0, self.manager.count_roles())

        u1 = self.manager.create_user(email='test@example.com')
        self.assertIsNotNone(u1)
        self.manager.commit()

        u2 = self.manager.find_user(email='test2@example.com')
        self.assertIsNone(u2)

        u3 = self.manager.find_user(email='test@example.com')
        self.assertIsNotNone(u3)
        self.assertEqual('test@example.com', u3.email)

        self.assertEqual(1, self.manager.count_users())
