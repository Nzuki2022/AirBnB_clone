#!/usr/bin/python3
"""
Initialize the models directory using the "__init__" magic method.
"""
# Import the "FileStorage" class from the "models.engine.file_storage" module.
from models.engine.file_storage import FileStorage

# Create a new instance of "FileStorage" named "storage".
storage = FileStorage()
storage.reload()
