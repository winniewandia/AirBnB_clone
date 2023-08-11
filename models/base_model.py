#!/usr/bin/python3
"""This module contains the BaseModel class that
defines all common attributes/methods for other classes
"""
import uuid
from datetime import datetime
from datetime import date


class BaseModel:
    """This BaseModel class contains the methods and
    attributes for other classes
    """

    def __init__(self, *args, **kwargs):
        """This is used to initialize the attributes
    and set up the initial state of the object
        """
        format = "%Y-%m-%dT%H:%M:%S.%f"
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            from models import storage
            storage.new(self)
        else:
            if '__class__' in kwargs:
                kwargs.pop('__class__')
            for key, value in kwargs.items():
                if key == 'created_at' or key == "updated_at":
                    value = datetime.strptime(value, format)
                setattr(self, key, value)

    def __str__(self):
        """returns the informal string representation of the object

        Returns:
            str: informal description
        """
        return ("[{}] ({}) {}".
                format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """updates the public instance attribute updated_at with
        the current datetime
        """
        self.updated_at = datetime.now()
        from models import storage
        storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__
        of the instance

        Returns:
            dict: instance dictionary
        """
        dict_copy = self.__dict__.copy()
        if 'created_at' in dict_copy:
            dict_copy['created_at'] = dict_copy['created_at'].isoformat()
        if 'updated_at' in dict_copy:
            dict_copy['updated_at'] = dict_copy['updated_at'].isoformat()

        dict_copy['__class__'] = self.__class__.__name__
        return dict_copy
