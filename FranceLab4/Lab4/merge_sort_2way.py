# merge_sort_2way.py
# Kordel France
########################################################################################################################
# This file provides functions to sort an array of integers in ascending order using a two-way merge sort.
########################################################################################################################

import time

M2X_COMP = 0
M2X_EX = 0

def merge_sort_two_way(data_arr):
    """
    Driver for implementing merge sort from two sub-arrays.
    :param data_arr: the array to split and merge sort from.
    ;return data_arr: the sorted array.
    ;return M2X_COMP: number of comparisons performed
    ;return M2X_EX: number of exchanges performed
    ;return time: The time it takes for the algorithm to sort the file.
    """
    start_time = time.time()
    global M2X_COMP
    global M2X_EX

    if len(data_arr) > 1:
        # finding the mid of the array
        mid = len(data_arr) // 2
        # dividing the array elements
        left_half = data_arr[:mid]

        # into 2 halves
        right_half = data_arr[mid:]

        # sorting the first half
        merge_sort_two_way(left_half)                                                       ### RECURSIVE CALL

        # sorting the second half
        merge_sort_two_way(right_half)                                                      ### RECURSIVE CALL

        i = j = k = 0

        # copy data to temp arrays L[] and R[]
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                data_arr[k] = left_half[i]
                i += 1
                M2X_COMP += 1
                M2X_EX += 1
            else:
                data_arr[k] = right_half[j]
                j += 1
                M2X_COMP += 1
                M2X_EX += 1
            k += 1

        # checking if any element was left
        while i < len(left_half):
            data_arr[k] = left_half[i]
            i += 1
            k += 1

        # checking if any element was right
        while j < len(right_half):
            data_arr[k] = right_half[j]
            j += 1
            k += 1
    end_time = time.time()
    delta_time = end_time - start_time
    return data_arr, M2X_COMP, M2X_EX, "{:.6f}".format(delta_time)


def reset_counts_merge_sort_two_way():
    """
    Resets the comparisons and exchanges counters so they are initialized for a new sort.
    """
    # reset comparison and exchange counts for next run
    global M2X_COMP
    global M2X_EX
    M2X_COMP = 0
    M2X_EX = 0

