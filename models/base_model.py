#!/usr/bin/python3
"""Defines the BaseModel class."""

from uuid import uuid4
from datetime import datetime
from models import storage


class BaseModel:
    """
    Base model that defines all common attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize a new BaseModel instance

        Args:
            *args (any): unused
            **kwargs (dict): Key/value pairs of attributes.
        """
        dt_form = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, dt_form)
                else:
                    self.__dict__[k] = v
        else:
            storage.new(self)

    def save(self):
        """
        Update updated_at with the current datetime and call the save
        method from storage.
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Return the dictionary of the BaseModel instance.
        Includes the key/value pair __class__ representing the
        class name of the object.
        """
        our_dict = self.__dict__.copy()
        our_dict["created_at"] = self.created_at.isoformat()
        our_dict["updated_at"] = self.updated_at.isoformat()
        our_dict["__class__"] = self.__class__.__name__
        return our_dict

    def __str__(self):
        """
        Return the print/str representation of the BaseModel instance.
        """
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)

    def __repr__(self):
        """
        Return a string representation of the BaseModel instance.
        """
        return self.__str__()
