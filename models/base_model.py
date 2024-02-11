#!/usr/bin/python3
"""This module provides a base model."""

import uuid
from datetime import datetime


class BaseModel():
    """A base model for all other classes."""

    def __init__(self, *args, **kwargs):
        """An initialization method"""
        if kwargs:
            for key in kwargs.keys():
                if key == "created_at" or key == "updated_at":
                    kwargs[key] = datetime.strptime(kwargs[key], "%Y-%m-%dT%H:%M:%S.%f")
            self.__dict__.update(**kwargs)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def save(self):
        """Updates the updated_at time"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary containing __dict__"""
        my_dict = self.__dict__
        my_dict["__class__"] = self.__class__.__name__
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        return my_dict

    def __str__(self):
        """A string representation of an instance"""
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))
