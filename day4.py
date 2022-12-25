# Randomization

import random

random_integer = random.randint(1, 10)
print(random_integer)

random_float = random.random() * 5
print(random_float)

# Head or Tails

import random

heads_or_tails = random.randint(0, 1)

if heads_or_tails == 1:
    print("Heads")
else:
    print("Tails")

# Banker Roulette

import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

# num_items = len(names)
# random_choice = random.randint(0, num_items - 1)
# random_person = names[random_choice]

random_person = random.choice(names)

print(f"{random_person} is going to buy the meal today!")