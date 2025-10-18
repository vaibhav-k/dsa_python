"""
algorithms.backtracking
=======================

This module contains implementations of backtracking algorithms.

Functions:
    n_queens: Solve the N-Queens problem using backtracking.
    sudoku_solver: Solve a Sudoku puzzle using backtracking.
    word_search: Find words in a grid using backtracking.
    subset_sum: Find subsets that sum to a target value using backtracking.
    permutations: Generate all permutations of a list using backtracking.
    rat_in_maze: Solve the Rat in a Maze problem using backtracking.
    hamiltonian_cycle: Find a Hamiltonian cycle in a graph using backtracking.
    knights_tour: Solve the Knight's Tour problem using backtracking.
    palindrome_partitioning: Partition a string into palindromic substrings using backtracking.
    combination_sum: Find combinations that sum to a target value using backtracking.
    all_possible_valid_parentheses: Generate all combinations of valid parentheses using backtracking.
    string_pattern_matching: Match a string against a pattern using backtracking.
    magic_square: Generate a magic square using backtracking.

CONSTANTS:
    BACKTRACKING_ALGORITHM_PROPERTIES: Description of the properties of backtracking algorithms.

Author:
    Vaibhav Kulshrestha

Date:
    2025-10-18
"""

BACKTRACKING_ALGORITHM_PROPERTIES = [
    "Uses recursion to explore all possible configurations",
    "Backtracks when a configuration is found to be invalid",
    "Often used for constraint satisfaction problems",
    "Can be inefficient for large problem spaces without optimizations",
]


def n_queens(n):
    """
    Solve the N-Queens problem using backtracking.

    Args:
        n (int): The size of the chessboard and number of queens.

    Returns:
        list: A list of solutions, where each solution is represented as a list of column indices for each row.

    Raises:
        ValueError: If n is not a positive integer.
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")

    def is_safe(board, row, col):
        """Check if it's safe to place a queen at board[row][col]."""
        for i in range(row):
            if (
                board[i] == col
                or board[i] - i == col - row
                or board[i] + i == col + row
            ):
                return False
        return True

    def solve(row, board, solutions):
        """Recursive helper function to solve the N-Queens problem."""
        if row == n:
            solutions.append(board[:])
            return
        for col in range(n):
            if is_safe(board, row, col):
                board.append(col)
                solve(row + 1, board, solutions)
                board.pop()

    solutions = []
    solve(0, [], solutions)
    return solutions


def sudoku_solver(board):
    """
    Solve a Sudoku puzzle using backtracking.

    Args:
        board (list of list of int): A 9x9 Sudoku board with 0s representing empty cells.

    Returns:
        bool: True if the Sudoku is solved, False otherwise.

    Raises:
        ValueError: If the board is not a valid 9x9 grid.
    """
    if (
        len(board) != 9
        or any(len(row) != 9 for row in board)
        or any(
            not all(isinstance(cell, int) and 0 <= cell <= 9 for cell in row)
            for row in board
        )
    ):
        raise ValueError("Board must be a 9x9 grid")

    def is_valid(num, row, col):
        """Check if placing num at board[row][col] is valid."""
        for i in range(9):
            if board[row][i] == num or board[i][col] == num:
                return False
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if board[start_row + i][start_col + j] == num:
                    return False
        return True

    def solve_sudoku():
        for row in range(9):
            for col in range(9):
                if board[row][col] == 0:
                    for num in range(1, 10):
                        if is_valid(num, row, col):
                            board[row][col] = num
                            if solve_sudoku():
                                return True
                            board[row][col] = 0
                    return False
        return True

    solve_sudoku()
    return True


