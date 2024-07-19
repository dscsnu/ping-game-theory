import random

class Strategy:

    def __init__(self):
        self.name = 'dumbass'

    def begin(self):
        return 'split'
            
    
    def turn(self, history):
        y=0
        if len(history)>3:
            for i in range(3):
                if history[-i-1]["opponent"] =='steal':
                    y+=1
            if y>=2:    
                return 'steal'
            else:
                return 'split'
        else:
            if y < 2:
                return random.choice(['split', 'steal'])
            return 'split'