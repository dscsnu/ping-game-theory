import random

class Strategy:

    def __init__(self):
        self.name = 'thief'

    def begin(self):
        return 'steal'
    
    def turn(self, history):
        return 'steal'