#!/usr/bin/python3
"""This module contains the Review class
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """The Review class defines the place_id, user_id,
    and the text
    """
    place_id = ""
    user_id = ""
    text = ""
