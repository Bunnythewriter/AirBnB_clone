#!/usr/bin/python3
"""Defines the Review class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represent a review.

    Attributes:
        place_id (str): The id associated with the place.
        user_id (str): The User id.
        text (str): The text review of the place.
    """

    place_id = ""
    user_id = ""
    text = ""
