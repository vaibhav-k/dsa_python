"""
This module provides a simple implementation of a queue data structure using Python classes.
The queue follows the First-In-First-Out (FIFO) principle and supports common operations such as:

- enqueue: Add an item to the rear of the queue
- dequeue: Remove and return the front item
- peek: View the front item without removing it
- is_empty: Check if the queue is empty
- size: Get the number of items in the queue

The Queue class is designed to be reusable and easy to integrate into larger applications.
It includes error handling for empty queue operations and a string representation for debugging.

Example usage:
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    print(queue.dequeue())  # Output: 1

Author: Vaibhav Kulshrestha
Date: 10/04/2025
"""

class Queue:
    """
    A class representing a queue data structure (FIFO - First In, First Out).
    """

    def __init__(self):
        """
        Initialize an empty queue.
        """
        self._items = []

    def enqueue(self, item):
        """
        Add an item to the rear of the queue.

        Parameters:
        item: The item to be added to the queue.
        """
        self._items.append(item)

    def dequeue(self):
        """
        Remove and return the front item of the queue.

        Returns:
        The item at the front of the queue.

        Raises:
        IndexError: If the queue is empty.
        """
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._items.pop(0)

    def peek(self):
        """
        Return the front item of the queue without removing it.

        Returns:
        The item at the front of the queue.

        Raises:
        IndexError: If the queue is empty.
        """
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self._items[0]

    def is_empty(self):
        """
        Check if the queue is empty.

        Returns:
        True if the queue is empty, False otherwise.
        """
        return len(self._items) == 0

    def size(self):
        """
        Return the number of items in the queue.

        Returns:
        The size of the queue.
        """
        return len(self._items)

    def __str__(self):
        """
        Return a string representation of the queue.

        Returns:
        A string showing the queue from front to rear.
        """
        return f"Queue (front -> rear): {str(self._items)}"


if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    print(queue)             # Queue (front -> rear): [10, 20, 30]
    print(queue.peek())      # 10
    print(queue.dequeue())   # 10
    print(queue.size())      # 2
    print(queue.is_empty())  # False
