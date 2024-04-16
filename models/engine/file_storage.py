#!/usr/bin/python3
"""Defines the FileStorage class for AirBnB."""

import json
from models.base_model import BaseModel

class FileStorage:
    """Manages storage of objects in JSON format."""

    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of all objects or a class-specific one."""
        if cls:
            return {k: v for k, v in self.__objects.items() if isinstance(v, cls)}
        return self.__objects

    def new(self, obj):
        """Adds a new object to the storage dictionary."""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Saves the objects dictionary to the JSON file."""
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, f)

    def reload(self):
        """Loads objects from the JSON file into the storage dictionary."""
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                data = json.load(f)
                self.__objects = {k: BaseModel(**v) for k, v in data.items()}
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Removes an object from the storage dictionary."""
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            del self.__objects[key]

    def close(self):
        """Reloads the objects from the JSON file."""
        self.reload()
