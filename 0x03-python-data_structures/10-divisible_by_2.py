#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    result = []  # Initialize an empty list to store the results
    
    for num in my_list:
        result.append(num % 2 == 0)
        # Check if the number is divisible by 2 and append the result
    
    return result
