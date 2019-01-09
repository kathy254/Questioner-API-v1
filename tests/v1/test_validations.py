import unittest
import datetime

from app.api.v1.utils.validations import Validations
from .base_tests import BaseTest


class TestValidations(BaseTest):
    def setUp(self):
        self.data = Validations()

    def tearDown(self):
        self.data = None

    def test_empty_data(self):
        """method to test if data is empty"""
        test = self.data.is_empty(["", "abcd"])
        self.assertTrue(test)

    def test_not_empty(self):
        """method to test that data is not emtpy"""
        test = self.data.is_empty(["abcd", "abcd"])
        self.assertFalse(test)

    def test_whitespace(self):
        """method to test presence of whitespace"""
        test = self.data.is_whitespace([" ", "efgh"])
        self.assertTrue(test)

    def test_not_whitespace(self):
        """method to test absence of whitespace"""
        test = self.data.is_whitespace(["efgh", "efgh"])
        self.assertFalse(test)

    def test_is_string(self):
        """method to test if input is a string"""
        test = self.data.is_string(["abcd", "efgh"])
        self.assertTrue(test)

    def test_is_not_string(self):
        """method to test if input is not a string"""
        test = self.data.is_string([1, 2])
        self.assertFalse(test)

    def test_is_integer(self):
        """method to test if input is an integer"""
        test = self.data.is_integer([1, 2, 3])
        self.assertTrue(test)

    def test_not_integer(self):
        """method to test if input is not an integer"""
        test1 = self.data.is_integer(["none", "one"])
        test2 = self.data.is_integer([1.34, 4.562])
        self.assertFalse(test1)
        self.assertFalse(test2)

    def test_valid_date(self):
        """method to test valid date format"""
        date = "12-12-2018"
        test = self.data.is_valid_date(date)
        self.assertTrue(test)

    def test_future_date(self):
        """method to test if date is in the future"""
        date = datetime.date(2019, 12, 12)
        test = self.data.is_future_date(date)
        self.assertTrue(test)

    def test_past_date(self):
        """method to test if date is in the past"""
        date = datetime.date(2018, 12, 12)
        test = self.data.is_future_date(date)
        self.assertFalse(test)

    def test_valid_email(self):
        test1 = self.data.is_valid_email("cat@gmail.com")
        test_ccTLD = self.data.is_valid_email("cat@mywork.co.ke")
        test3_longTLD = self.data.is_valid_email("cat@space.travel")
        test_upper = self.data.is_valid_email("CAT@SPACE.COM")
        self.assertTrue(test1)
        self.assertTrue(test_ccTLD)
        self.assertTrue(test3_longTLD)
        self.assertTrue(test_upper)

    def test_invalid_email(self):
        test1 = self.data.is_valid_email("lslslslslslsl")
        test2 = self.data.is_valid_email("email.com")
        self.assertFalse(test1)
        self.assertFalse(test2)

    


    
        

    