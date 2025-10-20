"""
data_structures.stack
=====================

A simple implementation of a stack data structure (LIFO) for Python.

Features:
    - push(item): Add an item to the top of the stack.
    - pop(): Remove and return the top item.
    - peek(): View the top item without removing it.
    - is_empty(): Check if the stack is empty.
    - size(): Get the number of items in the stack.
    - clear(): Remove all items from the stack.
    - to_list(): Return a copy of the stack as a list.
    - from_list(lst): Create a stack from a list.
    - search(item): Return the 1-based position of an item from the top, or -1 if not found.
    - extend(iterable): Add multiple items to the top from an iterable.

Author:
    Vaibhav Kulshrestha

Date:
    2025-14-20
"""


class Stack:
    """
    A class representing a stack data structure (LIFO - Last In, First Out).

    Attributes:
        _items (list): Internal list to store stack items.
    """

    def __init__(self):
        """Initialize an empty stack."""
        self._items = []

    def __str__(self):
        """
        Return a string representation of the stack from top to bottom.

        Returns:
            str: Stack from top to bottom.
        """
        return f"Stack (top -> bottom): {self._items[::-1]}"

    def size(self):
        """
        Return the number of items in the stack.

        Returns:
            int: Size of the stack.
        """
        return len(self._items)

    def __len__(self):
        """Return the number of items in the stack."""
        return self.size()

    def __contains__(self, item):
        """
        Check if an item is in the stack.

        Args:
            item: The item to check for.

        Returns:
            bool: True if item is in the stack, False otherwise.
        """
        if not self._items:
            return False
        return item in self._items

    def __iter__(self):
        """Return an iterator over the stack from bottom to top."""
        return iter(self._items)

    def __getitem__(self, index):
        """
        Get an item by index from the stack.

        Args:
            index (int): Index of the item to retrieve.

        Returns:
            Any: The item at the specified index.

        Raises:
            IndexError: If the index is out of range.
        """
        if index < 0 or index >= self.size():
            raise IndexError("stack index out of range")
        return self._items[index]

    def __setitem__(self, index, value):
        """
        Set an item at a specific index in the stack.

        Args:
            index (int): Index to set.
            value: Value to set.

        Raises:
            IndexError: If the index is out of range.
        """
        if index < 0 or index >= self.size():
            raise IndexError("stack index out of range")
        self._items[index] = value

    def push(self, item):
        """
        Add an item to the top of the stack.

        Args:
            item: The item to be added.
        """
        self._items.append(item)

    def pop(self):
        """
        Remove and return the top item of the stack.

        Returns:
            Any: The item at the top.

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
            Any: The item at the top.

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
            bool: True if the stack is empty, False otherwise.
        """
        return self.size() == 0

    def clear(self):
        """Remove all items from the stack."""
        self._items.clear()

    def to_list(self):
        """
        Convert the stack to a list.

        Returns:
            list: Items in the stack from top to bottom.
        """
        return self._items[::-1].copy()  # Return a copy with top item first

    @classmethod
    def from_list(cls, lst):
        """
        Create a stack from a list.

        Args:
            lst (list): Items to initialize the stack.

        Returns:
            Stack: Stack instance containing the items (top of stack is last element of list).
        """
        stack = cls()
        stack._items = list(lst)[::-1]  # Reverse to have last element as top
        return stack

    def search(self, item):
        """
        Search for an item and return its position from the top.

        Args:
            item: The item to search for.

        Returns:
            int: 1-based position from the top, or -1 if not found.
        """
        try:
            index = self._items[::-1].index(item)
            return index + 1
        except ValueError:
            return -1

    def extend(self, iterable):
        """
        Extend the stack by pushing all items from an iterable.

        Args:
            iterable: Items to be added to the stack.

        Raises:
            ValueError: If the iterable is empty.
        """
        if not iterable:
            raise ValueError("iterable is empty")
        for item in iterable:
            self.push(item)


def main():
    """Demonstrate the Stack class functionality."""
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack)  # Stack (top -> bottom): [3, 2, 1]
    print(stack.peek())  # 3
    print(stack.pop())  # 3
    print(stack.size())  # 2
    print(stack.is_empty())  # False
    stack.clear()
    print(stack.is_empty())  # True


if __name__ == "__main__":
    main()
