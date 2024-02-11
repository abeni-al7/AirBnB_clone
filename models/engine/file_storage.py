#!/usr/bin/python3
"""A module for file storage"""
import json
from models.base_model import BaseModel


class FileStorage():
    """A class for file storage"""
    
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the objects dictionary"""
        return FileStorage.__objects
    
    def new(self, obj):
        """Sets an object in the dictionary"""
        name = obj.__class__.__name__ 
        key = "{}.{}".format(name, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes objects"""
        my_objs = FileStorage.__objects
        obj_dict = {obj: my_objs[obj].to_dict() for obj in my_objs.keys()}
        with open(FileStorage.__file_path, "w") as json_file:
            json.dump(obj_dict, json_file)

    def reload(self):
        """Deserialize the JSON file if it exists."""
        try:
            with open(FileStorage.__file_path, "r") as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
