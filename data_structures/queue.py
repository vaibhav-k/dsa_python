"""
data_structures.queue
=====================

A simple implementation of a queue data structure (FIFO) for Python.

Features:
    - enqueue(item): Add an item to the rear of the queue.
    - dequeue(): Remove and return the front item.
    - peek(): View the front item without removing it.
    - is_empty(): Check if the queue is empty.
    - size(): Get the number of items in the queue.
    - clear(): Remove all items from the queue.
    - to_list(): Return a copy of the queue as a list.
    - from_list(lst): Create a queue from a list.
    - search(item): Return the 1-based position of an item from the front, or -1 if not found.
    - extend(iterable): Add multiple items to the rear from an iterable.

Author:
    Vaibhav Kulshrestha

Date:
    2025-10-31
"""


class Queue:
    """
    A class representing a queue data structure (FIFO - First In, First Out).

    Attributes:
        _items (list): Internal list to store queue items.
    """

    def __init__(self):
        """Initialize an empty queue."""
        self._items = []

    def __str__(self):
        """
        Return a string representation of the queue (front -> rear).

        Returns:
            str: Queue from front to rear.
        """
        return f"Queue (front -> rear): {self._items}"

    def size(self):
        """
        Return the number of items in the queue.

        Returns:
            int: Size of the queue.
        """
        return len(self._items)

    def __len__(self):
        """Return the number of items in the queue (len(queue))."""
        return self.size()

    def __contains__(self, item):
        """
        Check if an item is in the queue.

        Args:
            item: The item to check for.

        Returns:
            bool: True if item is in the queue, False otherwise.
        """
        return item in self._items

    def __iter__(self):
        """Return an iterator over the queue from front to rear."""
        return iter(self._items)

    def __getitem__(self, index):
        """
        Get an item by index from the queue.

        Args:
            index (int): Index of the item to retrieve.

        Returns:
            Any: The item at the specified index.

        Raises:
            IndexError: If the index is out of range.
        """
        if isinstance(index, int):
            size = self.size()
            if index < 0:
                index += size
            if index < 0 or index >= size:
                raise IndexError(
                    f"queue index out of range: {index} (valid range: 0 to {size - 1})"
                )
            return self._items[index]
        elif isinstance(index, slice):
            # Support slicing
            return self._items[index]
        else:
            raise TypeError(
                "queue indices must be integers or slices, not {}".format(
                    type(index).__name__
                )
            )

    def __setitem__(self, index, value):
        """
        Set an item at a specific index in the queue.

        Args:
            index (int or slice): Index or slice to set.
            value: Value to set (or iterable for slice).

        Raises:
            IndexError: If the index is out of range.
            TypeError: If index is not int or slice.
        """
        if isinstance(index, int):
            size = self.size()
            if index < 0:
                index += size
            if index < 0 or index >= size:
                raise IndexError("queue index out of range")
            self._items[index] = value
        elif isinstance(index, slice):
            self._items[index] = value
        else:
            raise TypeError(
                "queue indices must be integers or slices, not {}".format(
                    type(index).__name__
                )
            )

    def enqueue(self, item):
        """
        Add an item to the rear of the queue.

        Args:
            item: The item to be added.
        """
        self._items.append(item)

    def dequeue(self):
        """
        Remove and return the front item of the queue.

        Returns:
            Any: The item at the front.

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
            Any: The item at the front.

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
            bool: True if the queue is empty, False otherwise.
        """
        return self.size() == 0

    def clear(self):
        """Remove all items from the queue."""
        self._items.clear()

    def to_list(self):
        """
        Convert the queue to a list.

        Returns:
            list: Items in the queue from front to rear.
        """
        return self._items.copy()  # Return a copy of the list from front to rear

    @classmethod
    def from_iterable(cls, iterable):
        """
        Create a queue from any iterable.

        Args:
            iterable: An iterable of items to be added to the queue.

        Returns:
            Queue: Queue instance containing the items in order.
        """
        queue = cls()
        for item in iterable:
            queue.enqueue(item)  # Maintain order from front to rear
        return queue

    def search(self, item):
        """
        Search for an item and return its position from the front.

        Args:
            item: The item to search for.

        Returns:
            int: 1-based position from the front, or -1 if not found.
        """
        try:
            index = self._items.index(item)
            return index + 1
        except ValueError:
            return -1

    def extend(self, iterable):
        """
        Extend the queue by adding all items from an iterable to the rear.

        Args:
            iterable: Items to be added to the queue.
        """
        iterator = iter(iterable)
        try:
            first_item = next(iterator)
        except StopIteration:
            return  # Iterable is empty, do nothing
        self.enqueue(first_item)
        for item in iterator:
            self.enqueue(item)


def main():
    """Demonstrate the Queue class functionality."""
    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)

    print(queue)  # Queue (front -> rear): [10, 20, 30]
    print(queue.peek())  # 10
    print(queue.dequeue())  # 10
    print(queue.size())  # 2
    print(queue.is_empty())  # False

    queue.extend([40, 50])
    print(queue)  # Queue (front -> rear): [20, 30, 40, 50]
    print(queue.search(30))  # 2
    print(queue.search(0))  # 2

    queue.clear()
    print(queue.is_empty())  # True

    queue_from_list = Queue.from_iterable([1, 2, 3])
    print(queue_from_list)  # Queue (front -> rear): [1, 2, 3]


if __name__ == "__main__":
    main()
