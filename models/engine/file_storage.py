#!/usr/bin/python3
"""FileStorage BaseModel to handle serialization and deserialization of objects.
"""


import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


classes = {
    "State": State, "Amenity": Amenity, "Review": Review,
    "BaseModel": BaseModel, "City": City, "Place": Place, "User": User
}


class FileStorage:
    """Serializes and deserializes instances

    The attributes:
        __file_path: string - path to the json file
        __objects: dictionary - dictionary storing all the models
    """
    __file_path = "file.json"
    __objects = dict()

    def all(self):
        """returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id
        """
        obj_name = obj.__class__.__name__
        obj_id = obj.id
        obj_repr = "{}.{}".format(obj_name, obj_id)
        if obj is not None:
            self.__objects[obj_repr] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)
        """
        all_obj = dict()

        for k, v in self.__objects.items():
            all_obj[k] = v.to_dict()

        a_dict = json.dumps(all_obj)

        with open(self.__file_path, "w", encoding="utf-8") as f:
            f.write(a_dict)

    def reload(self):
        """deserializes the JSON file to __objects
        """
        file_name = self.__file_path
        try:
            with open(file_name, "r", encoding="utf-8") as f:
                str_json = f.read()
                dict_obj = json.loads(str_json)

                for k in dict_obj:
                    self.__objects[k] = classes[dict_obj[k]["__class__"]](
                        **dict_obj[k]
                    )

        except FileNotFoundError:
            pass
