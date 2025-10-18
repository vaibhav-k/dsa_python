"""
algorithms.greedy
=================

This module contains implementations of various greedy algorithms.

Functions:
    coin_change(coins, amount): Solve the coin change problem using a greedy approach.
    interval_scheduling(intervals): Solve the interval scheduling problem using a greedy approach.
    job_sequencing(jobs, deadlines, profits): Solve the job sequencing problem using a greedy approach.
    huffman_coding(symbols, frequencies): Generate Huffman codes for given symbols using a greedy approach.
    train_station_scheduling(trains): Schedule trains at a station using a greedy approach.
    egyptian_fraction(numerator, denominator): Represent a fraction as an Egyptian fraction using a greedy approach.
    gas_station_problem(stations, tank_capacity): Solve the gas station problem using a greedy approach.
    largest_number(arr): Form the largest number from an array of numbers using a greedy approach.
    dijkstra(graph, start): Find the shortest path in a graph using Dijkstra's algorithm (greedy approach).

Constants:
    GREEDY_ALGORITHM_PROPERTIES: Description of the properties of greedy algorithms.

Author:
    Vaibhav Kulshrestha

Date:
    2025-10-18
"""

GREEDY_ALGORITHM_PROPERTIES = [
    "Greedy choice property: A global optimum can be arrived at by selecting a local optimum.",
    "Optimal substructure: An optimal solution to the problem contains optimal solutions to its subproblems.",
]


def coin_change(coins, amount):
    """
    Solve the coin change problem using a greedy approach.

    Args:
        coins (list): List of coin denominations (must be positive integers).
        amount (int): The target amount to make change for.

    Returns:
        list: List of coins that make up the target amount, or an empty list if no solution exists.

    Raises:
        ValueError: If amount is negative or coins contain non-positive integers.
    """
    if amount < 0 or not isinstance(amount, int):
        raise ValueError("Amount must be a non-negative integer.")
    if any(coin <= 0 for coin in coins) or not all(
        isinstance(coin, int) for coin in coins
    ):
        raise ValueError("Coin denominations must be positive integers.")
    coins = sorted(coins, reverse=True)
    result = []

    # Iterate through coin denominations and use as many as possible
    for coin in coins:
        while amount >= coin:
            amount -= coin
            result.append(coin)
    if amount == 0:
        return result
    else:
        return []  # No solution found


def interval_scheduling(intervals):
    """
    Solve the interval scheduling problem using a greedy approach.

    Args:
        intervals (list of tuples): List of intervals represented as (start, end).

    Returns:
        list of tuples: Maximum set of non-overlapping intervals.

    Raises:
        ValueError: If intervals are not in the correct format.
    """
    if not isinstance(intervals, list) or not all(
        isinstance(i, tuple) and len(i) == 2 for i in intervals
    ):
        raise ValueError("Intervals must be a list of tuples (start, end).")
    if not intervals:
        return []
    sorted_intervals = sorted(intervals, key=lambda x: x[1])
    selected_intervals = []
    last_end_time = float("-inf")

    # Iterate through sorted intervals and select non-overlapping ones
    for interval in sorted_intervals:
        if interval[0] >= last_end_time:
            selected_intervals.append(interval)
            last_end_time = interval[1]

    return selected_intervals


def job_sequencing(jobs, deadlines, profits):
    """
    Solve the job sequencing problem using a greedy approach.

    Args:
        jobs (list): List of job identifiers.
        deadlines (list): List of deadlines for each job.
        profits (list): List of profits for each job.

    Returns:
        list: Sequence of jobs that maximizes profit within deadlines.

    Raises:
        ValueError: If input lists are not of the same length.
    """
    if not (len(jobs) == len(deadlines) == len(profits)):
        raise ValueError(
            "Jobs, deadlines, and profits lists must be of the same length."
        )
    if not jobs:
        return []
    job_info = sorted(zip(jobs, deadlines, profits), key=lambda x: x[2], reverse=True)
    max_deadline = max(deadlines)
    result = [None] * max_deadline
    total_profit = 0

    # Iterate through jobs and schedule them
    for job, deadline, profit in job_info:
        for j in range(min(deadline, max_deadline) - 1, -1, -1):
            if result[j] is None:
                result[j] = job
                total_profit += profit
                break

    return [job for job in result if job is not None]


def huffman_coding(symbols, frequencies):
    """
    Generate Huffman codes for given symbols using a greedy approach.

    Args:
        symbols (list): List of symbols.
        frequencies (list): List of frequencies for each symbol.

    Returns:
        dict: Dictionary mapping symbols to their Huffman codes.

    Raises:
        ValueError: If input lists are not of the same length.
    """
    import heapq

    if len(symbols) != len(frequencies):
        raise ValueError("Symbols and frequencies lists must be of the same length.")
    if not symbols:
        return {}

    heap = [[weight, [symbol, ""]] for symbol, weight in zip(symbols, frequencies)]
    heapq.heapify(heap)

    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = "0" + pair[1]
        for pair in hi[1:]:
            pair[1] = "1" + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])

    huffman_codes = {}
    for pair in heap[0][1:]:
        huffman_codes[pair[0]] = pair[1]
    return huffman_codes


def train_station_scheduling(trains):
    """
    Schedule trains at a station using a greedy approach.

    Args:
        trains (list of tuples): List of trains represented as (arrival_time, departure_time).

    Returns:
        int: Maximum number of trains that can be scheduled without overlap.

    Raises:
        ValueError: If trains are not in the correct format.
    """
    if not isinstance(trains, list) or not all(
        isinstance(t, tuple) and len(t) == 2 for t in trains
    ):
        raise ValueError(
            "Trains must be a list of tuples (arrival_time, departure_time)."
        )
    if not trains:
        return 0
    sorted_trains = sorted(trains, key=lambda x: x[1])
    count = 0
    last_departure_time = float("-inf")

    # Iterate through sorted trains and schedule non-overlapping ones
    for train in sorted_trains:
        if train[0] >= last_departure_time:
            count += 1
            last_departure_time = train[1]

    return count


