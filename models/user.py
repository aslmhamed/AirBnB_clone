#!/usr/bin/python3
"""This is the user Model."""
from models.base_model import BaseModel


class User(BaseModel):
    """This a user class."""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Initialize the user instance."""
        super().__init__(*args, **kwargs)
