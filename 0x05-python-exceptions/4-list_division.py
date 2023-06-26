#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):

    fresh_list = []
    for n in range(0, list_length):
        try:
            divides = my_list_1[n] / my_list_2[n]
        except TypeError:
            print("wrong type")
            divides = 0
        except ZeroDivisionError:
            print("division by 0")
            divides = 0
        except IndexError:
            print("out of range")
            divides = 0
        finally:
            fresh_list.append(divides)
    return (fresh_list)
