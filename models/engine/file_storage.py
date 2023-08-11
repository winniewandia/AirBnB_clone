#!/usr/bin/python3
""" This module contains FileStorage class that is to
serialize and deserialize instances to a json file

    Returns:
        dict: The dict __object
"""
import json
import os

from models.user import User


class FileStorage:
    """This class  that serializes instances to 
    a JSON file and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """This method returns the dictionary __objects

        Returns:
            dictonary: The dictonary __object 
        """
        return FileStorage.__objects

    def new(self, obj):
        """This method sets in __objects the obj with key
        <obj class name>.id

        Args:
            obj: value of the dictonary
        """
        key = obj.__class__.__name__ + '.' + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """This method serializes __objects to the JSON
        file (path: __file_path)
        """
        copy_dict = {}
        for key, value in FileStorage.__objects.items():
            copy_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(copy_dict, f)

    def reload(self):
        """This method deserializes the JSON file to __objects
        (only if the JSON file
        """
        from models.base_model import BaseModel
        copy_dict = {'BaseModel': BaseModel, 'User': User}

        if os.path.exists(FileStorage.__file_path) is True:
            with open(FileStorage.__file_path, 'r') as f:
                for key, value in json.load(f).items():
                    self.new(copy_dict[value['__class__']](**value))
