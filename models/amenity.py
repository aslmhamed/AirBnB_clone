#!/usr/bin/python3
"""This is the Amenity Model"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """This is the Amenity model that inherits from BaseModel"""

    name = ""

    def __init__(self, *args, **kwargs):
        """Initializes the Amenity model from the BaseModel."""
        super().__init__(self, *args, **kwargs)
