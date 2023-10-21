#!/usr/bin/python3
"""This script is the file storage class for AirBnB"""
import json
import sys
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """This class for serializes  to JSON file and
    JSON file to instances
    Attributes:
        __file_path: for path to the JSON file
        __objects: for objects will be stored
    """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """for return this dictionary
        Return:
            return this dictionary of (__object)
        """
        if cls is None:
            return self.__objects
        else:
            new_dict = {}
            if len(self.__objects) > 0:
                for key, value in self.__objects.items():
                    if type(cls) is str:
                        if cls == key.split('.')[0]:
                            new_dict[key] = value
                    else:
                        if cls is type(value):
                            new_dict[key] = value
            return new_dict

    def new(self, obj):
        """this method for sets __object to given obj
        Args:
            obj: for given object
        """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """for serialize the file path to JSON file path
        """
        my_dict = {}
        for key, value in self.__objects.items():
            my_dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(my_dict, f)

    def reload(self):
        """for serialize the file path to JSON file path
        """
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                for key, value in (json.load(f)).items():
                    value = eval(value["__class__"])(**value)
                    self.__objects[key] = value
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """for Deletes obj from __objecs if its inside
        Not sure if it should also delete from json file
        """

        dict_key = ""
        for key, value in self.__objects.items():
            if obj == value:
                dict_key = key
        if dict_key is not "":
            del self.__objects[dict_key]

    def close(self):
        """ this for calls reload() for deserializing the JSON file to objects."""
        self.reload()
