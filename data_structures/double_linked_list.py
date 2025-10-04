"""
This module provides a simple implementation of a doubly linked list using Python classes.
The doubly linked list supports common operations such as:

- append: Add an item to the end of the list
- prepend: Add an item to the beginning of the list
- delete: Remove an item by value
- find: Search for an item by value
- display_forward: Print all items from head to tail
- display_backward: Print all items from tail to head
- size: Get the number of items in the list

The DoublyLinkedList class is designed to be reusable and easy to integrate into larger applications.
It includes error handling for empty list operations and a string representation for debugging.

Author: Vaibhav Kulshrestha
Date: 10/04/2025
"""

class Node:
    """
    Represents a node in a doubly linked list.

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
    A class representing a doubly linked list.
    """

    def __init__(self):
        """
        Initialize an empty doubly linked list.
        """
        self.head = None
        self.tail = None

    def append(self, data):
        """
        Add a node with the given data to the end of the list.

        Args:
            data: The value to be added.
        """
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
        new_node = Node(data)
        if not self.head:
            self.head = self.tail = new_node
            return

        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def delete(self, data):
        """
        Delete the first node with the specified data.

        Args:
            data: The value to be removed.

        Raises:
            ValueError: If the value is not found.
        """
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

    def find(self, data):
        """
        Search for a node with the specified data.

        Args:
            data: The value to search for.

        Returns:
            bool: True if found, False otherwise.
        """
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def size(self):
        """
        Count the number of nodes in the list.

        Returns:
            int: The number of nodes.
        """
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def display_forward(self):
        """
        Print the list from head to tail.
        """
        nodes = []
        current = self.head
        while current:
            nodes.append(str(current.data))
            current = current.next
        print(f"Forward: {' <-> '.join(nodes)}")

    def display_backward(self):
        """
        Print the list from tail to head.
        """
        nodes = []
        current = self.tail
        while current:
            nodes.append(str(current.data))
            current = current.prev
        print(f"Backward: {' <-> '.join(nodes)}")


if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.append(10)
    dll.append(20)
    dll.prepend(5)
    dll.display_forward()    # Forward: 5 <-> 10 <-> 20
    dll.display_backward()   # Backward: 20 <-> 10 <-> 5
    print(dll.find(10))      # True
    dll.delete(10)
    dll.display_forward()    # Forward: 5 <-> 20
    print(dll.size())        # 2
