import random

class genNum:
    
    def __init__(self,list):
         self.list = list
    
    def generatingNumber(self):
        random.shuffle(self.list)
        number = self.list[0:4]
        return number

        

            


