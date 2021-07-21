# heap_sort.py
# Kordel France
########################################################################################################################
# This file provides functions to construct a heap from a passed array (list) argument and sort it in ascending order.
########################################################################################################################
import time

H_COMP = 0
H_EX = 0


def construct_heap(data_arr, length, index):
    """
    Performs the first step in heap sort - building the heap.
    This is a recursive call.
    :param length: the length of the heap array.
    :param index: the current index of the pointer.
    """
    global H_COMP
    global H_EX
    # initialize root and left & right children
    root = index
    left_heap = 2 * index + 1
    right_heap = 2 * index + 2

    # if left child of root exists and greater than largest element (root)
    if left_heap < length and data_arr[root] < data_arr[left_heap]:
        root = left_heap
        H_COMP += 2
        H_EX += 1

    # if right child of root exists and greater than largest element (root)
    if right_heap < length and data_arr[root] < data_arr[right_heap]:
        root = right_heap
        H_COMP += 2
        H_EX += 1

    # if the above results in a root change, do it
    if root != index:
        data_arr[index], data_arr[root] = data_arr[root], data_arr[index]
        # continue to build heap so long as the array is not empty
        construct_heap(data_arr, length, root)                                                  ### RECURSIVE CALL
        H_EX += 1


def heap_sort(data_arr):
    """
    Driver for the second step in heap sort - sort the constructed heap.
    :param data_arr: the array to create the sorted heap from.
    ;return: data_arr: the array as a sorted heap that has been traversed into an array.
    ;return H_COMP: number of comparisons performed
    ;return H_EX: number of exchanges performed'
    ;return time: The time it takes for the algorithm to sort the file.
    """
    start_time = time.time()
    length = len(data_arr)
    # construct the max heap
    for i in range((length // 2) - 1, -1, -1):
        # add the next value to the heap
        construct_heap(data_arr, length, i)

    # traverse through heap to build list
    for j in range((length - 1), 0, -1):
        # interchange indices
        data_arr[j], data_arr[0] = data_arr[0], data_arr[j]
        # get the next value from the heap
        construct_heap(data_arr, j, 0)
    # return data_arr
    end_time = time.time()
    delta_time = end_time - start_time
    return data_arr, H_COMP, H_EX, "{:.6f}".format(delta_time)


def reset_counts_heap_sort():
    """
    Resets the comparisons and exchanges counters so they are initialized for a new sort.
    """
    # reset comparison and exchange counts for next run
    global H_COMP
    global H_EX
    H_COMP = 0
    H_EX = 0


