import random
from utils.types import History, Move

class Strategy:

    def __init__(self):
        self.name = 'pushover'

    def begin(self) -> Move:
        return Move.SPLIT
    
    def turn(self, history: History) -> Move:
        return Move.SPLIT