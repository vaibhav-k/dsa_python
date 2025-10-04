"""
This module provides a simple implementation of a singly linked list using Python classes.
The singly linked list supports common operations such as:

- append: Add an item to the end of the list
- prepend: Add an item to the beginning of the list
- delete: Remove an item by value
- find: Search for an item by value
- display: Print all items in the list
- size: Get the number of items in the list

The LinkedList class is designed to be reusable and easy to integrate into larger applications.
It includes error handling for empty list operations and a string representation for debugging.

Author: Vaibhav Kulshrestha
Date: 10/04/2025
"""

class Node:
    """
    A class representing a node in a singly linked list.
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
    A class representing a singly linked list.
    """

    def __init__(self):
        """
        Initialize an empty linked list.
        """
        self.head = None

    def append(self, data):
        """
        Add a node with the given data to the end of the list.

        Args:
            data: The value to be added to the list.
        """
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
            data: The value to be added to the list.

        Args:
            data: The value to be added to the list.
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        """
        Delete the first node with the given data.

        Args:
            data: The value to be removed from the list.

        Raises:
            ValueError: If the list is empty or the value is not found.
        """
        if not self.head:
            raise ValueError("List is empty")

        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        while current.next and current.next.data != data:
            current = current.next

        if not current.next:
            raise ValueError(f"{data} not found in the list")

        current.next = current.next.next

    def find(self, data):
        """
        Search for a node with the given data.

        Args:
            data: The value to search for.

        Returns:
        True if found, False otherwise.
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
            int: The total number of nodes.
        """
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def display(self):
        """
        Print all nodes in the list.
        """
        nodes = []
        current = self.head
        while current:
            nodes.append(str(current.data))
            current = current.next
        print(f"LinkedList: {' -> '.join(nodes)}")


if __name__ == "__main__":
    ll = LinkedList()
    ll.append(10)
    ll.append(20)
    ll.prepend(5)
    ll.display()           # LinkedList: 5 -> 10 -> 20
    print(ll.find(10))     # True
    ll.delete(10)
    ll.display()           # LinkedList: 5 -> 20
    print(ll.size())       # 2
