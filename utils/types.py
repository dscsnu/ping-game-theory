from enum import Enum
from typing import List, NamedTuple, Tuple


class Move(Enum):
    SPLIT = "split"
    STEAL = "steal"


class HistoryEntry(NamedTuple):
    opponent: Move
    you: Move


MutableHistory = List[HistoryEntry]
History = Tuple[HistoryEntry, ...]


class Strategy:
    def __init__(self):
        self.name: str = "sample"

    def begin(self) -> Move:
        """
            Logic for the first move of any showdown.
            Is only run once on the initial run.

            return
                `Move`
        """
        return Move.SPLIT

    def turn(self, history: History) -> Move:
        """
            Logic for any move in the showdown after the first move.
            Is run every time except on the initial run.

            arguments
                `history`: `History`
        
            return
                `Move`
        """
        return Move.SPLIT
