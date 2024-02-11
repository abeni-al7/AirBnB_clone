#!/usr/bin/python3
"""This module provides a base model."""

import uuid
from datetime import datetime
import models


class BaseModel():
    """A base model for all other classes."""

    def __init__(self, *args, **kwargs):
        """An initialization method"""
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, time_format)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def save(self):
        """Updates the updated_at time"""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing __dict__"""
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = self.__class__.__name__
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        return my_dict

    def __str__(self):
        """A string representation of an instance"""
        name = self.__class__.__name__
        return ("[{}] ({}) {}".format(name, self.id, self.__dict__))
