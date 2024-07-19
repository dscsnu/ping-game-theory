import random

class Strategy:

    def __init__(self):
        self.name = 'titfortat'

    def begin(self):
        return 'split'
    
    def turn(self, history):
        if (history[-1].get('opponent') == 'split'):
            return 'split'
        return 'steal'
