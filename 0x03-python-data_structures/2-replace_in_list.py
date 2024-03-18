#!/usr/bin/python3
def replace_in_list(my_lis, idx, element):
    if idx < 0 or idx >= len(my_lis):
        return my_lis
    else:
        my_lis[idx] = element
        return my_lis
