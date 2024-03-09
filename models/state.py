#!/usr/bin/python3
"""This is the state model."""

from models.base_model import BaseModel


class State(BaseModel):
    """This is a state model that inherits from Basemodel."""

    name = ""

    def __init__(self, *args, **kwargs):
        """Initialize the state model."""
        super().__init__(*args, **kwargs)
