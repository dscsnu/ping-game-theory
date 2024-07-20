# import random
from utils.types import History, Move


class Strategy:

    def __init__(self):
        self.name = "titfortwotat"

    def begin(self) -> Move:
        return Move.SPLIT

    def turn(self, history: History) -> Move:
        if len(history) < 2:
            return Move.SPLIT
        last, second_last = history[-1].opponent, history[-2].opponent

        if last == Move.STEAL and second_last == Move.STEAL:
            return Move.STEAL
        return Move.SPLIT
