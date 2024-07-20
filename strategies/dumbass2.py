import random
from utils.types import History, Move

class Strategy:

    def __init__(self):
        self.name = 'dumbass2'

    def begin(self):
        return Move.SPLIT


    def turn(self, history: History):
        y=0
        if len(history)>3:
            for i in range(3):
                if history[-i-1].opponent == Move.STEAL:
                    y+=1
            if y>=1:
                return Move.STEAL
            else:
                return Move.SPLIT
        else:
            return random.choice([Move.SPLIT, Move.STEAL])