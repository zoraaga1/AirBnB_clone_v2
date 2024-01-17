#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls is not None:
            if type(cls) == str:  # noqa
                cls = eval(cls)
            cls_dict = {}
            for k, v in self.__objects.items():
                if type(v) == cls:  # noqa
                    cls_dict[k] = v
            return cls_dict
        return self.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj

    def save(self):
        """Saves storage dictionary to file"""
        serialized_obj = {o: self.__objects[o].to_dict() for o in self.__objects.keys()}  # noqa
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(serialized_obj, f)

    def reload(self):
        """Import storage dictionary from models classes"""
        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                for objec in json.load(f).values():
                    name = objec["__class__"]
                    del objec["__class__"]
                    self.new(eval(name)(**objec))
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """delete obj from _objects"""
        try:
            del self.__objects["{}.{}".format(type(obj).__name__, obj.id)]
        except (AttributeError, KeyError):
            pass

    def close(self):
        """Call the Reload method and close"""
        self.reload()
