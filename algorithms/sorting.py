"""
algorithms.sorting
==================

This module implements and demonstrates various sorting algorithms.

Each algorithm sorts a list in place, meaning the original list is modified rather
than returning a new sorted list. These algorithms are implemented for educational
purposes, showcasing different sorting techniques and their logic.

Included Algorithms:
--------------------
- Bubble Sort
- Selection Sort
- Insertion Sort
- Merge Sort
- Quick Sort
- Heap Sort

Each algorithm handles improper comparisons (e.g., sorting numbers and strings together)
by using `try-except` blocks, raising a `ValueError` when types cannot be compared.

Author:
    Vaibhav Kulshrestha
Date:
    2025-11-03
"""


def bubble_sort(arr):
    """
    Sorts an array in place using the Bubble Sort algorithm.

    Algorithm Overview:
        - Repeatedly traverse the list.
        - Compare adjacent elements.
        - Swap them if they are in the wrong order.
        - Largest elements "bubble up" to the end with each pass.

    Time Complexity: O(n²)
    Space Complexity: O(1)

    Args:
        arr (list): The list of elements to sort.

    Raises:
        ValueError: If any elements in `arr` are not comparable.

    Returns:
        None
    """
    if not arr or len(arr) < 2:
        return None  # No sorting needed

    # Outer loop controls number of passes
    for i in range(len(arr)):
        # Inner loop compares adjacent elements
        for j in range(0, len(arr) - i - 1):
            try:
                # Swap if the next element is smaller
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
            except TypeError:
                raise ValueError("Elements in the array must be of comparable types.")
    return None


def selection_sort(arr):
    """
    Sorts an array in place using the Selection Sort algorithm.

    Algorithm Overview:
        - Divide the list into two parts: sorted and unsorted.
        - Repeatedly find the smallest element from the unsorted part.
        - Swap it into the correct position in the sorted part.

    Time Complexity: O(n²)
    Space Complexity: O(1)

    Args:
        arr (list): The list of elements to sort.

    Raises:
        ValueError: If elements in `arr` are not comparable.

    Returns:
        None
    """
    if not arr or len(arr) < 2:
        return None

    n = len(arr)

    for i in range(n):
        min_idx = i  # Assume current position has the smallest value
        for j in range(i + 1, n):
            try:
                # If a smaller element is found, update min index
                if arr[j] < arr[min_idx]:
                    min_idx = j
            except TypeError:
                raise ValueError("Elements in the array must be of comparable types.")
        # Swap minimum element into the correct position
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return None


def insertion_sort(arr):
    """
    Sorts an array in place using the Insertion Sort algorithm.

    Algorithm Overview:
        - Builds a sorted section one element at a time.
        - Takes the next unsorted element and inserts it at the correct position.

    Time Complexity:
        - Average/Worst: O(n²)
        - Best (already sorted): O(n)

    Space Complexity: O(1)

    Args:
        arr (list): The list of elements to sort.

    Raises:
        ValueError: If elements in `arr` are not comparable.

    Returns:
        None
    """
    if not arr or len(arr) < 2:
        return None

    for i in range(1, len(arr)):
        key = arr[i]  # Current element to be inserted
        j = i - 1  # Index of previous element

        try:
            # Move elements greater than key to one position ahead
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
        except TypeError:
            raise ValueError("Elements in the array must be of comparable types.")

        # Insert the key at its correct position
        arr[j + 1] = key
    return None


def merge_sort(arr):
    """
    Sorts an array in place using the Merge Sort algorithm.

    Algorithm Overview:
        - Divide the list into two halves.
        - Recursively sort each half.
        - Merge the two sorted halves into a single sorted list.

    Time Complexity: O(n log n)
    Space Complexity: O(n)  (due to temporary sublists)

    Args:
        arr (list): The list of elements to sort.

    Raises:
        ValueError: If elements in `arr` are not comparable.

    Returns:
        None
    """
    # Base case: arrays of length 0 or 1 are already sorted
    if len(arr) <= 1:
        return None

    # Split array into halves
    middle_index = len(arr) // 2
    left_subarr = arr[:middle_index]
    right_subarr = arr[middle_index:]

    # Recursively sort both halves
    merge_sort(left_subarr)
    merge_sort(right_subarr)

    # Merge process
    left_pointer = right_pointer = merged_pointer = 0

    # Merge the sorted subarrays back into the original array
    try:
        # Compare elements from both halves and merge
        while left_pointer < len(left_subarr) and right_pointer < len(right_subarr):
            if left_subarr[left_pointer] < right_subarr[right_pointer]:
                arr[merged_pointer] = left_subarr[left_pointer]
                left_pointer += 1
            else:
                arr[merged_pointer] = right_subarr[right_pointer]
                right_pointer += 1
            merged_pointer += 1

        # Copy remaining elements from left_subarr
        while left_pointer < len(left_subarr):
            arr[merged_pointer] = left_subarr[left_pointer]
            left_pointer += 1
            merged_pointer += 1

        # Copy remaining elements from right_subarr
        while right_pointer < len(right_subarr):
            arr[merged_pointer] = right_subarr[right_pointer]
            right_pointer += 1
            merged_pointer += 1
    except TypeError:
        raise ValueError("Elements in the array must be of comparable types.")

    return None


