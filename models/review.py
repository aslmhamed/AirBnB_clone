#!/usr/bin/python3
"""This is the Review Model"""

from models.base_model import BaseModel


class Review(BaseModel):
    """This is a Review model inheriting from basemodel"""

    place_id = ""   # Place.id
    user_id = ""    # User.id
    text = ""
