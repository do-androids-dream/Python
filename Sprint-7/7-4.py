"""
Imagine we have a washing machine which can wash the clothes, rinse the clothes and spin 
the clothes but all the tasks separately. We need a system that can automate the whole task 
without the disturbance or interference of us. 

To solve the above-described problem, we would like to hire the Facade Method. 
It will help us to hide or abstract the complexities of the subsystems as follows.

Note: the methods wash(), rinse() and spin() provide the output of the appropriate operation.
"""
class WashingMachine:
    def __init__(self):
        self.washing = washing
        self.rinsing = rinsing
        self.spinning = spinning
    
    def startWashing(self):
        self.washing()
        self.rinsing()
        self.spinning()

def washing():
    print("Washing...")

def rinsing():
    print("Rinsing...")

def spinning():
    print("Spinning...")

washingMachine = WashingMachine()
washingMachine.startWashing()
# Washing...
# Rinsing...
# Spinning...