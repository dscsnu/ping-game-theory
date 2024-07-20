import random
from utils.types import History, Move

class Strategy:
    def __init__(self):
        self.name = "gideon" # SIR GIDEON OFNIR, THE ALL KNOWING
        self.cooperation_threshold = 0.7
        self.forgiveness_rate = 0.1

    def begin(self):
        return Move.SPLIT

    def turn(self, history: History):
        if not history:
            return self.begin()

        opponent_moves = [entry.opponent for entry in history]
        total_moves = len(opponent_moves)
        opponent_split_ratio = opponent_moves.count(Move.SPLIT) / total_moves

        if opponent_split_ratio >= self.cooperation_threshold:
            return Move.SPLIT
        elif opponent_split_ratio < self.cooperation_threshold:
            if random.random() < self.forgiveness_rate:
                return Move.SPLIT
            else:
                return Move.STEAL

        return Move.SPLIT