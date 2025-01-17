#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
import models
from models.amenity import Amenity
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from os import getenv
""" Add a conditional depending of the value of the environment variable
HBNB_TYPE_STORAGE:
If equal to db:
Import DBStorage class in this file
Create an instance of DBStorage and store it in the variable storage (the line
storage.reload() should be executed after this instantiation)
Else:
Import FileStorage class in this file
Create an instance of FileStorage and store it in the variable storage (the
line storage.reload() should be executed after this instantiation) """

if getenv('HBNB_TYPE_STORAGE') == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()
