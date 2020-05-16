# Yorn is just a Y or N function
# To call it, use this: yorn.YORN("insert message to ask the user here")

import jrlib
import random
import time 

# This is a function that makes a message that says that one class has killed another. This is used extensivley after the battle begins.

def messageGet(teamWin, teamLoss, classWin, classLoss) :
    rand1 = random.randint(1, 5)

    if rand1 == 1:
        CVC = f"The {teamWin} {classWin} have destroyed the {teamLoss} {classLoss}!"
    elif rand1 == 2:
        CVC = f"The {teamWin} {classWin} have massacred the {teamLoss} {classLoss}!"
    elif rand1 == 3:
        CVC = f"The {teamLoss} {classLoss} have fallen to the {teamWin} {classWin}."
    elif rand1 == 4:
        CVC = f"The {teamLoss} {classLoss} has been killed by the {classWin} of the {teamWin} army!"
    elif rand1 == 5:
        CVC = f"The {teamWin} {classWin} have killed the {teamLoss} {classLoss}."
    return CVC

# Variables

blueScore = 0
redScore = 0
blueFScore = 0
redFScore = 0

# Start of actual program
print("Welcome to Battle Sim!")
name = input("What is your name? \n")
print(f"Hello {name}!")


while True:
    # Asking user for number of red foot soldiers
    while True:
        footRed = input("How many foot soldiers would you like in the red army? \n")
        try:
            int(footRed)
        except ValueError:
            print("Please enter a number next time.")
            continue
        break
    print(f"Ok! There will be {footRed} foot soldier(s) in the red army.")

    # Asking user for number of blue foot soldiers
    while True:
        footBlue = input("Next, how many foot soldiers would you like in the blue army? \n")
        try:
            int(footBlue)
        except ValueError:
            print("Please enter a number next time.")
            continue
        break

    # Asking user if the numbers are correct.
    if jrlib.YORN(f"There will be {footBlue} blue foot soldier(s) and {footRed} red foot soldier(s). Would you like to edit these numbers? (Y/N) \n") == 1:
        continue
    else:
        break

while True:
    # Asking user for number of red archers
    while True:
        archRed = input("How many archers would you like in the red army? \n")
        try:
            int(archRed)
        except ValueError:
            print("Please enter a number next time.")
            continue
        break
    print(f"Ok! There will be {archRed} archer(s) in the red army.")

    # Asking user for number of blue archers
    while True:
        archBlue = input("Next, how many archers would you like in the blue army? \n")
        try:
            int(archBlue)
        except ValueError:
            print("Please enter a number next time.")
            continue
        break

    # Asking user if the numbers are correct.
    if jrlib.YORN(f"There will be {archBlue} blue archer(s) and {archRed} red archer(s). Would you like to edit these numbers? (Y/N) \n") == 1:
        continue
    else:
        break

while True:
    # Asking user for number of red heavy soldiers
    while True:
        hardRed = input("How many heavy soldiers would you like in the red army? \n")
        try:
            int(hardRed)
        except ValueError:
            print("Please enter a number next time.")
            continue
        break
    print(f"Ok! There will be {hardRed} heavy soldier(s) in the red army.")

    # Asking user for number of blue heavy soldiers
    while True:
        hardBlue = input("Next, how many heavy soldiers would you like in the blue army? \n")
        try:
            int(hardBlue)
        except ValueError:
            print("Please enter a number next time.")
            continue
        break

    # Asking user if the numbers are correct.
    if jrlib.YORN(f"Blue army has {footBlue} foot soldier(s), {archBlue} archer(s), and {hardBlue} heavy soldier(s). Red army has {footRed} foot soldier(s), {archRed} archer(s) and {hardRed} heavy soldier(s). Would you like to start the battle? (Y/N)") == 1:
        break
    else:
        continue

print("Let the battle begin!")
print("Round 1")
time.sleep(1)
# Blue attacks!
print("Blue is attacking!")

message = messageGet("blue", "red", "archers", "foot soldiers")
if archBlue >= footRed:
    print(message)
    blueScore = blueScore + 1
else:
    print("The blue archers and the red foot soldiers are at a standstill.")
time.sleep(1)

message = messageGet("blue", "red", "heavy soldiers", "archers")
if hardBlue >= archRed:
    print(message)
    blueScore = blueScore + 1
else:
    print("The red heavy soldiers and the blue archers are at a standstill.")
time.sleep(1)

message = messageGet("blue", "red", "foot soldiers", "heavy soldiers")
if footBlue >= hardRed:
    print(message)
    blueScore = blueScore + 1
else:
    print("The blue foot soldiers and the red heavy soldiers are at a standstill")
time.sleep(1)

# Red attacks!
print("Red is attacking!")

message = messageGet("red", "blue", "archers", "foot soldiers")
if archBlue >= footRed:
    print(message)
    redScore = redScore + 1
else:
    print("The red archers and the blue foot soldiers are at a standstill.")
