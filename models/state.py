#!/usr/bin/python3
"""
    This module contains the state model
    which defines all states in the application
"""

# external packages
from models.base_model import BaseModel


class State(BaseModel):
    """
    state class for all states applications

    Args:
        name (str): empty string
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """calling parent class's constructor to set basic info"""
        super().__init__(*args, **kwargs)
