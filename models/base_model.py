#!/usr/bin/python3
"""This is the BaseModel for all the models."""

from datetime import datetime
import uuid
import models


class BaseModel():
    """This is the basemodel upon which all classes will be formed from."""

    def __init__(self, *args, **kwargs):
        """Initialize the basemodel"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if hasattr(self, "created_at") and type(self.created_at) is str:
                self.created_at = datetime.fromisoformat(kwargs["created_at"])
            if hasattr(self, "updated_at") and type(self.updated_at) is str:
                self.updated_at = datetime.fromisoformat(kwargs["updated_at"])
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)
            models.storage.save()

    def __str__(self):
        """Return a string representation of the instance."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        new_dict = self.__dict__.copy()
        if "created_at" in new_dict:
            new_dict["created_at"] = new_dict["created_at"].isoformat()
        if "updated_at" in new_dict:
            new_dict["updated_at"] = new_dict["updated_at"].isoformat()
        new_dict["__class__"] = self.__class__.__name__
        return new_dict
        # obj_dict = self.__dict__.copy()
        # obj_dict['__class__'] = self.__class__.__name__
        # obj_dict['created_at'] = obj_dict['created_at'].isoformat()
        # obj_dict['updated_at'] = obj_dict['updated_at'].isoformat()
        # return obj_dict