def quick_sort(arr):
    """
    Sorts an array in place using the Quick Sort algorithm.

    This implementation is **type-flexible** — it works with any elements
    that can be compared using `<` and `>` (e.g., int, float, str, custom
    objects that define comparison methods).

    Quick Sort is a divide-and-conquer algorithm that works by:
        1. Selecting a 'pivot' element.
        2. Partitioning the array into elements less than and greater than the pivot.
        3. Recursively sorting the sub-arrays.

    Average time complexity: O(n log n), but can degrade to O(n²) in the worst case
    (e.g., when the smallest or largest element is always chosen as the pivot).
    Space complexity: O(log n) due to recursion stack space.

    Args:
        arr (list): List of elements to be sorted.

    Raises:
        ValueError: If elements in `arr` are not comparable (e.g., mixing int and str).

    Returns:
        None: The function sorts the list in place.
    """
    # If list is empty or has one element, no sorting is needed
    if not arr or len(arr) < 2:
        return None

    # --- Helper Function: Partition the array around a pivot ---
    def _partition(array, low, high):
        """
        Rearranges elements in the array segment [low..high] around a pivot such that:
            - Elements smaller than the pivot are placed before it.
            - Elements larger than the pivot are placed after it.

        Returns:
            int: The final pivot index.
        """
        pivot = array[high]  # Choose the last element as pivot
        i = low - 1  # Index of the smaller element section

        for j in range(low, high):
            try:
                if array[j] < pivot:
                    i += 1
                    array[i], array[j] = array[j], array[i]
            except TypeError as e:
                raise ValueError(
                    f"Elements '{array[j]}' and '{pivot}' are not comparable:\n{e}"
                )

        # Place pivot in correct sorted position
        array[i + 1], array[high] = array[high], array[i + 1]
        return i + 1

    # --- Helper Function: Recursive Quick Sort ---
    def _quick_sort_helper(array, low, high):
        """
        Recursively applies Quick Sort to partitions of the array.
        Uses tail recursion optimization (sort smaller side first)
        to minimize recursion depth.
        """
        while low < high:
            # Partition and get pivot index
            pivot_index = _partition(array, low, high)

            # Sort the smaller partition first (reduces recursion depth)
            if pivot_index - low < high - pivot_index:
                _quick_sort_helper(array, low, pivot_index - 1)
                low = pivot_index + 1
            else:
                _quick_sort_helper(array, pivot_index + 1, high)
                high = pivot_index - 1

    _quick_sort_helper(arr, 0, len(arr) - 1)
    return None


def heap_sort(arr):
    """
    Sorts an array in place using the Heap Sort algorithm.

    Algorithm Overview:
        - Build a max heap from the input list.
        - Repeatedly swap the root (max element) with the last element.
        - Reduce the heap size and heapify again.

    Time Complexity: O(n log n)
    Space Complexity: O(1)

    Args:
        arr (list): The list of elements to sort.

    Returns:
        None
    """
    # If list is empty or has one element, no sorting is needed
    if not arr or len(arr) < 2:
        return None

    def _heapify(arr, n, i):
        """Ensures the heap property for a node `i` within array size `n`."""
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        # Compare node with left and right children
        try:
            if left < n and arr[left] > arr[largest]:
                largest = left
            if right < n and arr[right] > arr[largest]:
                largest = right
        except TypeError:
            raise ValueError("Elements in the array must be of comparable types.")

        # If root is not largest, swap and heapify the affected subtree
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            _heapify(arr, n, largest)

    n = len(arr)

    # Step 1: Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        _heapify(arr, n, i)

    # Step 2: Extract elements from the heap one by one
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # Move current root to end
        _heapify(arr, i, 0)
    return None


def main():
    """
    Demonstrates all sorting algorithms using randomly generated arrays.

    For each sorting algorithm:
        - A random list of 10 integers (0–100) is created.
        - The unsorted and sorted lists are printed.

    Returns:
        None
    """
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
