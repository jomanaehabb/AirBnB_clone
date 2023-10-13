#!/usr/bin/python3
"""
This module handles issues of storage of data in JSON files
"""

import json
import copy


class FileStorage:
    """
    a base model for the storage part of the program

    Attributes:
        __file_path (str): path to the JSON file
        __objects (dict): a dictionary containing all objects
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns all objects in the JSON file"""
        return self.__objects

    def new(self, obj):
        """adds a new object to __objects dict"""
        key = obj.__class__.__name__ + '.' + obj.id
        (self.__objects)[key] = obj

    def save(self):
        """
        converting objs stored in __objects
        to strings for saving into JSON file
        """
        objs_dict = copy.deepcopy(self.__objects)
        for key, value in objs_dict.items():
            objs_dict[key] = value.to_dict()

        with open(self.__file_path, "w") as f:
            json.dump(objs_dict, f)

    def reload(self):
        """
        reloads the JSON file to __objects dict

        Raises:
            FileNotFoundError: if the JSON file doesn't exist
        """

        from ..base_model import BaseModel

        try:
            with open(self.__file_path, "r") as f:
                loaded_objs = json.load(f)
        except FileNotFoundError:
            return

        for key, value in loaded_objs.items():
            self.__objects[key] = BaseModel(**value)

    def destroy(self, obj):
        """Removing a specific object permanently"""
        obj_key = obj.__class__.__name__ + '.' + obj.id
        (self.__objects).pop(obj_key)
        self.save()
