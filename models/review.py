#!/usr/bin/python3
"""This is the Review Model."""

from models.base_model import BaseModel


class Review(BaseModel):
    """This is a Review model inheriting from basemodel."""

    place_id = ""   # Place.id
    user_id = ""    # User.id
    text = ""

    def __init__(self, *args, **kwargs):
        """Initialize the Review object."""
        super().__init__(*args, **kwargs)
