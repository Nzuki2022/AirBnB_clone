#!/usr/bin/python3
"""
This code defines the "Amenity" class, which represents an amenity.
"""

# Import the "BaseModel" class from the "models.base_model" module.
from models.base_model import BaseModel


# Define the "Amenity" class, which inherits from "BaseModel".
class Amenity(BaseModel):
    """
    Represents an amenity.

    Attributes:
        name (str): The amenity's name.
    """
    name = ""
