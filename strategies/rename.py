import random
import math
import numpy

from utils.types import History, Move

class Strategy:
    def __init__(self) -> None:
        self.name = ''
        self.description = ''
    
    def begin(self) -> Move:
        """
            Logic for the first move of any showdown.
            Is only run once on the initial run.

            return
                Move
        """
        
        return Move.SPLIT
        pass

    def turn(self, history: History) -> Move:
        """
            Logic for any move in the showdown after the first move.
            Is run every time except on the initial run.

            arguments
                history: History
  
            return
                Move
        """
        return Move.SPLIT