#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:  # Check if the list is empty
        return None

    max_value = my_list[0]  # Assume the first element as the maximum

    for num in my_list:
        if num > max_value:
            max_value = num

    return max_value
