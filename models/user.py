#!/usr/bin/python3
"""Contains User class
"""


from models.base_model import BaseModel


class User(BaseModel):
    """Inherits from BaseModel
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """User class constructor
        """
        super().__init__(*args, **kwargs)
