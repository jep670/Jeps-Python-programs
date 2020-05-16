import jrlib
import random
import sys

# Classes

class Worker: 
    def __init__(self):
        self.name = jrlib.generate_word(random.randint(3, 6))
        self.status
        self.maxhealth
        self.health
        self.food

# Variables

# Station variables
station.food
station.oxygen
station.day

# Worker 1
worker1.status = "alive"
worker1.health = 100
worker1.food = 100
worker1.name = jrlib.generate_word(random.randint(3, 6))

# Worker 2
worker2.status = "alive"
worker2.health = 100
worker2.food = 100
worker2.name = jrlib.generate_word(random.randint(4, 7))

# Worker 3
worker3.status = "alive"
worker3.health = 100
worker3.food = 100
worker3.name = jrlib.generate_word(random.randint(3, 5))

# Start

if jrlib.YORN("Would you like to start the game? (Y/N)") == 1:
    pass
else:
    sys.exit()

