#!/usr/bin/python3
"""
    This module contains the amenity model
    which defines all amenities in the application
"""

# external packages
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    amenity class for all amenities applications

    Args:
        name (str): empty string
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """calling parent class's constructor to set basic info"""
        super().__init__(*args, **kwargs)
