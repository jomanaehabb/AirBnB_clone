#!/usr/bin/python3

import uuid
from datetime import datetime


"""
    This module contains the base model of our other models
    which defines all common attributes/methods for other classes
"""


class BaseModel:
    """Base class for all models"""

    def __init__(self, *args, **kwargs):
        """
        initializing public instances necessary while creating objects

        Args:
            *args (optional):
            **kwargs (optional):
        """
        self.id = str(uuid.uuid4())
        self.created_at = (datetime.now())
        self.updated_at = self.created_at

    def __str__(self):
        """string represntation of the object"""
        return (f"[{self.name}] ({self.id}) {self.__dict__}")

    def save(self):
        """updating update_at instance attribute"""
        self.updated_at = (datetime.now())

    def to_dict(self):
        """generating a dictionary represnting the object preparing for JSON"""
        object_dict_JSON = self.__dict__
        object_dict_JSON['created_at'] = (self.created_at).isoformat()
        object_dict_JSON['updated_at'] = (self.updated_at).isoformat()
        object_dict_JSON['__class__'] = self.__class__.__name__
        return object_dict_JSON
