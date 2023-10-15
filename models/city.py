#!/usr/bin/python3
"""
    This module contains the city model
    which defines all cities in the application
"""

# external packages
from models.base_model import BaseModel


class City(BaseModel):
    """
    city class for all cities applications

    Args:
        state_id (str): empty string, it will be the State.id
        name (str): empty string
    """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """calling parent class's constructor to set basic info"""
        super().__init__(*args, **kwargs)
