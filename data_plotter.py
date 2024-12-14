import matplotlib.pyplot as plt
from collections import Counter

from models.run_statistics import RunStatistics


def count_occurrences_with_range(data):
    """
    Counts the occurrences of each value in the given list.

    Args:
      data: The list of integers.

    Returns:
      A dictionary where keys are the values from the list 
      and values are their respective counts. 
      Includes all values within the range of the list, 
      with 0 for values that do not occur in the list.
    """
    min_val = min(data)
    max_val = max(data)
    occurrences = Counter(data)
    return {i: occurrences.get(i, 0) for i in range(min_val, max_val + 1)}


def plot_floors_reached(statistics: RunStatistics):
    """
    Plots a chart of the floors reached in each run.
    """
    floors_dict = count_occurrences_with_range(statistics.floors_reached_list)
    floors, counts = zip(*floors_dict.items())
    plt.figure(figsize=(10, 6))
    plt.bar(floors, counts)
    plt.xlabel("Floor")
    plt.ylabel("Number of Runs")
    plt.title("Frequency of Floors Reached")
    plt.xticks(floors)
    plt.grid(True)
    plt.show()
