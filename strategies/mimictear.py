import random
from utils.types import History, Move

class Strategy:
    def __init__(self):
        self.name = "mimictear"
        self.initial_split_probability = 0.5

    def begin(self):
        """Initial move with 50% chance to split."""
        return Move.SPLIT if random.random() < self.initial_split_probability else Move.STEAL

    def turn(self, history: History):
        """
        Decide the next move based on the game history, mimicking the opponent's last move.
        
        :param history: List of tuples containing (my_move, opponent_move) for each turn
        :return: Move.SPLIT or Move.STEAL
        """
        if not history:
            return self.begin()

        last_turn = history[-1]
        return last_turn.opponent
