import random
from utils.types import History, Move


class Strategy:
    def __init__(self):
        self.name = "thief"

    def begin(self) -> Move:
        return Move.STEAL

    def turn(self, history: History) -> Move:
        return Move.STEAL
