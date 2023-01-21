#!/usr/bin/python3
"""Contains the BaseModel class
"""


import models
import uuid
import datetime


date_fmt = "%Y-%m-%dT%H:%M:%S.%f"
now = datetime.datetime.now()


class BaseModel:
    """Defines all common attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """BaseModel Class Constructor
        """
        if kwargs:
            str_created_at = kwargs["created_at"]
            str_updated_at = kwargs["updated_at"]
            to_iso_created_at = datetime.datetime.strptime(
                str_created_at, date_fmt
            )
            to_iso_updated_at = datetime.datetime.strptime(
                str_updated_at, date_fmt
            )
            kwargs['created_at'] = to_iso_created_at
            kwargs['updated_at'] = to_iso_updated_at

            for k, v in kwargs.items():
                if k != '__class__':
                    setattr(self, k, v)

        else:
            id = uuid.uuid4()
            self.id = str(id)
            self.created_at = now
            self.updated_at = now
            models.storage.new(self)
            models.storage.save()

    def __str__(self):
        """Returns a neatly formated string representation
        """
        str_repr = "[{:s}] ({:s}) {}".format(
            self.__class__.__name__,
            self.id, self.__dict__)
        return str_repr

    def save(self):
        """Updates the public instance attribute updated_at\
            with the current datetime
        """
        self.updated_at = now
        models.storage.save()

    def to_dict(self):
        """ returns a dictionary containing all keys/values\
            of __dict__ of the instance
        """
        my_dict = self.__dict__.copy()
        iso_created_at = my_dict['created_at'].isoformat()
        iso_updated_at = my_dict['updated_at'].isoformat()
        my_dict['created_at'] = iso_created_at
        my_dict['updated_at'] = iso_updated_at
        my_dict["__class__"] = self.__class__.__name__
        return (my_dict)
