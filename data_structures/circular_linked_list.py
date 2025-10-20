"""
data_structures.circular_linked_list
====================================

A module implementing a Circular Linked List data structure.

Classes:
- Node class representing each element in the list.
- CircularLinkedList class with methods to add, remove, and traverse nodes.

Features of CircularLinkedList:
    - add(data): Add a node with the given data to the list.
    - remove(data): Remove the first node with the given data.
    - traverse(): Generator to iterate through the list.
    - to_list(): Convert the circular linked list to a standard Python list.
    - clear(): Remove all nodes from the list.
    - is_empty(): Check if the list is empty.
    - find(data): Find a node with the given data.
    - display(): Print the elements of the list.
    - from_list(data_list): Class method to create a CircularLinkedList from a standard Python list.
    - __len__, __contains__, __iter__, __getitem__, __setitem__.

Author:
    Vaibhav Kulshrestha

Date:
    2025-14-20
"""


class Node:
    """
    A node in a circular linked list.

    Attributes:
        data: The value stored in the node.
        next: Reference to the next node in the list.
    """

    def __init__(self, data):
        """
        Initialize a node with the given data.

        Args:
            data: The value to be stored in the node.
        """
        self.data = data
        self.next = None


class CircularLinkedList:
    """
    A circular linked list implementation.

    Attributes:
        head (Node): The first node in the list.
        size (int): The number of nodes in the list.
    """

    def __init__(self):
        """Initialize an empty circular linked list."""
        self.head = None
        self.size = 0

    def add(self, data):
        """
        Add a node with the given data to the list at the end.

        Args:
            data: The value to be added to the list.

        Returns:
            None: Adds a new node to the circular linked list.
        """
        if not data:
            return
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = new_node
        else:
            tail = self.head
            while tail.next != self.head:
                tail = tail.next
            tail.next = new_node
            new_node.next = self.head
        self.size += 1

    def remove(self, data):
        """
        Remove the first node with the given data.

        Args:
            data: The value to be removed from the list.

        Returns:
            bool: True if the node was found and removed, False otherwise.
        """
        if not self.head or data is None:
            return False

        current = self.head
        prev = None

        for _ in range(self.size):
            if current.data == data:
                if prev:
                    prev.next = current.next
                    if current == self.head:
                        self.head = current.next
                else:
                    if self.size == 1:
                        self.head = None
                    else:
                        tail = self.head
                        while tail.next != self.head:
                            tail = tail.next
                        self.head = current.next
                        tail.next = self.head
                self.size -= 1
                return True
            prev = current
            current = current.next
            if current is None:
                break

        return False

    def traverse(self):
        """
        Generator to iterate through the circular linked list.

        Returns:
            Yields each node's data in the list.
        """
        if not self.head:
            return

        current = self.head
        while True:
            yield current.data
            current = current.next
            if current == self.head:
                break

    def to_list(self):
        """
        Convert the circular linked list to a standard Python list.

        Returns:
            list: A list containing all the elements of the circular linked list.
        """
        result = []
        for data in self.traverse():
            result.append(data)
        return result

    def clear(self):
        """
        Remove all nodes from the circular linked list.
        """
        self.head = None
        self.size = 0

    def is_empty(self):
        """
        Check if the circular linked list is empty.

        Returns:
            bool: True if the list is empty, False otherwise.
        """
        return self.size == 0

    def find(self, data):
        """
        Find a node with the given data.

        Args:
            data: The value to search for in the list.

        Returns:
            bool: True if the node is found, False otherwise.
        """
        if not self.head:
            return False

        current = self.head
        while True:
            if current.data == data:
                return True
            current = current.next
            if current == self.head:
                break

        return False

    def display(self):
        """
        Print the elements of the circular linked list.
        """
        if not self.head:
            print("List is empty")
            return

        current = self.head
        elements = []
        while True:
            elements.append(str(current.data))
            current = current.next
            if current == self.head:
                break

        print(" -> ".join(elements) + " (circular)")

    @classmethod
    def from_list(cls, data_list):
        """
        Create a CircularLinkedList from a standard Python list.

        Args:
            data_list (list): A list of values to be added to the circular linked list.

        Returns:
            CircularLinkedList: A new circular linked list containing the elements from data_list.
        """
        cll = cls()
        for data in data_list:
            cll.add(data)
        return cll

    def __len__(self):
        """
        Return the number of nodes in the circular linked list.
        """
        return self.size

    def __contains__(self, data):
        """
        Check if a value is in the circular linked list.

        Args:
            data: The value to check for.

        Returns:
            bool: True if the value is found, False otherwise.
        """
        return self.find(data)

    def __iter__(self):
        """
        Iterate over the circular linked list.
        """
        return self.traverse()

    def __getitem__(self, index):
        """
        Get the data at the specified index.

        Args:
            index (int): The index of the node to retrieve.

        Returns:
            The data at the specified index.

        Raises:
            IndexError: If the index is out of bounds.
        """
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        if self.size == 0:
            raise IndexError("Index out of bounds")

        current = self.head
        for _ in range(index):
            current = current.next
        return current.data

    def __setitem__(self, index, data):
        """
        Set the data at the specified index.

        Args:
            index (int): The index of the node to update.
            data: The new value to set.

        Raises:
            IndexError: If the index is out of bounds.
        """
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")

        current = self.head
        for _ in range(index):
            current = current.next
        current.data = data


def main():
    """
    Demonstrate the usage of CircularLinkedList.
    """
    cll = CircularLinkedList()
    cll.add(1)
    cll.add(2)
    cll.add(3)
    cll.display()                     # Output: 1 -> 2 -> 3 (circular)
    print(f"Size: {len(cll)}")        # Output: Size: 3
    cll.remove(2)
    cll.display()                     # Output: 1 -> 3 (circular)
    print(f"Contains 3: {3 in cll}")  # Output: Contains 3: True
    print(f"Contains 2: {2 in cll}")  # Output: Contains 2: False
    cll.clear()
    cll.display()                     # Output: List is empty


if __name__ == "__main__":
    main()
