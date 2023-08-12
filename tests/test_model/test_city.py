#!/usr/bin/python3
"""This module contains the unittest TestCase
for City
"""
import unittest
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """Tests for the City class
    """

    def test_instance(self):
        """Tests for City's Instance
        """
        city_1 = City()
        self.assertIsInstance(city_1, City)

    def test_attributes(self):
        """Tests if City has the defined attributes
        """
        city_1 = City()
        self.assertTrue(hasattr(city_1, "name"))
        self.assertTrue(hasattr(city_1, "state_id"))
        self.assertIsInstance(city_1.name, str)
        self.assertIsInstance(city_1.state_id, str)

    def test_class_name(self):
        """Checks the type for City instance
        """
        city_1 = City()
        self.assertEqual(str(type(city_1)), "<class 'models.city.City'>")


if __name__ == '__main__':
    unittest.main()
