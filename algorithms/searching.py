"""
algorithms.searching
====================

This module provides implementations of common searching algorithms
with robust error handling and inline documentation.

Each function includes detailed docstrings explaining the algorithm,
its time and space complexity, and usage examples.

Included Algorithms:
--------------------
- Linear Search
- Binary Search
- Jump Search
- Exponential Search
- Interpolation Search

Author:
    Vaibhav Kulshrestha

Date:
    2025-11-03
"""

from math import sqrt


def linear_search(arr, target):
    """
    Performs a Linear Search for the target in the given array.

    Algorithm:
        - Traverse the list sequentially.
        - Compare each element with the target until found.

    Time Complexity: O(n)
    Space Complexity: O(1)

    Args:
        arr (list): The list of elements to search.
        target: The value to search for.

    Returns:
        int: The index of the target if found, otherwise -1.
    """
    for index, value in enumerate(arr):
        try:
            if value == target:  # Direct equality check
                return index
        except Exception as e:
            # Handles cases like comparing incompatible types
            raise ValueError(f"Comparison failed between {value} and {target}: {e}")
    return -1


def binary_search(arr, target):
    """
    Performs a Binary Search for the target in a sorted array.

    Algorithm:
        - Repeatedly divide the search interval in half.
        - Compare the middle element with the target.

    Time Complexity: O(log n)
    Space Complexity: O(1)

    Args:
        arr (list): A sorted list of elements.
        target: The value to search for.

    Returns:
        int: The index of the target if found, otherwise -1.
    """
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        try:
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        except Exception as e:
            raise ValueError(f"Comparison failed at index {mid}: {e}")
    return -1


def jump_search(arr, target):
    """
    Performs a Jump Search for the target in a sorted array.

    Algorithm:
        - Jump ahead by fixed steps (sqrt(n)) until the target is possibly found.
        - Then perform linear search in that block.

    Time Complexity: O(√n)
    Space Complexity: O(1)

    Args:
        arr (list): A sorted list of elements.
        target: The value to search for.

    Returns:
        int: The index of the target if found, otherwise -1.
    """
    n = len(arr)
    if n == 0:
        return -1

    step = int(sqrt(n))
    prev = 0

    # Jump through the array to find a block that might contain the target
    while prev < n:
        try:
            if arr[min(step, n) - 1] >= target:
                break
        except Exception as e:
            raise ValueError(f"Comparison failed at jump index {min(step, n) - 1}: {e}")
        prev = step
        step += int(sqrt(n))
        if prev >= n:
            return -1

    # Linear search within the block
    for i in range(prev, min(step, n)):
        try:
            if arr[i] == target:
                return i
        except Exception as e:
            raise ValueError(f"Comparison failed at index {i}: {e}")
    return -1


def exponential_search(arr, target):
    """
    Performs an Exponential Search for the target in a sorted array.

    Algorithm:
        - Find a range where the target might exist by doubling the index.
        - Then perform Binary Search within that range.

    Time Complexity: O(log n)
    Space Complexity: O(1)

    Args:
        arr (list): A sorted list of elements.
        target: The value to search for.

    Returns:
        int: The index of the target if found, otherwise -1.
    """
    n = len(arr)
    if n == 0:
        return -1

    # Check the first element
    try:
        if arr[0] == target:
            return 0
    except Exception as e:
        raise ValueError(f"Comparison failed at index 0: {e}")

    # Find the range by exponential growth
    index = 1
    while index < n:
        try:
            if arr[index] > target:
                break
        except Exception as e:
            raise ValueError(f"Comparison failed at index {index}: {e}")
        index *= 2

    # Define the range for binary search
    left = index // 2
    right = min(index, n - 1)

    # Perform binary search on the range
    result = binary_search(arr[left : right + 1], target)
    return left + result if result != -1 else -1


def interpolation_search(arr, target):
    """
    Performs an Interpolation Search for the target in a sorted, uniformly distributed array.

    Algorithm:
        - Estimate the position of the target based on its value.
        - Adjust the search range based on the estimated position.

    Time Complexity: O(log log n) on average, O(n) in worst case.
    Space Complexity: O(1)

    Args:
        arr (list): A sorted list of uniformly distributed numeric elements.
        target: The value to search for.

    Returns:
        int: The index of the target if found, otherwise -1.
    """
    low = 0
    high = len(arr) - 1

    while low <= high:
        try:
            # Avoid division by zero and ensure target is within range
            if arr[low] == arr[high]:
                if arr[low] == target:
                    return low
                return -1

            # Estimate probable position
            pos = low + int(
                ((target - arr[low]) * (high - low)) / (arr[high] - arr[low])
            )
        except Exception as e:
            raise ValueError(f"Failed to estimate position due to type mismatch: {e}")

        # Ensure the position is within bounds
        if pos < 0 or pos >= len(arr):
            return -1

        try:
            if arr[pos] == target:
                return pos
            elif arr[pos] < target:
                low = pos + 1
            else:
                high = pos - 1
        except Exception as e:
            raise ValueError(f"Comparison failed at index {pos}: {e}")

    return -1


def main():
    """
    Demonstrates usage of all search algorithms with example data.
    """
    arr = [10, 20, 30, 40, 50, 60, 70, 80, 90]
    target = 70

    print("Linear Search:", linear_search(arr, target))
    print("Binary Search:", binary_search(arr, target))
    print("Jump Search:", jump_search(arr, target))
    print("Exponential Search:", exponential_search(arr, target))
    print("Interpolation Search:", interpolation_search(arr, target))


if __name__ == "__main__":
    main()
