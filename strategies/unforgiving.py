import random

class Strategy:

    def __init__(self):
        self.name = 'unforgiving'

    def begin(self):
        return 'split'
    
    def turn(self, history):
        if history[-1].get('opponent') == 'steal' or history[-1].get('you') == 'steal':
            return 'steal'
        return 'split'