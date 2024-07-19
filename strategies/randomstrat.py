import random

class Strategy:
    def __init__(self):
        self.name = 'random'
    
    def begin(self):
        return random.choice(['split', 'steal'])
    
    def turn(self, history):
        return random.choice(['split', 'steal'])
