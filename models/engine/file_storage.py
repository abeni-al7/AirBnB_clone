#!/usr/bin/python3
"""A module for file storage"""
import json
from models.base_model import BaseModel


class FileStorage(BaseModel):
    """A class for file storage"""
    
    def __init__(self):
        """An initialization method"""
        self.__file_path = "file.json"
        self.__objects = {}
        super.__init__()

    def all(self):
        """Returns the objects dictionary"""
        return self.__objects
    
    def new(self, obj):
        """Sets an object in the dictionary"""
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """Serializes objects"""
        with open(self.__file_path, "w+") as json_file:
            json.dump(self.__objects, json_file)
    
    def reload(self):
        """Reload objects from a json file"""
        try:
            with open(self.__file_path, "r") as json_file:
                self.__objects = json.load(json_file)
        except FileNotFoundError:
            pass
