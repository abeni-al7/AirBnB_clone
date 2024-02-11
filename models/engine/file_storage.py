#!/usr/bin/python3
"""A module for file storage"""

import json


class FileStorage():
    """Serializes and deserializes instances to and from json files"""


    def __init__(self):
        """An initializer method"""
        self.__file_path = ""
        self.__objects = {}

    def all(self):
        """Returns __objects"""
        return self.__objects
    
    def new(self, obj):
        """Adds an object to the _objects dictionary"""
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj.to_dict()

    def save(self):
        """Serializes the objects dictionary to json"""
        with open(self.__file_path, "w+") as json_file:
            json.dump(self.__objects, json_file)

    def reload(self):
        """Deserializes the json file to objects dictionary"""
        try:
            with open(self.__file_path, "r") as json_file:
                self.__objects = json.load(json_file)
        except:
            pass
