#!/usr/bin/python3
"""This module contains the tests for BaseModel class
"""
import datetime
from io import StringIO
import unittest
from unittest.mock import patch
from models.base_model import BaseModel


class TestBaseClass(unittest.TestCase):
    def test_init(self):
        my_model = BaseModel()
        my_model.name = "First Model"
        my_model.number = 10
        my_model.save()
        my_model_json = my_model.to_dict()
        self.assertEqual(my_model.name, my_model_json['name'])
        self.assertEqual(my_model.number, my_model_json['number'])
        self.assertEqual('BaseModel', my_model_json['__class__'])
        self.assertEqual(my_model.id, my_model_json['id'])

    def test_diff_object_time(self):
        my_model1 = BaseModel()
        my_model1.name = "First"
        my_model1.save()
        self.assertIsInstance(my_model1.id, str)
        self.assertIsInstance(my_model1.name, str)
        self.assertIsInstance(my_model1.created_at, datetime.datetime)
        self.assertIsInstance(my_model1.updated_at, datetime.datetime)
        dict_1 = my_model1.to_dict()

        my_model2 = BaseModel()
        my_model2.save()
        dict_2 = my_model1.to_dict()
        self.assertEqual(
            dict_1['created_at'], dict_2['created_at'])
        self.assertNotEqual(
            my_model1.updated_at, my_model2.updated_at)
       
    def test_kwargs(self):
        my_model = BaseModel()
        my_model.name = "First"
        my_model.number = 20
        my_model_json = my_model.to_dict()
        my_new_model = BaseModel(**my_model_json)

        output = "<class 'datetime.datetime'>"
        with patch("sys.stdout", StringIO()) as my_str:
            type(my_new_model.created_at)
            self.assertEqual(my_str.get_value(), output)


if __name__ == '__main__':
    unittest.main()
