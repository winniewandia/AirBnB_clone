#!/usr/bin/python3
"""This  module contains class User
"""
from models.base_model import BaseModel


class User(BaseModel):
    """ This class User inherits from BaseModel

    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
