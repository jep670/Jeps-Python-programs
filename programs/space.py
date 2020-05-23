import jrlib
import random
import sys

workers = []

# Classes

class Worker: 
    def __init__(self):
        global workers
        self.name = jrlib.generate_word(random.randint(3, 6))
        self.status = "alive"
        self.maxHealth = 100
        self.health = 100
        workers.append(self)
    def damage(self, damageTaken):
        self.health = self.health - damageTaken
    def heal(self, healthHealed):
        self.health = self.health + healthHealed
    def attack(self, target):
        target.damage(random.randint(10, 25))

class Alien:
    def __init__(self):
        self.name = jrlib.generate_word(random.randint(1, 10))
        self.maxHealth = random.randint(50, 120)
        self.health = self.maxHealth
        self.HEA = random.randint(21, 28)
        self.LEA = random.randint(10, 20)
    def damage(self, damageTaken):
        self.health = self.health - damageTaken  
    def attack(self, target):
        target.damage(random.randint(self.LEA, self.HEA))

class Station:
    def __init__(self):
        self.food = 21
        self.oxygen = 100
        self.day = 1

# Start

if jrlib.YORN("Would you like to start the game? (Y/N)") == 1:
    pass
else:
    sys.exit()

stationName = input("What would you like to name your station?")

station = Station()

for _ in range(3):
    Worker()

print(len(workers))
print(workers)

print(f"Day {station.day}")
print(f"{workers[0].name} is {workers[0].status}")

input("")