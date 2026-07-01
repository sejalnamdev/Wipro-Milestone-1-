# Create a dictionary
people = {
    "Jeff": "Is afraid of Dogs.",
    "David": "Plays the piano.",
    "Jason": "Can fly an airplane."
}

# Display the dictionary
for name, fact in people.items():
    print(f"{name}: {fact}")

print()

# Change Jeff's fact
people["Jeff"] = "Is afraid of heights."

# Add a new person
people["Jill"] = "Can hula dance."

# Display the updated dictionary
for name, fact in people.items():
    print(f"{name}: {fact}")



#OUTPUT:
Jeff: Is afraid of Dogs.
David: Plays the piano.
Jason: Can fly an airplane.

Jeff: Is afraid of heights.
David: Plays the piano.
Jason: Can fly an airplane.
Jill: Can hula dance.