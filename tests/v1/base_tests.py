"""
    This contains tests that will be reused by all test files
"""

import unittest
from app import create_app


class BaseTest(unittest.TestCase):
    """
    This class holds all similar test configurations
    """

    def setUp(self):
        self.app = create_app("testing")
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()

    def tearDown(self):
        pass