def word_search(board, word):
    """
    Find words in a grid using backtracking.

    Args:
        board (list of list of str): A 2D grid of characters.
        word (str): The word to search for.

    Returns:
        bool: True if the word is found in the grid, False otherwise.

    Raises:
        ValueError: If the board is not a valid 2D grid of characters or if word is not a string.
    """
    if not all(isinstance(row, list) for row in board) or not all(
        isinstance(cell, str) and len(cell) == 1 for row in board for cell in row
    ):
        raise ValueError("Board must be a 2D grid of single-character strings")
    if not isinstance(word, str):
        raise ValueError("Word must be a string")
    if not board or not board[0] or not word:
        return False
    rows, cols = len(board), len(board[0]) if board else 0

    def backtrack(r, c, index):
        """Backtracking helper function to search for the word."""
        if index == len(word):
            return True
        if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != word[index]:
            return False

        temp = board[r][c]
        board[r][c] = "#"

        found = (
            backtrack(r + 1, c, index + 1)
            or backtrack(r - 1, c, index + 1)
            or backtrack(r, c + 1, index + 1)
            or backtrack(r, c - 1, index + 1)
        )

        board[r][c] = temp
        return found

    for i in range(rows):
        for j in range(cols):
            if backtrack(i, j, 0):
                return True
    return False


def subset_sum(nums, target):
    """
    Find subsets that sum to a target value using backtracking.

    Args:
        nums (list of int): A list of integers.
        target (int): The target sum.

    Returns:
        list: A list of subsets that sum to the target value.

    Raises:
        ValueError: If nums is not a list of integers or if target is not an integer.
    """
    if not all(isinstance(num, int) for num in nums):
        raise ValueError("nums must be a list of integers")
    if not isinstance(target, int):
        raise ValueError("target must be an integer")

    def backtrack(start, path, current_sum):
        """Backtracking helper function to find subsets."""
        if current_sum == target:
            result.append(path[:])
            return
        if current_sum > target:
            return
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path, current_sum + nums[i])
            path.pop()

    result = []
    backtrack(0, [], 0)
    return result


def permutations(nums):
    """
    Generate all permutations of a list using backtracking.

    Args:
        nums (list): A list of elements to permute.

    Returns:
        list: A list of all permutations of the input list.

    Raises:
        ValueError: If nums is not a list.
    """
    if not isinstance(nums, list):
        raise ValueError("nums must be a list")

    result = []

    def backtrack(start):
        """Backtracking helper function to generate permutations."""
        if start == len(nums):
            result.append(nums[:])
            return
        for i in range(start, len(nums)):
            nums[start], nums[i] = nums[i], nums[start]
            backtrack(start + 1)
            nums[start], nums[i] = nums[i], nums[start]

    backtrack(0)
    return result


def rat_in_maze(maze):
    """
    Solve the Rat in a Maze problem using backtracking.

    Args:
        maze (list of list of int): A 2D grid where 1 is open and 0 is blocked.

    Returns:
        list: A list of paths, where each path is a list of (row, col) tuples.

    Raises:
        ValueError: If maze is not a valid 2D grid.
    """
    if not maze or not all(isinstance(row, list) for row in maze):
        raise ValueError("maze must be a 2D grid")
    n = len(maze)
    if any(len(row) != n for row in maze):
        raise ValueError("maze must be a square grid")

    paths = []

    def backtrack(r, c, path, visited):
        """Backtracking helper function to find paths."""
        if r < 0 or c < 0 or r >= n or c >= n or maze[r][c] == 0 or visited[r][c]:
            return
        path.append((r, c))
        visited[r][c] = True
        if r == n - 1 and c == n - 1:
            paths.append(path[:])
        else:
            backtrack(r + 1, c, path, visited)
            backtrack(r, c + 1, path, visited)
            backtrack(r - 1, c, path, visited)
            backtrack(r, c - 1, path, visited)
        path.pop()
        visited[r][c] = False

    visited = [[False] * n for _ in range(n)]
    backtrack(0, 0, [], visited)
    return paths


