#!/usr/bin/python3
"""Contains the BaseModel class
"""


import uuid
from datetime import datetime
import models
# iso_format = "%Y-%m-%dT%H:%M:%S.%f" # Custom datetime string


class BaseModel:
    """Defines all common attributes/methods for other classes.

    This will serve as the parent class for all the other classes.
    """

    def __init__(self, *args, **kwargs):
        """BaseModel Class Constructor.
        """
        if kwargs:
            for key, val in kwargs.items():
                if key in ("created_at", "updated_at"):
                    # val = datetime.strptime(val, iso_format) # Custom
                    # datetime string
                    val = datetime.fromisoformat(val)
                if key != "__class__":
                    setattr(self, key, val)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Returns a neatly formated string representation of\
        our object instances.
        """
        str_repr = "[{:s}] ({:s}) {}".format(
            self.__class__.__name__,
            self.id, self.__dict__)
        return str_repr

    def save(self):
        """Updates the public instance attribute updated_at\
            with the current datetime.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ returns a dictionary containing all keys/values\
            of __dict__ of the instance.

            This method will be used to serialize all objects.
        """
        my_dict = self.__dict__.copy()
        iso_created_at = my_dict["created_at"].isoformat()
        iso_updated_at = my_dict["updated_at"].isoformat()
        my_dict["created_at"] = iso_created_at
        my_dict["updated_at"] = iso_updated_at
        my_dict["__class__"] = self.__class__.__name__
        return (my_dict)
