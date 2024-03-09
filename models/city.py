#!/usr/bin/python3
"""This is the city model."""

from models.base_model import BaseModel


class City(BaseModel):
    """This is the model city that inherits from BaseModel."""

    state_id = ""    # State.id
    name = ""

    def __init__(self, *args, **kwargs):
        """Initialize the city model."""
        super().__init__(self, *args, **kwargs)
