# This is my first program.
# It's a madlibs program.
# Read the comments to see what stuff does.
# ?????????????????????????

# A R R A Y
profession = ["","","",""]

# Get input from user
print("Welcome user!")
print("Let's play a game...")
print("...of madlibs!")
neo = input("Please share with me your name.\n")

# Getting matrix variable from user
print(f"Hello {neo}! Are you ready?")
theMatrix = input("Question 1: What is somthing you want to know more about?\n")

# Getting system variable
print(f"So you want to know more about {theMatrix} huh?")
print(f"First, tell me what you already know about {theMatrix}")
system = input(f"What noun would you categorize {theMatrix} as? \n")

# Getting enemy variable from user
enemy = input(f"Give me an opposing noun to {system}.\n")

# Getting inside variable from user
inside = input("Now give me any relaxing noun (present tense)\n")

# Getting all 4 professions
print(f"Now i need 4 professions relating to {system}")

for i in range(len(profession)):
    profession[i] = input(f"Profession (plural) {i + 1} out of {len(profession)} \n")

save = input("Now give me a present tense verb.\n")
unplugged = input("And now a past tense verb. \n")
fight = input("One last verb, future tense \n")
input(f"Ok! I have made an extensive article on {theMatrix}! Press enter to see it! \n" )

# Print story
print(f"{theMatrix} is a {system}, {neo}. That {system} is our {enemy}. " +
f"But when you're {inside}, you look around, what do you see? " +
f"{profession[0]}, {profession[1]}, {profession[2]}, {profession[3]} " +
f"of the people we are trying to {save}. But until we do, " +
f"these people are still a part of that {system} and that makes " +
f"them our {enemy}. You have to understand, most of these people " +
f"are not ready to be {unplugged}. And many of them are so inured, " +
f"so hopelessly dependent on the {system}, that they will {fight} to protect it.")

input("Press enter to end the application. \n")