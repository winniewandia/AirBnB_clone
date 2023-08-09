#!/usr/bin/python3
"""unittest for the FileStorage class
"""
import json
import os
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage


class TestFileStorage(unittest.TestCase):
    """This class contains the suite for FileStorage tests

    Args:
        unittest: class for unittest
    """

    def testException(self):
        """Tests the arguments of the save function
        """
        output = "FileStorage.save() takes 1 positional argument but 2 were given"
        with self.assertRaises(TypeError) as err:
            FileStorage.save(self, 20)
        self.assertEqual(str(err.exception), output)

    def testFileStorageAttr(self):
        """Checks if the FileStorage class has the attr __file_path
        and __objects
        """
        self.assertEqual(hasattr(FileStorage, '_FileStorage__file_path'), True)
        self.assertEqual(hasattr(FileStorage, '_FileStorage__objects'), True)

    def testStorageInstance(self):
        """Checks if storage is an instance of FileStorage
        """
        my_model = BaseModel()
        self.assertIsInstance(storage, FileStorage)

    def testAll(self):
        """Checks if the All method contains Keys and
        if created_at and updated_at for 2 different instances,
        if they are the same
        """
        my_model = BaseModel()
        my_model.name = "First Model"
        my_model.save()
        dict = my_model.to_dict()
        objects = storage.all()

        key = dict['__class__'] + "." + dict['id']
        self.assertEqual(key in objects, True)
        self.assertEqual(dict['name'], "First Model")

        created = dict['created_at']
        updated = dict['updated_at']
        my_model.name = "Second Model"
        my_model.save()
        dict = my_model.to_dict()
        objects = storage.all()
        self.assertEqual(key in objects, True)
        created2 = dict['created_at']
        updated2 = dict['updated_at']
        self.assertEqual(created, created2)
        self.assertNotEqual(updated, updated2)
        self.assertEqual(dict['name'], "Second Model")

    def test_new(self):
        """checks if the to_dicts method key, is the same as when
        deserialize json file to object and get the key
        """
        my_model = BaseModel()
        dict = my_model.to_dict()
        key1 = dict['__class__'] + "." + dict['id']
        storage.save()
        with open("file.json", 'r') as f:
            dict2 = json.load(f)
        my_dict = dict2[key1]
        for key in my_dict:
            self.assertEqual(dict[key], my_dict[key])

    def testReload(self):
        """Checks if the path of the __filepath exists and
        if the All method's objects are the same as the __objects
        """
        my_model = BaseModel()
        my_model.save()
        self.assertEqual(os.path.exists(storage._FileStorage__file_path), True)
        objs = storage.all()
        FileStorage._FileStorage__objects = {}
        self.assertNotEqual(objs, FileStorage._FileStorage__objects)
        storage.reload()
        for key, value in storage.all().items():
            self.assertEqual(objs[key].to_dict(), value.to_dict())

    def testSave(self):
        """Checks if the storage.all and __objects are the same
        """
        self.assertEqual(os.path.exists(storage._FileStorage__file_path), True)
        self.assertEqual(storage.all(), storage._FileStorage__objects)
