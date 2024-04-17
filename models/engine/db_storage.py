#!/usr/bin/python3
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.base_model import BaseModel

from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

import os
from sqlalchemy import MetaData

class DBStorage():
    __engine = None
    __session = None

    def __init__(self):
        user = os.getenv('HBNB_MYSQL_USER')
        pwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST', default='localhost')
        db = os.getenv('HBNB_MYSQL_DB')
        env = os.getenv('HBNB_ENV')

        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(user, pwd, host, db),
            pool_pre_ping=True
        )

        if env == 'test':
            Base.metadata.drop_all(self.__engine)

        Session = scoped_session(sessionmaker(bind=self.__engine, expire_on_commit=False))
        self.__session = Session()

    def all(self, cls=None):
        classes = [cls] if cls else [State, City, User, Place, Review, Amenity]
        objects = {}
        for c in classes:
            for obj in self.__session.query(c):
                key = "{}.{}".format(obj.__class__.__name__, obj.id)
                objects[key] = obj
        return objects

    def new(self, obj):
        """Add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete obj from the current database session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database and create the current database session"""
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(bind=self.__engine, expire_on_commit=False))
        self.__session = Session()
