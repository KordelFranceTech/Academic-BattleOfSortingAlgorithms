# file_manager.py
# Kordel France
########################################################################################################################
# This file provides public-accessible functions to generate a sorted, reverse-sorted, or random data stream.
# Each function returns an array of it's designated sorting distribution.
# Let it be emphasized that all data is automatically generated.
########################################################################################################################

import random

def generate_sorted_file(length) -> [int]:
    """
    Generates an array of integers sorted in ascending order.
    :param length: the length of the array to generate.
    ;return: sorted_arr: the generated array of integers listed in ascending order.
    """
    initVal = 1000
    sorted_arr = []
    for i in range(0, length):
        sorted_arr.append(int(initVal + i))
    return sorted_arr


def generate_reverse_sorted_file(length) -> [int]:
    """
    Generates an array of integers sorted in descending (reverse ascending) order.
    :param length: the length of the array to generate.
    ;return: sorted_arr: the generated array of integers listed in descending order.
    """
    sorted_arr = generate_sorted_file(length)
    unsorted_arr = []
    for i in range(0, len(sorted_arr)):
        unsorted_arr.append(sorted_arr.pop())
    return unsorted_arr


def generate_random_sorted_file(length) -> [int]:
    """
    Generates an array list of random integers.
    Performs a first-order check on uniqueness of each number generated to limit number of duplicates in returned array.
    :param length: the length of the array to generate.
    ;return rand_arr: the generated array of 'randomly' selected integers.
    """
    minVal = 1000
    maxVal = 9999
    rand_arr = []
    for i in range(1, length + 1):
        rand_int = random.randint(minVal, maxVal)
        unique_int = check_randomness(rand_int, rand_arr)
        rand_arr.append(unique_int)
        # rand_arr.append(rand_int + int(int(rand_int) // int(i)))
    return rand_arr


def check_randomness(val, data_arr):
    """
    Performs a check for the random number, val, to ensure it isn't already in the array, data_arr.
    If it is in the array, it is altered by another randomly generated number.
    :param val: the value to check for duplicates of.
    ;return rand_arr: the generated array of 'randomly' selected integers.
    """
    if val in data_arr:
        rand_int = random.randint(2, len(data_arr))
        # while val in data_arr:
        #     val += (val // rand_int)
        val += (val // rand_int)
    return val