def hamiltonian_cycle(graph):
    """
    Find a Hamiltonian cycle in a graph using backtracking.

    Args:
        graph (list of list of int): An adjacency matrix representing the graph.

    Returns:
        list: A list of vertices representing the Hamiltonian cycle, or an empty list if no
                cycle exists.

    Raises:
        ValueError: If graph is not a valid adjacency matrix.
    """
    if not graph or not all(isinstance(row, list) for row in graph):
        raise ValueError("graph must be a 2D adjacency matrix")
    n = len(graph)
    if any(len(row) != n for row in graph):
        raise ValueError("graph must be a square matrix")

    path = [-1] * n
    path[0] = 0

    def is_safe(v, pos):
        """Check if vertex v can be added at position pos in the Hamiltonian Cycle."""
        if graph[path[pos - 1]][v] == 0:
            return False
        if v in path:
            return False
        return True

    def hamiltonian_util(pos):
        """Recursive utility function to solve the Hamiltonian Cycle problem."""
        if pos == n:
            return graph[path[pos - 1]][path[0]] == 1
        for v in range(1, n):
            if is_safe(v, pos):
                path[pos] = v
                if hamiltonian_util(pos + 1):
                    return True
                path[pos] = -1
        return False

    if not hamiltonian_util(1):
        return []
    return path + [path[0]]


def knights_tour(n):
    """
    Solve the Knight's Tour problem using backtracking.

    Args:
        n (int): The size of the chessboard (n x n).

    Returns:
        list: A list of moves representing the Knight's Tour, or an empty list if no tour exists.

    Raises:
        ValueError: If n is not a positive integer.
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")

    moves = [
        (2, 1),
        (1, 2),
        (-1, 2),
        (-2, 1),
        (-2, -1),
        (-1, -2),
        (1, -2),
        (2, -1),
    ]

    board = [[-1 for _ in range(n)] for _ in range(n)]
    path = []

    def is_valid(x, y):
        """Check if the move is valid."""
        return 0 <= x < n and 0 <= y < n and board[x][y] == -1

    def backtrack(x, y, move_count):
        """Backtracking helper function to find the Knight's Tour."""
        board[x][y] = move_count
        path.append((x, y))
        if move_count == n * n - 1:
            return True
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny):
                if backtrack(nx, ny, move_count + 1):
                    return True
        board[x][y] = -1
        path.pop()
        return False

    if backtrack(0, 0, 0):
        return path
    else:
        return []


def palindrome_partitioning(s):
    """
    Partition a string into palindromic substrings using backtracking.

    Args:
        s (str): The input string.

    Returns:
        list: A list of lists, where each inner list contains a valid partition of palindromic substrings.

    Raises:
        ValueError: If s is not a string.
    """
    if not isinstance(s, str):
        raise ValueError("s must be a string")

    def is_palindrome(sub):
        """Check if a substring is a palindrome."""
        return sub == sub[::-1]

    def backtrack(start, path):
        """Backtracking helper function to find palindromic partitions."""
        if start == len(s):
            result.append(path[:])
            return
        for end in range(start + 1, len(s) + 1):
            substring = s[start:end]
            if is_palindrome(substring):
                path.append(substring)
                backtrack(end, path)
                path.pop()

    result = []
    backtrack(0, [])
    return result


def combination_sum(candidates, target):
    """
    Find combinations that sum to a target value using backtracking.

    Args:
        candidates (list of int): List of candidate numbers.
        target (int): Target sum.

    Returns:
        list: List of lists, each containing a valid combination.

    Raises:
        ValueError: If candidates is not a list of integers or target is not an integer.
    """
    if not all(isinstance(num, int) for num in candidates):
        raise ValueError("candidates must be a list of integers")
    if not isinstance(target, int):
        raise ValueError("target must be an integer")

    result = []

    def backtrack(start, path, total):
        """Backtracking helper function to find combinations."""
        if total == target:
            result.append(path[:])
            return
        if total > target:
            return
        for i in range(start, len(candidates)):
            path.append(candidates[i])
            backtrack(i, path, total + candidates[i])
            path.pop()

    backtrack(0, [], 0)
    return result


