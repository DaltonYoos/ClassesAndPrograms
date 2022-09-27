import random


class Insect:

    def __init__(self,w,l):

       self.wings = w
       self.legs = l
       self.flight = 0 
    
    #Be careful not to name attributes and methods the same thing, i.e. flight

    def calc_flight(self):
        self.flight = random.randint(1,10)
    
    def get_flight(self):
        return self.flight