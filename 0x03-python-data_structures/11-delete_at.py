#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):  # Check if the index is negative or out of range
        return my_list

    new_list = []  # Initialize a new list to store the updated list
    
    for i in range(len(my_list)):
        if i != idx:  # Exclude the item at the specified index
            new_list.append(my_list[i])
    
    return new_list
