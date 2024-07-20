import random
from utils.types import History, Move


class Strategy:

    def __init__(self):
        self.name = "unforgiving"

    def begin(self) -> Move:
        return Move.SPLIT

    def turn(self, history: History) -> Move:
        if history[-1].opponent == Move.STEAL or history[-1].you == Move.STEAL:
            return Move.STEAL
        return Move.SPLIT
