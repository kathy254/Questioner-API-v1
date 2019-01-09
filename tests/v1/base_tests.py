"""
    This contains tests that will be reused by all test files
"""

import unittest
from app import create_app
from app.api.v1.models.meetup_models import meetup_list
from app.api.v1.models.user_models import user_accounts


class BaseTest(unittest.TestCase):
    """
    This class holds all similar test configurations
    """

    def setUp(self):
        self.app = create_app("testing")
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()

    def tearDown(self):
        """removes the dictionaries and the context"""
        del meetup_list[:]
        del user_accounts[:]
