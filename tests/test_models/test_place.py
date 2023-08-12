#!/usr/bin/python3
"""This module contains the unittest TestCase
for Amenity
"""
import unittest

from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    """Tests for the Place class
    """

    def test_instance(self):
        """Tests for Place's Instance
        """
        first_place = Place()
        self.assertIsInstance(first_place, Place)

    def test_attributes(self):
        """Tests if Place has the defined attributes
        """
        first_place = Place()
        self.assertTrue(hasattr(first_place, "city_id"))
        self.assertTrue(hasattr(first_place, "user_id"))
        self.assertTrue(hasattr(first_place, "name"))
        self.assertTrue(hasattr(first_place, "description"))
        self.assertTrue(hasattr(first_place, "number_rooms"))
        self.assertTrue(hasattr(first_place, "number_bathrooms"))
        self.assertTrue(hasattr(first_place, "max_guest"))
        self.assertTrue(hasattr(first_place, "price_by_night"))
        self.assertTrue(hasattr(first_place, "latitude"))
        self.assertTrue(hasattr(first_place, "longitude"))
        self.assertTrue(hasattr(first_place, "amenity_ids"))
        self.assertIsInstance(first_place.city_id, str)
        self.assertIsInstance(first_place.user_id, str)
        self.assertIsInstance(first_place.name, str)
        self.assertIsInstance(first_place.description, str)
        self.assertIsInstance(first_place.number_rooms, int)
        self.assertIsInstance(first_place.number_bathrooms, int)
        self.assertIsInstance(first_place.max_guest, int)
        self.assertIsInstance(first_place.price_by_night, int)
        self.assertIsInstance(first_place.latitude, float)
        self.assertIsInstance(first_place.longitude, float)
        self.assertIsInstance(first_place.amenity_ids, list)

    def test_class_name(self):
        """Checks the type for Place instance
        """
        firstPlace = Place()
        self.assertEqual(str(type(firstPlace)),
                         "<class 'models.place.Place'>")


if __name__ == '__main__':
    unittest.main()
