#!/usr/bin/python3
"""This module contains the unittest TestCase
for User
"""
import unittest
from models.base_model import BaseModel

from models.user import User


class TestUser(unittest.TestCase):
    """Tests for the User class
    """

    def test_instance(self):
        """Tests for User's Instance
        """
        user_1 = User()
        self.assertIsInstance(user_1, User)

    def test_attributes(self):
        """Tests if User has the defined attributes
        """
        user_1 = User()
        self.assertTrue(hasattr(user_1, "email"))
        self.assertTrue(hasattr(user_1, "password"))
        self.assertTrue(hasattr(user_1, "first_name"))
        self.assertTrue(hasattr(user_1, "last_name"))
        self.assertIsInstance(user_1.first_name, str)
        self.assertIsInstance(user_1.email, str)
        self.assertIsInstance(user_1.password, str)
        self.assertIsInstance(user_1.last_name, str)

    def test_class_name(self):
        """Checks the type for User instance
        """
        user_1 = User()
        self.assertEqual(str(type(user_1)), "<class 'models.user.User'>")


if __name__ == '__main__':
    unittest.main()
