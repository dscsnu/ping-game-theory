import random
from utils.types import History, Move

class Strategy:
    def __init__(self):
        self.name = "rainman"
        self.split_probability = 0.6  # Start with 60% chance to split
        self.steal_probability = 1 - self.split_probability

    def begin(self):
        """Initial move with 60% chance to split."""
        return Move.SPLIT if random.random() < self.split_probability else Move.STEAL

    def turn(self, history: History):
        """
        Decide the next move based on the game history and adjust probabilities.
        
        :param history: List of tuples containing (my_move, opponent_move) for each turn
        :return: Move.SPLIT or Move.STEAL
        """
        if history:
            last_turn = history[-1]
            self._adjust_probabilities(last_turn)

        # Make decision based on current probabilities
        return Move.SPLIT if random.random() < self.split_probability else Move.STEAL

    def _adjust_probabilities(self, last_turn):
        """
        Adjust split and steal probabilities based on the outcome of the last turn.
        
        :param last_turn: Tuple of (my_move, opponent_move) from the last turn
        """
        my_move, opponent_move = last_turn.you, last_turn.opponent

        if my_move == Move.SPLIT and opponent_move == Move.STEAL:
            # Increase steal probability if we split and opponent stole
            self.steal_probability = min(self.steal_probability * 1.5, 0.8)
        elif my_move == Move.STEAL and opponent_move == Move.SPLIT:
            # Slightly reduce steal probability if we successfully stole
            self.steal_probability *= 0.9
        elif my_move == opponent_move == Move.SPLIT:
            # Slightly increase steal probability if we both split
            self.steal_probability = min(self.steal_probability * 1.1, 0.8)
        elif my_move == opponent_move == Move.STEAL:
            # Reduce steal probability if we both stole
            self.steal_probability *= 0.8

        # Ensure probabilities are valid
        self.steal_probability = max(0.2, min(self.steal_probability, 0.8))
        self.split_probability = 1 - self.steal_probability