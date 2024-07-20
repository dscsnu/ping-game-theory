import random
from utils.types import History, Move

class Strategy:
    def __init__(self):
        self.name = 'random'
    
    def begin(self) -> Move:
        return random.choice([Move.SPLIT, Move.STEAL])
    
    def turn(self, history:History) -> Move:
        return random.choice([Move.SPLIT, Move.STEAL])
