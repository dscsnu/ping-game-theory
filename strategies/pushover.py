import random

class Strategy:

    def __init__(self):
        self.name = 'pushover'

    def begin(self):
        return 'split'
    
    def turn(self, history):
        return 'split'