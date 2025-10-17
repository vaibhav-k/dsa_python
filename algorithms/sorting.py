"""
algorithms.sorting
==================

This module contains implementations of various sorting algorithms.
Algorithms included:
- Bubble Sort
- Selection Sort
- Insertion Sort
- Merge Sort
- Quick Sort
- Heap Sort

Functions:
    bubble_sort(arr): Sorts an array using the bubble sort algorithm.
    selection_sort(arr): Sorts an array using the selection sort algorithm.
    insertion_sort(arr): Sorts an array using the insertion sort algorithm.
    merge_sort(arr): Sorts an array using the merge sort algorithm.
    quick_sort(arr): Sorts an array using the quick sort algorithm.
    heap_sort(arr): Sorts an array using the heap sort algorithm.

Author:
    Vaibhav Kulshrestha
Date:
    2025-10-17
"""


def bubble_sort(arr):
    """
    Sorts an array using the bubble sort algorithm.
    Args:
        arr (list): The list of elements to be sorted.

    Returns:
        None: The list is sorted in place.
    """
    if not arr or len(arr) < 2:
        return None
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return None


def selection_sort(arr):
    """
    Sorts an array using the selection sort algorithm.

    Args:
        arr (list): The list of elements to be sorted.

    Returns:
        None: The list is sorted in place.
    """
    if not arr or len(arr) < 2:
        return None
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
    return None


def insertion_sort(arr):
    """
    Sorts an array using the insertion sort algorithm.

    Args:
        arr (list): The list of elements to be sorted.

    Returns:
        None: The list is sorted in place.
    """
    if not arr or len(arr) < 2:
        return None
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return None


def merge_sort(arr):
    """
    Sorts an array using the merge sort algorithm in place.

    Args:
        arr (list): The list of elements to be sorted.

    Returns:
        None: The list is sorted in place.
    """
    if not arr or len(arr) < 2:
        return None
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    merge_sort(left)
    merge_sort(right)

    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1
    return None


def quick_sort(arr):
    """
    Sorts an array using the quick sort algorithm.

    Args:
        arr (list): The list of elements to be sorted.

    Returns:
        None: The list is sorted in place.
    """
    if not arr or len(arr) < 2:
        return None

    def _partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def _quick_sort_helper(arr, low, high):
        if low < high:
            pi = _partition(arr, low, high)
            _quick_sort_helper(arr, low, pi - 1)
            _quick_sort_helper(arr, pi + 1, high)

    _quick_sort_helper(arr, 0, len(arr) - 1)
    return None


def heap_sort(arr):
    """
    Sorts an array using the heap sort algorithm.

    Args:
        arr (list): The list of elements to be sorted.

    Returns:
        None: The list is sorted in place.
    """
    if not arr or len(arr) < 2:
        return None

    def _heapify(arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            _heapify(arr, n, largest)

    n = len(arr)
    # Build a maxheap
    for i in range(n // 2 - 1, -1, -1):
        _heapify(arr, n, i)
    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        _heapify(arr, i, 0)
    return None


def main():
    """Demonstrate the sorting algorithms."""
    from random import randint

    algorithms = [
        bubble_sort,
        selection_sort,
        insertion_sort,
        merge_sort,
        quick_sort,
        heap_sort,
    ]

    for sort_func in algorithms:
        arr = [randint(0, 100) for _ in range(10)]
        print(f"Original array for {sort_func.__name__}: {arr}")
        sort_func(arr)
        print(f"Sorted array: {arr}\n")


if __name__ == "__main__":
    main()
