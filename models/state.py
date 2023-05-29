#!/usr/bin/python3
"""
This module defines the State class, which represents a state.
"""

from models.base_model import BaseModel


class State(BaseModel):
    """
    A class used to represent a state.

    Attributes
    ----------
    name : str
        the name of the state
    """
    name = ""
