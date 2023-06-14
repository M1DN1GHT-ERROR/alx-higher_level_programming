#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    diff_set = set_1 ^ set_2  # Symmetric difference of set_1 and set_2
    return diff_set
