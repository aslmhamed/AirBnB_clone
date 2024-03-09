#!/usr/bin/python3
"""This is the BaseModel for all the models."""

from datetime import datetime
import models
import uuid

format_t = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel():
    """This is the basemodel upon which all classes will be formed from."""

    def __init__(self, *args, **kwargs):
        """Initialize the basemodel."""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if hasattr(self, "created_at") and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"], format_t)
            if hasattr(self, "updated_at") and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs["updated_at"], format_t)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
            models.storage.save()

    def __str__(self):
        """Return a string representation of the instance."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Save the object to the json file and updates the time."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Convert the object to a dictionary."""
        # new_dict = self.__dict__.copy()
        # if "created_at" in new_dict:
        #     new_dict["created_at"] = new_dict["created_at"]
        # if "updated_at" in new_dict:
        #     new_dict["updated_at"] = new_dict["updated_at"]
        # new_dict["__class__"] = self.__class__.__name__
        # return new_dict
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = obj_dict['created_at'].strftime(format_t)
        obj_dict['updated_at'] = obj_dict['updated_at'].strftime(format_t)
        return obj_dict
