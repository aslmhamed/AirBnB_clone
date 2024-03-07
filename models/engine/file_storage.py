#!/usr/bin/python3
"""This is the file storage object."""


import json
from models.base_model import BaseModel

class FileStorage():
    """Storage object to store data in a json file and read it back."""

    __file_path = "store.json"
    __objects = {}

    def all(self):
        """Returns the dictionary objects."""
        return self.__objects

    def new(self, obj):
        """Appends a new object to the object dictionary."""
        if obj:
            self.__objects[f'{obj.__class__.__name__}.{obj.id}'] = obj


    def save(self):
        """Serialize the __objects dictionary to a json format and write it to a file."""
        json_ob = {}
        for key in self.__objects:
            json_ob[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(json_ob, file)

    def reload(self):
        """Deserialize the json objects in a file and store them in the objects dictionary."""
        try:
            with open(self.__file_path, 'r') as file:
                json_data = json.load(file)
            for key in json_data:
                self.__objects[key] = BaseModel(**json_data[key])
        except:
            pass


