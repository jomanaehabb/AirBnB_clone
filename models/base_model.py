#!/usr/bin/python3
"""
    This module contains the base model of our other models
    which defines all common attributes/methods for other classes
"""

# external packages
import uuid
from datetime import datetime
import copy

# internal packages
from models import storage


class BaseModel:
    """Base class for all models"""

    def __init__(self, *args, **kwargs):
        """

        initializing public instances with attributes
        necessary while creating objects, and save objects
        into JSON file once they are created fro the first time

        Args:
            *args (optional):
            **kwargs (optional, dict): attributes to create instance with
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    pass
                elif key == "created_at":
                    self.created_at = datetime.fromisoformat(str(value))
                elif key == "updated_at":
                    self.updated_at = datetime.fromisoformat(str(value))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = (datetime.now())
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        """string represntation of the object"""
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """
        updating update_at instance attribute, and
        saving the object to the JSON file
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """generating a dictionary represnting the object preparing for JSON"""
        object_dict_JSON = copy.deepcopy(self.__dict__)
        object_dict_JSON['created_at'] = (self.created_at).isoformat()
        object_dict_JSON['updated_at'] = (self.updated_at).isoformat()
        object_dict_JSON['__class__'] = self.__class__.__name__
        return object_dict_JSON
