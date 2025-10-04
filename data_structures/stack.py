"""
This module provides a simple implementation of a stack data structure using Python classes.
The stack follows the Last-In-First-Out (LIFO) principle and supports common operations such as:

- push: Add an item to the top of the stack
- pop: Remove and return the top item
- peek: View the top item without removing it
- is_empty: Check if the stack is empty
- size: Get the number of items in the stack

The Stack class is designed to be reusable and easy to integrate into larger applications.
It includes error handling for empty stack operations and a string representation for debugging.

Example usage:
    stack = Stack()
    stack.push(1)
    stack.push(2)
    print(stack.pop())  # Output: 2

Author: Vaibhav Kulshrestha
Date: 10/04/2025
"""

class Stack:
    """
    A class representing a stack data structure (LIFO - Last In, First Out).
    """

    def __init__(self):
        """
        Initialize an empty stack.
        """
        self._items = []

    def push(self, item):
        """
        Add an item to the top of the stack.

        Parameters:
        item: The item to be added to the stack.
        """
        self._items.append(item)

    def pop(self):
        """
        Remove and return the top item of the stack.

        Returns:
        The item at the top of the stack.

        Raises:
        IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self):
        """
        Return the top item of the stack without removing it.

        Returns:
        The item at the top of the stack.

        Raises:
        IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._items[-1]

    def is_empty(self):
        """
        Check if the stack is empty.

        Returns:
        True if the stack is empty, False otherwise.
        """
        return len(self._items) == 0

    def size(self):
        """
        Return the number of items in the stack.

        Returns:
        The size of the stack.
        """
        return len(self._items)

    def __str__(self):
        """
        Return a string representation of the stack.

        Returns:
        A string showing the stack from bottom to top.
        """
        return f"Stack (bottom -> top): {str(self._items)}"


if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print(stack)             # Stack (bottom -> top): [10, 20, 30]
    print(stack.peek())      # 30
    print(stack.pop())       # 30
    print(stack.size())      # 2
    print(stack.is_empty())  # False
