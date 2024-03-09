#!/usr/bin/python3
"""This is the Place model."""

from models.base_model import BaseModel


class Place(BaseModel):
    """This is the place model inherting from Basemodel."""

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []    # Amenity.id - list of strings

    def __init__(self, *args, **kwargs):
        """Initialize the Place model from the Basemodel."""
        super().__init__(*args, **kwargs)
