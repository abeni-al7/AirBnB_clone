#!/usr/bin/python3
"""A module for review"""

from models.base_model import BaseModel


class Review(BaseModel):
    """A review class"""

    place_id = ""
    user_id = ""
    text = ""
