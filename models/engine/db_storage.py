#!/usr/bin/python3
"""Defines the DBStorage engine."""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.base_model import Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.amenity import Amenity


classes = {"User": User, "State": State, "City": City,
           "Amenity": Amenity, "Place": Place, "Review": Review}


class DBStorage:
    """Defines DBStorage class"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialize DBStorage"""
        user = getenv('HBNB_MYSQL_USER')
        password = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')
        env = getenv('HBNB_ENV')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, password, host, db),
                                      pool_pre_ping=True)

        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on the curr db session"""

        dict = {}
        for c_ls in classes:
            if cls is None or cls is classes[c_ls] or cls is c_ls:
                objs = self.__session.query(classes[c_ls]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    dict[key] = obj
        return dict

    def new(self, obj):
        """Add the object to the curr db session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the curr db session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the curr db session obj if not None"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the db
        and create the current db session"""

        Base.metadata.create_all(self.__engine)
        db_session = scoped_session(sessionmaker(bind=self.__engine, expire_on_commit=False))  # noqa
        self.__session = db_session()

    def close(self):
        """Closes the working SQLAlchemy session"""
        self.__session.close()
