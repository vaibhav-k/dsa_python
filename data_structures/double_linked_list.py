"""
data_structures.double_linked_list
==================================

A simple implementation of a doubly linked list for Python.

Features:
    - append(data): Add an item to the end of the list.
    - prepend(data): Add an item to the beginning of the list.
    - delete(data): Remove the first item by value.
    - find(data): Search for an item by value.
    - display_forward(): Print all items from head to tail.
    - display_backward(): Print all items from tail to head.
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
    2025-14-20
"""


class Node:
    """
    A node in a doubly linked list.

    Attributes:
        data: The value stored in the node.
        prev: Reference to the previous node.
        next: Reference to the next node.
    """

    def __init__(self, data):
        """
        Initialize a node with data and no links.

        Args:
            data: The value to store in the node.
        """
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    """
    A doubly linked list implementation.

    Attributes:
        head (Node): The first node in the list.
        tail (Node): The last node in the list.
    """

    def __init__(self):
        """Initialize an empty doubly linked list."""
        self.head = None
        self.tail = None

    def __str__(self):
        """Return a string representation of the list."""
        return f"DoublyLinkedList: {' <-> '.join(map(str, self.to_list()))}"

    def size(self):
        """
        Count the number of nodes in the list.

        Returns:
            int: The total number of nodes.
        """
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
        if not self.head or not data:  # Empty list or None data
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
        if not self.head or not item:  # Empty list or None item
            return False
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
            IndexError: If the index is out of range.
        """
        if index < 0 or index >= self.size():
            raise IndexError("list index out of range")
        current = self.head
        for _ in range(index):
            if not current:
                raise IndexError("list index out of range")
            current = current.next
        if not current:
            raise IndexError("list index out of range")
        return current.data

    def __setitem__(self, index, value):
        """
        Set the value at a specific index.

        Args:
            index (int): The index to set.
            value: The value to assign.

        Raises:
            IndexError: If the index is out of range.
        """
        if index < 0 or index >= self.size():
            raise IndexError("list index out of range")
        current = self.head
        for _ in range(index):
            if not current:
                raise IndexError("list index out of range")
            current = current.next
        if not current:
            raise IndexError("list index out of range")
        current.data = value

    def append(self, data):
        """
        Add a node with the given data to the end of the list.

        Args:
            data: The value to be added.
        """
        if not data:  # Ignore None or empty data
            return
        new_node = Node(data)
        if not self.head:
            self.head = self.tail = new_node
            return
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    def prepend(self, data):
        """
        Add a node with the given data to the beginning of the list.

        Args:
            data: The value to be added.
        """
        if not data:  # Ignore None or empty data
            return
        new_node = Node(data)
        if not self.head:
            self.head = self.tail = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def delete(self, data):
        """
        Delete the first node with the given data.

        Args:
            data: The value to be removed.

        Raises:
            ValueError: If the list is empty or data not found.
        """
        if not self.head:
            raise ValueError("List is empty")
        if not data:
            raise ValueError("Cannot delete None or empty data")
        current = self.head
        while current:
            if current.data == data:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                return
            current = current.next
        raise ValueError(f"{data} not found in the list")

    def clear(self):
        """Remove all nodes from the list."""
        self.head = None
        self.tail = None

    def to_list(self):
        """
        Convert the linked list to a Python list.

        Returns:
            list: List of node values.
        """
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

    @classmethod
    def from_list(cls, lst):
        """
        Create a doubly linked list from a Python list.

        Args:
            lst (list): List of values.

        Returns:
            DoublyLinkedList: Linked list containing the values.
        """
        if not lst:  # Empty list
            return cls()
        dll = cls()
        for item in lst:
            dll.append(item)
        return dll

    def search(self, data):
        """
        Search for an item and return its 1-based position, or -1 if not found.

        Args:
            data: The value to search for.

        Returns:
            int: 1-based position, or -1 if not found.
        """
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
        for item in iterable:
            self.append(item)

    def display_forward(self):
        """Print all nodes from head to tail."""
        print(f"Forward: {' <-> '.join(map(str, self.to_list()))}")

    def display_backward(self):
        """Print all nodes from tail to head."""
        nodes = []
        current = self.tail
        while current:
            nodes.append(str(current.data))
            current = current.prev
        print(f"Backward: {' <-> '.join(nodes)}")


def main():
    """Demonstrate the DoublyLinkedList class functionality."""
    dll = DoublyLinkedList()
    dll.append(10)
    dll.append(20)
    dll.prepend(5)
    dll.display_forward()  # Forward: 5 <-> 10 <-> 20
    dll.display_backward()  # Backward: 20 <-> 10 <-> 5
    print(dll.find(10))  # True
    dll.delete(10)
    dll.display_forward()  # Forward: 5 <-> 20
    print(dll.size())  # 2
    dll.extend([30, 40])
    dll.display_forward()  # Forward: 5 <-> 20 <-> 30 <-> 40
    print(dll.search(40))  # 4
    print(dll.to_list())  # [5, 20, 30, 40]
    dll.clear()
    print(len(dll))  # 0
    print(list(dll))  # []


if __name__ == "__main__":
    main()
