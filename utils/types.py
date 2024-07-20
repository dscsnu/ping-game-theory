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
        return Move.SPLIT

    def turn(self, history: History) -> Move:
        return Move.SPLIT
