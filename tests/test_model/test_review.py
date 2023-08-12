#!/usr/bin/python3
"""This module contains the unittest TestCase
for Review
"""
import unittest

from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """Tests for the Review class
    """

    def test_instance(self):
        """Tests for Review's Instance
        """
        first_review = Review()
        self.assertIsInstance(first_review, Review)

    def test_attributes(self):
        """Tests if Review has the defined attributes
        """
        first_review = Review()
        self.assertTrue(hasattr(first_review, "place_id"))
        self.assertTrue(hasattr(first_review, "user_id"))
        self.assertTrue(hasattr(first_review, "text"))
        self.assertIsInstance(first_review.place_id, str)
        self.assertIsInstance(first_review.user_id, str)
        self.assertIsInstance(first_review.text, str)

    def test_class_name(self):
        """Checks the type for Review instance
        """
        first_review = Review()
        self.assertEqual(str(type(first_review)),
                         "<class 'models.review.Review'>")


if __name__ == '__main__':
    unittest.main()
