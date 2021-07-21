# merge_sort_natural.py
# Kordel France
########################################################################################################################
# This file provides functions to sort an array of integers in ascending order using the natural merge sort algorithm.
########################################################################################################################
# NOTE: Source 3 was leveraged to figure out whether or not the number of comparisons should be incremented while
#  identifying the number of runs.

import time

M1X_COMP = 0
M1X_EX = 0

'''
The signature of the merge() method differs from the example above as follows:

Instead of subarrays, the entire original array and the positions of the areas to be merged are passed to the method.
Instead of returning a new array, the target array is also passed to the method for being populated.
'''


def merge_sort_natural(data_arr):
    """
    Driver for implementing the natural merge sort algorithm.
    :param data_arr: the array to split and merge sort from.
    ;return data_arr: the sorted array.
    ;return M1X_COMP: number of comparisons performed
    ;return M1X_EX: number of exchanges performed
    ;return time: The time it takes for the algorithm to sort the file.
    """
    start_time = time.time()
    global M1X_COMP
    global M1X_EX

    begin_length = len(data_arr)
    length = len(data_arr)
    temp_arr = [0] * length
    pntr_array = [0] * (length + 1)

    # 1 - identify runs
    runs = 0
    pntr_array[0] = 0
    for i in range(1, length + 1):
        if (i == length) or (data_arr[i] < data_arr[i - 1]):
            runs += 1
            pntr_array[runs] = i
            M1X_COMP += 1
        # endif
    # endloop

    # 2 - merge runs until only 1 run is left
    tx_arr = data_arr
    rx_arr = temp_arr

    while (runs > 1):
        new_runs = 0
        # merge 2 runs together
        for i in range(0, runs - 1, 2):
            merge_natural(tx_arr, rx_arr, pntr_array[i], pntr_array[i + 1], pntr_array[i + 2])      ### RECURSIVE CALL
            pntr_array[new_runs] = pntr_array[i]
            new_runs += 1
        # endif

        # if there was an odd number of runs, copy the last one
        if (runs % 2 == 1):
            last_start = pntr_array[runs - 1]
            for j in range(last_start, length):
                rx_arr.append(tx_arr[i])
            pntr_array[new_runs] = last_start
            new_runs += 1
        # endif

        pntr_array[new_runs] = length
        runs = new_runs

        swap_arr = tx_arr
        tx_arr = rx_arr
        rx_arr = swap_arr
    # endloop

    # copy run if final run is not in data array
    for i in range(0, length):
        data_arr[i] = tx_arr[i]
    # endloop

    end_time = time.time()
    delta_time = end_time - start_time
    return data_arr, M1X_COMP, M1X_EX, "{:.6f}".format(delta_time)


def merge_natural(tx_arr, rx_arr, left_idx, right_idx, end_pos):
    """
    Function for finding both middle indices needed for the three-way merge sort.
    :param tx_arr: the array to split and merge sort from - transmitting (tx) array.
    :param rx_arr: the array to merge to - receiving (rx) array.
    :param left_idx: the low pointer for traversal.
    :param right_idx: the high pointer for traversal.
    :param end_pos: the end pointer for traversal.
    """
    global M1X_COMP
    global M1X_EX

    left_pos = left_idx
    right_pos = right_idx
    pointer_pos = left_idx

    # traverse array as long as both arrays contain elements to traverse
    while (left_pos < right_idx) and (right_pos < end_pos):
        left_val = tx_arr[left_pos]
        right_val = tx_arr[right_pos]
        if (left_val <= right_val):
            rx_arr[pointer_pos] = left_val
            pointer_pos += 1
            left_pos += 1
            M1X_COMP += 1
            M1X_EX += 1
        else:
            rx_arr[pointer_pos] = right_val
            pointer_pos += 1
            right_pos += 1
            M1X_COMP += 1
            M1X_EX += 1
        # endif
    # endloop

    # copy the rest
    while (left_pos < right_idx):
        rx_arr[pointer_pos] = tx_arr[left_pos]
        pointer_pos += 1
        left_pos += 1
        M1X_COMP += 1
        M1X_EX += 1
    # endloop

    while (right_pos < end_pos):
        rx_arr[pointer_pos] = tx_arr[right_pos]
        pointer_pos += 1
        right_pos += 1
        M1X_COMP += 1
        M1X_EX += 1
    # endloop



def reset_counts_merge_sort_natural():
    """
    Resets the comparisons and exchanges counters so they are initialized for a new sort.
    """
    # reset comparison and exchange counts for next run
    global M1X_COMP
    global M1X_EX
    M1X_COMP = 0
    M1X_EX = 0

