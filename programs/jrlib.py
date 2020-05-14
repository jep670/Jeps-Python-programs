import random

# Y or N question function
def YORN (message):
    while True:
        output = input(message)
        if output.lower() == "y":
            return 1
        elif output.lower() == "n":
            return 0
        print(f"{output} was not an option. Please type Y or N next time.")