#!/usr/bin/python3
"""
    This module contains the user model
    which defines all users in the application
"""

# external packages
from models.base_model import BaseModel


class User(BaseModel):
    """
    User class for all users applications

    Args:
        email (str): empty string
        password (str): empty string
        first_name (str): empty string
        last_name: (str): empty string
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """calling parent class's constructor to set basic info"""
        super().__init__(*args, **kwargs)
