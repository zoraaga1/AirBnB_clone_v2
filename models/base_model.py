#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import models
import uuid
from uuid import uuid4
from datetime import datetime
import os
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, DateTime, String


Base = declarative_base()

class BaseModel:
    """A base class for all hbnb models"""
    id = Column(String(60), unique=True, nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    
    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        updated_set = flag_created_at = False
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at":
                    flag_created_at = True
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    updated_set = True
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
        if not flag_created_at:
            self.created_at = datetime.now()
        if not updated_set:
            self.updated_at = datetime.now()
        self.id = str(uuid.uuid4())

    def __str__(self):
        """Returns a string representation of the instance"""
        return '[{}] ({}) {}'.format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        new_dict = {key: value for key, value in dict(
            self.__dict__).items() if key != "_sa_instance_state"}
        new_dict["__class__"] = str(type(self).__name__)
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict

    def delete(self):
        """Delete the current instance from storage"""
        models.storage.delete(self)
