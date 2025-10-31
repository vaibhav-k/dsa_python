"""
data_structures.single_linked_list
==================================

A simple implementation of a singly linked list for Python.

Features:
    - append(data): Add an item to the end of the list.
    - prepend(data): Add an item to the beginning of the list.
    - delete(data): Remove the first item by value.
    - find(data): Search for an item by value.
    - display(): Print all items in the list.
    - size(): Get the number of items in the list.
    - clear(): Remove all items from the list.
    - to_list(): Return a copy of the list as a Python list.
    - from_list(lst): Create a linked list from a Python list.
    - search(data): Return the 1-based position of an item, or -1 if not found.
    - extend(iterable): Add multiple items from an iterable.
    - __len__, __contains__, __iter__, __getitem__, __setitem__.

Author:
    Vaibhav Kulshrestha

Date:
    2025-10-31
"""


class Node:
    """
    A node in a singly linked list.

    Attributes:
        data: The value stored in the node.
        next: Reference to the next node.
    """

    def __init__(self, data):
        """
        Initialize a node with data and a reference to the next node.

        Args:
            data: The value to store in the node.
        """
        self.data = data
        self.next = None


class LinkedList:
    """
    A singly linked list implementation.

    Attributes:
        head (Node): The first node in the list.
    """

    def __init__(self):
        """Initialize an empty linked list."""
        self.head = None

    def to_list(self):
        """
        Convert the linked list to a Python list.

        Returns:
            list: List of node values.
        """
        if not self.head:  # Empty list
            return []
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

    def __str__(self):
        """Return a string representation of the list."""
        return f"LinkedList: {' -> '.join(map(str, self.to_list()))}"

    def size(self):
        return sum(1 for _ in self)

    def __len__(self):
        """Return the number of nodes in the list."""
        return self.size()

    def find(self, data):
        """
        Search for a node with the given data.

        Args:
            data: The value to search for.

        Returns:
            bool: True if found, False otherwise.
        """
        if not self.head or data is None:  # Empty list or None data
            return False
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def __contains__(self, item):
        """
        Check if an item is in the list.

        Args:
            item: The value to check for.

        Returns:
            bool: True if found, False otherwise.
        """
        return self.find(item)

    def __iter__(self):
        """Iterate over the list from head to tail."""
        current = self.head
        while current:
            yield current.data
            current = current.next

    def __getitem__(self, index):
        """
        Get the item at a specific index.

        Args:
            index (int): The index to retrieve.

        Returns:
            The value at the specified index.

        Raises:
            IndexError: If the index is out of range or the list is empty.
            TypeError: If the index is not an integer.
        """
        if not isinstance(index, int):
            raise TypeError("Index must be an integer")
        if index < 0 or index >= self.size():
            raise IndexError("list index out of range")
        current = self.head
        for _ in range(index):
            if not current:
                raise IndexError("list index out of range")
            current = current.next
        return current.data

    def __setitem__(self, index, value):
        """
        Set the value at a specific index.

        Args:
            index (int): The index to set.
            value: The value to assign.

        Raises:
            IndexError: If the index is out of range.
            TypeError: If the index is not an integer.
        """
        if not isinstance(index, int):
            raise TypeError("Index must be an integer")
        if index < 0 or index >= self.size():
            raise IndexError("list index out of range")
        current = self.head
        for _ in range(index):
            current = current.next
        current.data = value

    def append(self, data):
        """
        Add a node with the given data to the end of the list.

        Args:
            data: The value to be added.

        Raises:
            ValueError: If data is None or empty.
        """
        if data is None:
            raise ValueError("Cannot append None or empty data")
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def prepend(self, data):
        """
        Add a node with the given data to the beginning of the list.

        Args:
            data: The value to be added.

        Raises:
            ValueError: If data is None or empty.
        """
        if data is None:
            raise ValueError("Cannot prepend None or empty data")
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        """
        Delete the first node with the given data.

        Args:
            data: The value to be deleted.

        Raises:
            ValueError: If the list is empty or data not found.
        """
        if not self.head:
            raise ValueError("List is empty")
        if data is None:
            raise ValueError("Cannot delete None or empty data")
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next
        raise ValueError(f"{data} not found in the list")

    def clear(self):
        """Remove all nodes from the list."""
        self.head = None

    @classmethod
    def from_iterable(cls, iterable):
        """
        Create a linked list from any iterable.

        Args:
            iterable: An iterable of values.

        Returns:
            LinkedList: Linked list containing the values.
        """
        ll = cls()
        for item in iterable:
            if item is not None:
                ll.append(item)
        return ll

    def search(self, data):
        """
        Search for an item and return its 1-based position, or -1 if not found.
        Returns the position of the first occurrence of the item.

        Args:
            data: The value to search for.

        Returns:
            int: 1-based position, or -1 if not found.
        """
        if not self.head or data is None:  # Empty list or None/empty data
            return -1
        current = self.head
        pos = 1
        while current:
            if current.data == data:
                return pos
            current = current.next
            pos += 1
        return -1

    def extend(self, iterable):
        """
        Add multiple items from an iterable to the end of the list.

        Args:
            iterable: Items to add.
        """
        if iterable is None:  # Exit if iterable is None
            return
        for item in iterable:
            if item is not None:
                self.append(item)

    def display(self):
        """Print all nodes in the list."""
        print(self)


def main():
    """Demonstrate the LinkedList class functionality."""
    ll = LinkedList()
    ll.append(10)
    ll.append(20)
    ll.prepend(5)
    ll.display()                                                        # LinkedList: 5 -> 10 -> 20

    print(ll.find(10))                                                  # True
    ll.delete(10)
    ll.display()                                                        # LinkedList: 5 -> 20

print(ll.size())                                                        # 2
    ll.extend([30, 40])
    ll.display()                                                        # LinkedList: 5 -> 20 -> 30 -> 40

    print(ll.search(40))                                                # 4
    print(ll.to_list())                                                 # [5, 20, 30, 40]
    ll.clear()
    print(len(ll))                                                      # 0
    print(list(ll))                                                     # []

    single_linked_from_list = LinkedList.from_iterable([1, 2, 3, 4])
    single_linked_from_list.display()                                   # LinkedList: 1 -> 2 -> 3 -> 4


if __name__ == "__main__":
    main()
