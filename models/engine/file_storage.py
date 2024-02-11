#!/usr/bin/python3
"""A module for file storage"""
import json


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
        """Reload objects from a json file"""
        try:
            with open(FileStorage.__file_path) as json_file:
                obj_dict = json.load(json_file)
                for obj in obj_dict.values():
                    class_name = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(class_name)(**obj))
        except FileNotFoundError:
            return
