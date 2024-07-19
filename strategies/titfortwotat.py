# import random
SPLIT = "split"
STEAL = "steal"


class Strategy:

    def __init__(self):
        self.name = 'Tit for two tat'

    def begin(self):
        return 'split'

    def turn(self, history):
        if len(history) < 2:
            return SPLIT
        last, second_last = history[-1]["opponent"], history[-2]["opponent"]

        if last == STEAL and second_last == STEAL:
            return STEAL
        return SPLIT