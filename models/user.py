#!/usr/bin/python3
"""A module for the user class"""

from models.base_model import BaseModel


class User(BaseModel):
    """A class for users"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
