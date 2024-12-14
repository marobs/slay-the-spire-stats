from typing import List

from .run_data import RunData


class RunStatistics:
    runs: List[RunData]
    floors_reached_list: List[int]

    def __init__(self, runs: List[RunData]):
        self.runs = runs
        self.floors_reached_list = self.get_floors_reached()

    def get_floors_reached(self):
        """Returns the floors reached"""
        if not self.runs:
            return []
        return [run.floor_reached for run in self.runs]

    def get_average_floor_reached(self):
        """Calculates the average floor reached across all runs."""
        if not self.runs:
            return 0.0
        return sum(run.floor_reached for run in self.runs) / len(self.runs)

    def get_win_rate(self):
        """Calculates the win rate (percentage of victorious runs)."""
        if not self.runs:
            return 0.0
        wins = sum(1 for run in self.runs if run.victory)
        return wins / len(self.runs) * 100

    def get_most_common_character(self):
        """Determines the most frequently played character."""
        character_counts = {}
        for run in self.runs:
            character_counts[run.character_chosen] = character_counts.get(
                run.character_chosen, 0) + 1
        return max(character_counts, key=character_counts.get)
