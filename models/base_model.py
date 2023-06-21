#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""

import uuid
import models
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

"""
Remove the inheritance of BaseModel from Base.
The BaseModel class should now inherit directly from object.
"""
Base = declarative_base()


class BaseModel:
    """This class will defines all common attributes/methods
    Attributes
        id: to represents the id
        created_at: to represents a column containing a datetime
        updated_at: to represents the updated date time.
    """
    id = Column(String(60), unique=True, nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=(datetime.utcnow()))
    updated_at = Column(DateTime, nullable=False, default=(datetime.utcnow()))

    def __init__(self, *args, **kwargs):
        """Instantiation of base model class."""
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
            if "id" not in kwargs:
                self.id = str(uuid.uuid4())
            if "created_at" not in kwargs:
                self.created_at = datetime.now()
            if "updated_at" not in kwargs:
                self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """Returns a string representation of the instance."""
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def __repr__(self):
        """return a string representaion"""
        return self.__str__()

    def save(self):
        """
        Updates updated_at with current time when instance is changed
        """
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Convert instance into dict format."""
        new_dict = dict(self.__dict__)
        new_dict["__class__"] = str(type(self).__name__)
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        if '_sa_instance_state' in new_dict.keys():
            del new_dict['_sa_instance_state']
        return new_dict

    def delete(self):
        """ Deletes this BaseModel instance from the storage"""
        models.storage.delete(self)
