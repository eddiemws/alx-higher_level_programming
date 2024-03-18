#!/usr/bin/python3
# 5-no_c.py

def no_c(my_string):
    """Remove all chars c and C from a str."""
    copy = [x for x in my_string if x != 'c' and x != 'C']
    return ("".join(copy))
