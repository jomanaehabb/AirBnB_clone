#!/usr/bin/python3
"""
    This module contains the review model
    which defines all reviews in the application
"""

# external packages
from models.base_model import BaseModel


class Review(BaseModel):
    """
    review class for all reviews applications

    Args:
        place_id (str): empty string - it will be the Place.id
        user_id (str): empty string - it will be the User.id
        text (str): empty string
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """calling parent class's constructor to set basic info"""
        super().__init__(*args, **kwargs)
