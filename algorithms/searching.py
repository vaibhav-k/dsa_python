"""
algorithms.searching
====================

This module provides implementations of common searching algorithms.

Algorithms included:
- Linear Search
- Binary Search
- Jump Search
- Exponential Search
- Interpolation Search

Functions:
    linear_search(arr, target): Searches for a target value in an array using linear search.
    binary_search(arr, target): Searches for a target value in a sorted array using binary search.
    jump_search(arr, target): Searches for a target value in a sorted array using jump search.
    exponential_search(arr, target): Searches for a target value in a sorted array using exponential search.
    interpolation_search(arr, target): Searches for a target value in a sorted array using interpolation search.

Author:
    Vaibhav Kulshrestha

Date:
    2025-10-17
"""


def linear_search(arr, target):
    """
    Searches for a target value in an array using linear search.

    Args:
        arr (list): The list of elements to search.
        target: The value to search for.

    Returns:
        int: The index of the target if found, otherwise -1.
    """
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1


def binary_search(arr, target):
    """
    Searches for a target value in a sorted array using binary search.

    Args:
        arr (list): The sorted list of elements to search.
        target: The value to search for.

    Returns:
        int: The index of the target if found, otherwise -1.
    """
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def jump_search(arr, target):
    """
    Searches for a target value in a sorted array using jump search.

    Args:
        arr (list): The sorted list of elements to search.
        target: The value to search for.

    Returns:
        int: The index of the target if found, otherwise -1.
    """
    from math import sqrt

    n = len(arr)
    if n == 0:
        return -1
    step = int(sqrt(n))
    prev = 0

    # Find the block where the element may be present
    while prev < n and arr[min(step, n) - 1] < target:
        prev = step
        step += int(sqrt(n))
        if prev >= n:
            return -1

    # Linear search within the block
    for i in range(prev, min(step, n)):
        if arr[i] == target:
            return i
    return -1


def exponential_search(arr, target):
    """
    Searches for a target value in a sorted array using exponential search.

    Args:
        arr (list): The sorted list of elements to search.
        target: The value to search for.

    Returns:
        int: The index of the target if found, otherwise -1.
    """
    if len(arr) == 0:
        return -1
    if arr[0] == target:
        return 0

    index = 1
    while index < len(arr) and arr[index] <= target:
        index *= 2

    # Call binary search for the found range
    left = index // 2
    right = min(index, len(arr) - 1)
    return (
        binary_search(arr[left : right + 1], target) + left
        if binary_search(arr[left : right + 1], target) != -1
        else -1
    )


def interpolation_search(arr, target):
    """
    Searches for a target value in a sorted array using interpolation search.

    Args:
        arr (list): The sorted list of elements to search.
        target: The value to search for.

    Returns:
        int: The index of the target if found, otherwise -1.
    """
    low = 0
    high = len(arr) - 1

    while low <= high and arr[low] <= target <= arr[high]:
        if low == high:
            if arr[low] == target:
                return low
            return -1

        # Estimate the position
        pos = low + ((target - arr[low]) * (high - low) // (arr[high] - arr[low]))

        if arr[pos] == target:
            return pos
        if arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1

    return -1


def main():
    arr = [10, 20, 30, 40, 50, 60, 70, 80, 90]
    target = 70

    print("Linear Search:", linear_search(arr, target))
    print("Binary Search:", binary_search(arr, target))
    print("Jump Search:", jump_search(arr, target))
    print("Exponential Search:", exponential_search(arr, target))
    print("Interpolation Search:", interpolation_search(arr, target))


if __name__ == "__main__":
    main()