def egyptian_fraction(numerator, denominator):
    """
    Represent a fraction as an Egyptian fraction using a greedy approach.

    Args:
        numerator (int): Numerator of the fraction.
        denominator (int): Denominator of the fraction.

    Returns:
        list: List of denominators of the unit fractions.

    Raises:
        ValueError: If numerator or denominator are not positive integers.
    """
    if (
        numerator <= 0
        or denominator <= 0
        or not isinstance(numerator, int)
        or not isinstance(denominator, int)
    ):
        raise ValueError("Numerator and denominator must be positive integers.")
    result = []

    # Iterate to find unit fractions
    while numerator != 0:
        x = -(-denominator // numerator)  # Ceiling division
        result.append(x)
        numerator = numerator * x - denominator
        denominator = denominator * x

    return result


def gas_station_problem(stations, tank_capacity):
    """
    Solve the gas station problem using a greedy approach.

    Args:
        stations (list of tuples): List of gas stations represented as (distance, fuel).
        tank_capacity (int): Maximum fuel capacity of the vehicle.

    Returns:
        int: Minimum number of refueling stops needed to reach the destination, or -1 if not possible.

    Raises:
        ValueError: If tank_capacity is not a positive integer.
    """
    if tank_capacity <= 0 or not isinstance(tank_capacity, int):
        raise ValueError("Tank capacity must be a positive integer.")
    stations.append((float("inf"), 0))  # Destination
    stations.sort()
    fuel = tank_capacity
    prev_distance = 0
    stops = 0
    max_heap = []
    import heapq

    # Iterate through stations and manage refueling
    for distance, fuel_available in stations:
        fuel -= distance - prev_distance
        while fuel < 0 and max_heap:
            fuel += -heapq.heappop(max_heap)
            stops += 1
        if fuel < 0:
            return -1
        heapq.heappush(max_heap, -fuel_available)
        prev_distance = distance

    return stops


def largest_number(arr):
    """
    Form the largest number from an array of numbers using a greedy approach.

    Args:
        arr (list): List of non-negative integers.

    Returns:
        str: The largest number formed by concatenating the integers.

    Raises:
        ValueError: If arr contains negative integers.
    """
    if any(num < 0 for num in arr):
        raise ValueError("Array must contain non-negative integers only.")
    from functools import cmp_to_key

    def compare(x, y):
        return int(y + x) - int(x + y)

    # Convert integers to strings for comparison
    arr_str = list(map(str, arr))
    arr_str.sort(key=cmp_to_key(compare))
    largest_num = "".join(arr_str)
    return "0" if largest_num[0] == "0" else largest_num


def dijkstra(graph, start):
    """
    Find the shortest path in a graph using Dijkstra's algorithm (greedy approach).

    Args:
        graph (dict): Adjacency list representation of the graph.
        start: Starting node.

    Returns:
        dict: Shortest distance from start to each node.

    Raises:
        ValueError: If graph is not in the correct format or start node is not in the graph.
    """
    import heapq

    if not isinstance(graph, dict):
        raise ValueError("Graph must be represented as an adjacency list (dictionary).")
    if start not in graph:
        raise ValueError("Start node must be present in the graph.")
    distances = {node: float("inf") for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    # Iterate through the graph to find the shortest paths
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        if current_distance > distances[current_node]:
            continue
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    return distances


def main():
    """
    Function to demonstrate greedy algorithms.
    """
    # Example usage of coin_change
    coins = [1, 5, 10, 25]
    amount = 63
    print("Coin Change:", coin_change(coins, amount))

    # Example usage of interval_scheduling
    intervals = [(1, 3), (2, 5), (4, 6), (6, 7)]
    print("\nInterval Scheduling:", interval_scheduling(intervals))

    # Example usage of job_sequencing
    jobs = ["a", "b", "c", "d"]
    deadlines = [2, 1, 2, 1]
    profits = [100, 19, 27, 25]
    print("\nJob Sequencing:", job_sequencing(jobs, deadlines, profits))

    # Example usage of huffman_coding
    symbols = ["a", "b", "c", "d"]
    frequencies = [5, 9, 12, 13]
    print("\nHuffman Coding:", huffman_coding(symbols, frequencies))

    # Example usage of train_station_scheduling
    trains = [(900, 910), (940, 1200), (950, 1120), (1100, 1130)]
    print("\nTrain Station Scheduling:", train_station_scheduling(trains))

    # Example usage of egyptian_fraction
    numerator = 2
    denominator = 3
    print("\nEgyptian Fraction:", egyptian_fraction(numerator, denominator))

    # Example usage of gas_station_problem
    stations = [(0, 4), (2, 2), (5, 3), (6, 4)]
    tank_capacity = 5
    print("\nGas Station Problem:", gas_station_problem(stations, tank_capacity))

    # Example usage of largest_number
    arr = [3, 30, 34, 5, 9]
    print("\nLargest Number:", largest_number(arr))

    # Example usage of dijkstra
    graph = {
        "A": {"B": 1, "C": 4},
        "B": {"A": 1, "C": 2, "D": 5},
        "C": {"A": 4, "B": 2, "D": 1},
        "D": {"B": 5, "C": 1},
    }
    print("\nDijkstra:", dijkstra(graph, "A"))


if __name__ == "__main__":
    main()