time.sleep(1)

message = messageGet("red", "blue", "heavy soldiers", "archers")
if hardBlue >= archRed:
    print(message)
    redScore = redScore + 1
else:
    print("The red heavy soldiers and the blue archers are at a standstill.")
time.sleep(1)

message = messageGet("red", "blue", "foot soldiers", "heavy soldiers")
if footBlue >= hardRed:
    print(message)
    redScore = redScore + 1
else:
    print("The red foot `1soldiers and the blue heavy soldiers are at a standstill.")
time.sleep(0.5)

if blueScore >= redScore :
    print("Blue wins!")
    blueFScore = blueFScore + 1
elif redScore >= blueScore :
    print("Red wins!")
    redFScore = redFScore + 1
else:
    print("It's A Tie!")

blueScore = 0
redScore = 0
time.sleep(0.5)

print("Round 2")
time.sleep(1)
# Blue attacks!
print("Blue is attacking!")

message = messageGet("blue", "red", "archers", "foot soldiers")
if archBlue >= footRed:
    print(message)
    blueScore = blueScore + 1
else:
    print("The blue archers and the red foot soldiers are at a standstill.")
time.sleep(1)

message = messageGet("blue", "red", "heavy soldiers", "archers")
if hardBlue >= archRed:
    print(message)
    blueScore = blueScore + 1
else:
    print("The red heavy soldiers and the blue archers are at a standstill.")
time.sleep(1)

message = messageGet("blue", "red", "foot soldiers", "heavy soldiers")
if footBlue >= hardRed:
    print(message)
    blueScore = blueScore + 1
else:
    print("The blue foot soldiers and the red heavy soldiers are at a standstill")
    
time.sleep(1)
# Red attacks!
print("Red is attacking!")

message = messageGet("red", "blue", "archers", "foot soldiers")
if archBlue >= footRed:
    print(message)
    redScore = redScore + 1
else:
    print("The red archers and the blue foot soldiers are at a standstill.")
time.sleep(1)

message = messageGet("red", "blue", "heavy soldiers", "archer")
if hardBlue >= archRed:
    print(message)
    redScore = redScore + 1
else:
    print("The red heavy soldiers and the blue archers are at a standstill.")
time.sleep(1)

message = messageGet("red", "blue", "foot soldiers", "heavy soldiers")
if footBlue >= hardRed:
    print(message)
    redScore = redScore + 1
else:
    print("The red foot soldiers and the blue heavy soldiers are at a standstill.")
time.sleep(0.5)

if blueScore >= redScore :
    print("Blue wins!")
    blueFScore = blueFScore + 1
elif redScore >= blueScore :
    print("Red wins!")
    redFScore = redFScore + 1
else:
    print("It's A Tie!")

blueScore = 0
redScore = 0
time.sleep(0.5)

print("Round 3")
time.sleep(1)
# Blue attacks!
print("Blue is attacking!")

message = messageGet("blue", "red", "archers", "foot soldiers")
if archBlue >= footRed:
    print(message)
    blueScore = blueScore + 1
else:
    print("The blue archers and the red foot soldiers are at a standstill.")
time.sleep(1)

message = messageGet("blue", "red", "heavy soldiers", "arch")
if hardBlue >= archRed:
    print(message)
    blueScore = blueScore + 1
else:
    print("The red heavy soldiers and the blue archers are at a standstill.")
time.sleep(1)

message = messageGet("blue", "red", "foot soldiers", "heavy soldiers")
if footBlue >= hardRed:
    print(message)
    blueScore = blueScore + 1
else:
    print("The blue foot soldiers and the red heavy soldiers are at a standstill.")

time.sleep(1)
# Red attacks!
print("Red is attacking!")

message = messageGet("red", "blue", "archers", "foot soldiers")
if archBlue >= footRed:
    print(message)
    redScore = redScore + 1
else:
    print("The red archers and the blue foot soldiers are at a standstill.")
time.sleep(1)

message = messageGet("red", "blue", "heavy soldiers", "arch")
if hardBlue >= archRed:
    print(message)
    redScore = redScore + 1
else:
    print("The red heavy soldiers and the blue archers are at a standstill.")
time.sleep(1)

message = messageGet("red", "blue", "foot soldiers", "heavy soldiers")
if footBlue >= hardRed:
    print(message)
    redScore = redScore + 1
else:
    print("The red foot soldiers and the blue heavy soldiers are at a standstill.")

time.sleep(0.5)

if blueScore >= redScore :
    print("Blue wins!")
    blueFScore = blueFScore + 1
elif redScore >= blueScore :
    print("Red wins!")
    redFScore = redFScore + 1
else:
    print("It's A Tie!")

blueScore = 0
redScore = 0
time.sleep(0.5)

if blueFScore >= redFScore :
    print("Blue wins all of the battles!")
elif redFScore >= blueFScore :
    print("Red wins all of the battles!")
else:
    print("It's a tie!")

input("Press enter to exit.")