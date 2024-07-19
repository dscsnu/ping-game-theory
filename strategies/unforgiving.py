import random

class Strategy:

    def __init__(self):
        self.name = 'unforgiving'

    def begin(self):
        return 'split'
    
    def turn(self, history):
        
        has_stolen = False
        for i in history:
            if i.get('opponent') == 'steal':
                has_stolen = True
                break
        
        if has_stolen:
            return 'steal'
        return 'split'