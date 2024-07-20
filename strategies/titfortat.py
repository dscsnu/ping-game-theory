import random
from utils.types import History, Move


class Strategy:

    def __init__(self):
        self.name = "titfortat"

    def begin(self) -> Move:
        return Move.SPLIT

    def turn(self, history: History) -> Move:
        if history[-1].opponent == Move.SPLIT:
            return Move.SPLIT
        return Move.STEAL
