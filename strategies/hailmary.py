from utils.types import History, Move

class Strategy:
    def __init__(self):
        self.name = 'hailmary'
        self.steal_count = 0
        self.consecutive_splits = 0
        self.times_to_steal = 0

    def begin(self) -> Move:
        return Move.SPLIT

    def turn(self, history: History) -> Move:
        # self.steal_count = 0
        # self.consecutive_splits = 0
        # self.times_to_steal = 0

        if history:
            last_entry = history[-1]
            if last_entry.opponent == Move.STEAL:
                self.steal_count += 1
                self.consecutive_splits = 0
                if self.steal_count == 1:
                    self.times_to_steal = 1
                elif self.steal_count == 2:
                    self.times_to_steal = 2
                elif self.steal_count >= 3:
                    self.times_to_steal = 4
            elif last_entry.opponent == Move.SPLIT:
                self.consecutive_splits += 1
            
            if last_entry.you == Move.STEAL:
                self.times_to_steal -= 1

        # Rest of the logic remains the same
        if self.times_to_steal > 0:
            return Move.STEAL
        elif self.consecutive_splits >= 2:
            return Move.SPLIT
        else:
            return Move.SPLIT