def all_possible_valid_parentheses(n):
    """
    Generate all combinations of valid parentheses using backtracking.

    Args:
        n (int): Number of pairs of parentheses.

    Returns:
        list: A list of strings, each representing a valid combination of parentheses.

    Raises:
        ValueError: If n is not a non-negative integer.
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("n must be a non-negative integer")

    result = []

    def backtrack(s="", left=0, right=0):
        """Backtracking helper function to generate valid parentheses."""
        if len(s) == 2 * n:
            result.append(s)
            return
        if left < n:
            backtrack(s + "(", left + 1, right)
        if right < left:
            backtrack(s + ")", left, right + 1)

    backtrack()
    return result


def string_pattern_matching(s, pattern):
    """
    Match a string against a pattern using backtracking.

    Args:
        s (str): The input string.
        pattern (str): The pattern, which may include '.' (any char) and '*' (zero or more of previous char).

    Returns:
        bool: True if the string matches the pattern, False otherwise.
    """

    def backtrack(i, j):
        """Backtracking helper function to match string with pattern."""
        if j == len(pattern):
            return i == len(s)
        first_match = i < len(s) and (pattern[j] == s[i] or pattern[j] == ".")
        if (j + 1) < len(pattern) and pattern[j + 1] == "*":
            return backtrack(i, j + 2) or (first_match and backtrack(i + 1, j))
        return first_match and backtrack(i + 1, j + 1)

    return backtrack(0, 0)


def magic_square(n):
    """
    Generate a magic square using backtracking.

    Args:
        n (int): The size of the magic square (n x n).

    Returns:
        list: A 2D list representing the magic square.

    Raises:
        ValueError: If n is not a positive integer.
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")

    magic_sum = n * (n * n + 1) // 2
    square = [[0] * n for _ in range(n)]
    used = set()

    def is_valid(row, col, num):
        """Check if placing num at square[row][col] is valid."""
        if num in used:
            return False
        square[row][col] = num
        used.add(num)

        if all(square[row][c] != 0 for c in range(n)):
            if sum(square[row]) != magic_sum:
                square[row][col] = 0
                used.remove(num)
                return False

        if all(square[r][col] != 0 for r in range(n)):
            if sum(square[r][col] for r in range(n)) != magic_sum:
                square[row][col] = 0
                used.remove(num)
                return False

        if row == col and all(square[i][i] != 0 for i in range(n)):
            if sum(square[i][i] for i in range(n)) != magic_sum:
                square[row][col] = 0
                used.remove(num)
                return False

        if row + col == n - 1 and all(square[i][n - 1 - i] != 0 for i in range(n)):
            if sum(square[i][n - 1 - i] for i in range(n)) != magic_sum:
                square[row][col] = 0
                used.remove(num)
                return False

        return True

    def backtrack(row, col):
        """Backtracking helper function to generate the magic square."""
        if row == n:
            return True
        next_row, next_col = (row, col + 1) if col + 1 < n else (row + 1, 0)
        for num in range(1, n * n + 1):
            if is_valid(row, col, num):
                if backtrack(next_row, next_col):
                    return True
                square[row][col] = 0
                used.remove(num)
        return False

    backtrack(0, 0)
    return square


def main():
    """Demonstrate the backtracking algorithms."""
    print("N-Queens (n=4):", n_queens(4))
    sudoku = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ]
    sudoku_solver(sudoku)
    print("Sudoku solution")
    for row in sudoku:
        print(row)
    print("\nWord Search:", word_search([["A", "B"], ["C", "D"]], "ABCD"))
    print("\nSubset Sum:", subset_sum([1, 2, 3], 3))
    print("\nPermutations:", permutations([1, 2, 3]))
    print("\nRat in Maze:", rat_in_maze([[1, 0], [1, 1]]))
    print("\nHamiltonian Cycle:", hamiltonian_cycle([[0, 1, 1], [1, 0, 1], [1, 1, 0]]))
    print("\nKnight's Tour:", knights_tour(5))
    print("\nPalindrome Partitioning:", palindrome_partitioning("aab"))
    print("\nCombination Sum:", combination_sum([2, 3, 6, 7], 7))
    print("\nValid Parentheses:", all_possible_valid_parentheses(3))
    print("\nString Pattern Matching:", string_pattern_matching("aab", "c*a*b"))
    print("\nMagic Square (n=3):\n")
    for row in magic_square(3):
        print(row)


if __name__ == "__main__":
    main()
