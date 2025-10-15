"""
algorithms.recursion
====================

Recursive algorithms for classic computational problems.

Functions:
    sum_list(numbers): Calculate the sum of a list of numbers recursively.
    int_to_str(n, base): Convert an integer to a string in any base recursively.
    sierpinski_triangle(order): Generate a Sierpinski triangle pattern recursively.
    tower_of_hanoi(n, source, target, auxiliary): Solve the Tower of Hanoi problem recursively.
    explore_maze(maze, start, end, path=None): Find a path through a maze recursively.

Constants:
    THREE_LAWS_OF_RECURSION: Description of the three laws of recursion.

Author:
    Vaibhav Kulshrestha

Date:
    2025-15-10
"""

THREE_LAWS_OF_RECURSION = [
    "A recursive algorithm must have a base case.",
    "A recursive algorithm must change its state and move toward the base case.",
    "A recursive algorithm must call itself, recursively.",
]


def sum_list(numbers):
    """
    Recursively calculates the sum of a list of numbers.

    Args:
        numbers (list): List of numbers.

    Returns:
        int or float: The sum of the numbers.
    """
    if not numbers:
        return 0
    return numbers[0] + sum_list(numbers[1:])


def int_to_str(n, base):
    """
    Recursively converts an integer to a string in any base.

    Args:
        n (int): The integer to convert.
        base (int): The base for conversion (2-36).

    Returns:
        str: String representation of the integer in the given base.

    Raises:
        ValueError: If n is negative, an integer, or the base is out of range.
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer.")
    if not (2 <= base <= 36):
        raise ValueError("Base must be between 2 and 36.")
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n < base:
        return digits[n]
    else:
        return int_to_str(n // base, base) + digits[n % base]


def sierpinski_triangle(order):
    """
    Recursively generates a Sierpinski triangle pattern.

    Args:
        order (int): The order (depth) of the triangle.

    Returns:
        list of str: Lines representing the Sierpinski triangle.

    Raises:
        ValueError: If order is negative or not an integer.
    """
    if order < 0 or not isinstance(order, int):
        raise ValueError("Order must be a non-negative integer.")
    if order == 0:
        return ["*"]
    prev = sierpinski_triangle(order - 1)
    space = " " * (2 ** (order - 1))
    top = [space + line + space for line in prev]
    bottom = [line + " " + line for line in prev]
    return top + bottom


def tower_of_hanoi(n, source, target, auxiliary, moves=None):
    """
    Recursively solves the Tower of Hanoi problem.

    Args:
        n (int): Number of disks.
        source (str): Name of the source rod.
        target (str): Name of the target rod.
        auxiliary (str): Name of the auxiliary rod.
        moves (list, optional): List to record moves.

    Returns:
        list of tuple: Moves as (from_rod, to_rod).

    Raises:
        ValueError: If n is not a positive integer.
    """
    if n <= 0 or not isinstance(n, int):
        raise ValueError("Number of disks must be a positive integer.")
    if moves is None:
        moves = []
    if n == 1:
        moves.append((source, target))
    else:
        tower_of_hanoi(n - 1, source, auxiliary, target, moves)
        moves.append((source, target))
        tower_of_hanoi(n - 1, auxiliary, target, source, moves)
    return moves


def explore_maze(maze, start, end, path=None):
    """
    Recursively explores a maze to find a path from start to end.

    Args:
        maze (list of list): 2D grid representing the maze (0: open, 1: wall).
        start (tuple): Starting position (row, col).
        end (tuple): Ending position (row, col).
        path (list, optional): Current path.

    Returns:
        list of tuple or None: Path from start to end, or None if not found.
    """
    if path is None:
        path = []
    row, col = start
    if (
        row < 0
        or row >= len(maze)
        or col < 0
        or col >= len(maze[0])
        or maze[row][col] == 1
        or start in path
    ):
        return None
    path = path + [start]
    if start == end:
        return path
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        next_pos = (row + dr, col + dc)
        result = explore_maze(maze, next_pos, end, path)
        if result:
            return result
    return None


def main():
    """Demonstrate the recursive algorithms."""
    numbers = [1, 2, 3, 4, 5]
    print(f"Sum of {numbers}:", sum_list(numbers))

    n, base = 255, 16
    print(f"Integer {n} in base {base}:", int_to_str(n, base))

    order = 4
    print(f"Sierpinski Triangle of order {order}:")
    for line in sierpinski_triangle(order):
        print(line)

    num_disks = 3
    source_rod, target_rod, auxiliary_rod = "A", "C", "B"
    print(f"Tower of Hanoi moves for {num_disks} disks:")
    for move in tower_of_hanoi(num_disks, source_rod, target_rod, auxiliary_rod):
        print(f"Move disk from {move[0]} to {move[1]}")

    maze = [
        [0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 1, 1, 0],
    ]
    start_pos, end_pos = (0, 0), (4, 4)
    path = explore_maze(maze, start_pos, end_pos)
    print(f"Path through the maze from {start_pos} to {end_pos}:\n{path}")

    print("Three Laws of Recursion:")
    for law in THREE_LAWS_OF_RECURSION:
        print("-", law)


if __name__ == "__main__":
    main()
