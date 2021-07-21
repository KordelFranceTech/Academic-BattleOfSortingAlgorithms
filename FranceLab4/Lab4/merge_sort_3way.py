# merge_sort_3way.py
# Kordel France
########################################################################################################################
# This file provides functions to sort an array of integers in ascending order using a three-way merge sort.
########################################################################################################################

import time

M3X_COMP = 0
M3X_EX = 0


def merge_three_way(tx_arr, low, mid1, mid2, high, rx_arr):
    """
    Function for merging three sub-arrays as a subfunction of a 3-way merge sort
    :param tx_arr: the array to split and merge sort from - transmitting (tx) array.
    :param low: the low pointer for the first subarray.
    :param mid1: the low mid pointer (divides first and second subarrays).
    :param mid2: the high mid pointer (divides second and third subarrays).
    :param high: the high pointer (end of third subarray).
    :param rx_arr: the array to merge to - receiving (rx) array.
    """
    global M3X_COMP
    global M3X_EX

    i = int(low)
    j = int(mid1)
    k = int(mid2)
    l = int(low)

    # choose smaller of the smallest in the three ranges
    while ((i < mid1) and (j < mid2) and (k < high)):
        if (tx_arr[i] < tx_arr[j]):
            M3X_COMP += 1
            if (tx_arr[i] < tx_arr[k]):
                rx_arr[l] = tx_arr[i]
                i += 1
                l += 1
                M3X_COMP += 1
                M3X_EX += 1
            else:
                rx_arr[l] = tx_arr[k]
                k += 1
                l += 1
                M3X_COMP += 1
                M3X_EX += 1
            # endif
        else:
            if (tx_arr[j] < tx_arr[k]):
                rx_arr[l] = tx_arr[j]
                l += 1
                j += 1
                M3X_COMP += 1
                M3X_EX += 1
            else:
                rx_arr[l] = tx_arr[k]
                k += 1
                l += 1
                M3X_COMP += 1
                M3X_EX += 1
            # endif
        # endif
    # endloop

    # case where first and second ranges have remaining values
    while ((i < mid1) and (j < mid2)):
        if (tx_arr[i] < tx_arr[j]):
            rx_arr[l] = tx_arr[i]
            i += 1
            l += 1
            M3X_COMP += 1
            M3X_EX += 1
        else:
            rx_arr[l] = tx_arr[j]
            l += 1
            j += 1
            M3X_COMP += 1
            M3X_EX += 1
        # endif
    # endloop

    # case where second and third ranges have remaining values
    while ((j < mid2) and (k < high)):
        if (tx_arr[j] < tx_arr[k]):
            rx_arr[l] = tx_arr[j]
            j += 1
            l += 1
            M3X_COMP += 1
            M3X_EX += 1
        else:
            # print(f'tx_arr: {tx_arr}')
            # print(f'rx_arr: {rx_arr}')
            # print(f'k: {k}\nl:{l}')
            rx_arr[l] = tx_arr[k]
            k += 1
            l += 1
            M3X_COMP += 1
            M3X_EX += 1
        # endif
    # endloop

    # case where first and third ranges have remaining values
    while ((i < mid1) and (k < high)):
        if (tx_arr[i] < tx_arr[k]):
            rx_arr[l] = tx_arr[i]
            i += 1
            l += 1
            M3X_COMP += 1
            M3X_EX += 1
        else:
            rx_arr[l] = tx_arr[k]
            k += 1
            l += 1
            M3X_COMP += 1
            M3X_EX += 1
        # endif
    # endloop

    # copy remaining values from first range
    while (i < mid1):
        rx_arr[l] = tx_arr[i]
        i += 1
        l += 1

    # copy remaining values from first range
    while (j < mid2):
        rx_arr[l] = tx_arr[j]
        j += 1
        l += 1

    # copy remaining values from first range
    while (k < high):
        rx_arr[l] = tx_arr[k]
        k += 1
        l += 1


def merge_sort_three_way_recursive_helper(tx_arr, low, high, rx_arr):
    """
    Function for finding both middle indices needed for the three-way merge sort.
    :param tx_arr: the array to split and merge sort from - transmitting (tx) array.
    :param low: the low pointer for the first subarray.
    :param high: the high pointer (end of third subarray).
    :param rx_arr: the array to merge to - receiving (rx) array.
    """
    if (high - low) < 2:
        return

    mid1 = low + int((high - low) / 3)
    mid2 = low + 2 * int((high - low) / 3) + 1

    # sort the 3 arrays recursively, calling separate recursive stack for each one
    merge_sort_three_way_recursive_helper(rx_arr, low, mid1, tx_arr)                                ### RECURSIVE CALL
    merge_sort_three_way_recursive_helper(rx_arr, mid1, mid2, tx_arr)                               ### RECURSIVE CALL
    merge_sort_three_way_recursive_helper(rx_arr, mid2, high, tx_arr)                               ### RECURSIVE CALL

    # arrays are sorted - now consolidate them in one final merge
    merge_three_way(rx_arr, low, mid1, mid2, high, tx_arr)


def merge_sort_three_way(tx_arr):
    """
    Driver for implementing merge sort from three sub-arrays.
    :param tx_arr: the array to split and merge sort from.
    ;return tx_arr: the sorted array.
    ;return M3X_COMP: number of comparisons performed
    ;return M3X_EX: number of exchanges performed
    ;return time: The time it takes for the algorithm to sort the file.
    """
    start_time = time.time()
    n = len(tx_arr)
    if (n == 0):
        return

    final_arr = [int] * n
    for i in range(0, n):
        final_arr[i] = tx_arr[i]
    merge_sort_three_way_recursive_helper(final_arr, 0, n, tx_arr)

    for i in range(0, n):
        tx_arr[i] = final_arr[i]

    end_time = time.time()
    delta_time = end_time - start_time
    return tx_arr, M3X_COMP, M3X_EX, "{:.6f}".format(delta_time)


def reset_counts_merge_sort_three_way():
    """
    Resets the comparisons and exchanges counters so they are initialized for a new sort.
    """
    # reset comparison and exchange counts for next run
    global M3X_COMP
    global M3X_EX
    M3X_COMP = 0
    M3X_EX = 0



