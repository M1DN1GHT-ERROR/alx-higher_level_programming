#!/usr/bin/python3
def uniq_add(my_list):
    unique_nums = set(my_list)  # Convert list to a set to remove duplicates
    sum_unique = sum(unique_nums)  # Calculate the sum of unique numbers
    return sum_unique
