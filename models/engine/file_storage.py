#!/usr/bin/python3
"""FileStorage BaseModel to handle serialization and\
    deserialization of objects.
"""


import os
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


classes = {
    "State": State,
    "Amenity": Amenity,
    "Review": Review,
    "BaseModel": BaseModel,
    "City": City, "Place": Place,
    "User": User
}


class FileStorage:
    """Serializes and deserializes instances

    The attributes:
        __file_path: string - path to the json file
        __objects: dictionary - dictionary storing all the models
    """
    __file_path = os.path.abspath("file.json")
    __objects = {}

    def __init__(self) -> None:
        """Instantiates the FileStorage class"""
        pass
    
    @classmethod
    def all(cls):
        """returns the dictionary __objects
        """
        return cls.__objects

    @classmethod
    def new(cls, obj):
        """sets in __objects the obj with key <obj class name>.id
        """
        obj_name = obj.__class__.__name__
        obj_id = obj.id
        if obj:
            obj_repr = f"{obj_name}.{obj_id}"
            cls.__objects[obj_repr] = obj

    @classmethod
    def save(cls):
        """serializes __objects to the JSON file (path: __file_path)
        """
        to_serialize = {k: v.to_dict() for k, v in cls.__objects.items()}

        with open(cls.__file_path, "w", encoding="utf-8") as f:
            json.dump(to_serialize, f, indent=4)

    @classmethod
    def reload(cls):
        """deserializes the JSON file to __objects
        """

        if os.path.exists(cls.__file_path):
            try:
                with open(cls.__file_path, "r", encoding="utf-8") as f:
                    object_dict = json.load(f)
                    for key, val in object_dict.items():
                        obj_name = val["__class__"]
                        obj = classes[obj_name]
                        cls.__objects[key] = obj(**val)

            except FileNotFoundError:
                pass
