#!/usr/bin/python3
"""Defines the City class."""
from models.base_model import BaseModel


class City(BaseModel):
    """Represents a city.

    Attributes:
        state_id (str): The ID of the state that the city belongs to.
        name (str): The name of the city.
    """

    def __init__(self, *args, **kwargs):
        """Initializes a new City instance.

        Args:
            *args: Unused.
            **kwargs: Key/value pairs of attributes.
        """
        super().__init__(*args, **kwargs)

    state_id = ""
    name = ""
