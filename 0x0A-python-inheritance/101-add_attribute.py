#!/usr/bin/python3
"""
    File name 101-add_attribute:contain add_attribute()
"""


def add_attribute(cls, name, value):
    """
        adds a new attribute if possible
    """
    if hasattr(cls, "__dict__") is False:
        raise TypeError("can't add new attribute")
    setattr(cls, name, value)
