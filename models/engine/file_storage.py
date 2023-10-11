#!/usr/bin/python3
"""
This module handles issues of storage of data in JSON files
"""

import json


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
        """adds a new object to the JSON file"""
        key = str(obj['__class__']) + '.' + str(obj['id'])
        self.__objects[key] = obj

    def save(self):
        """saves the JSON file from __objects dict"""
        with open(self.__file_path, "w") as f:
            json.dump(self.__objects, f)

    def reload(self):
        """
        reloads the JSON file to __objects dict

        Raises:
            FileNotFoundError: if the JSON file doesn't exist
        """
        try:
            with open(self.__file_path, "r") as f:
                self.__objects = json.load(f)
        except FileNotFoundError:
            pass
