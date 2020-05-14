import random
import string


# Y or N question function
def YORN(message):
    while True:
        output = input(message)
        if output.lower() == "y":
            return 1
        elif output.lower() == "n":
            return 0
        print(f"{output} was not an option. Please type Y or N next time.")


# Generate a random word composed of random characters
def generate_word(length):
    output_word = ""
    for _ in range(length):
        output_word = output_word + random.choice(string.ascii_lowercase)
    return output_word
