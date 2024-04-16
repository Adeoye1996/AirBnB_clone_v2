#!/usr/bin/python3
"""create a unique storage instance for the application"""
from os import getenv
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage

# Import all necessary models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

# Determine the type of storage based on environment variable
if getenv("HBNB_TYPE_STORAGE") == "db":
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()
