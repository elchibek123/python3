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

# Treasure Map

row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

horizontal = int(position[0])
vertical = int(position[1])

map[vertical - 1][horizontal -1] = "X "

print(f"{row1}\n{row2}\n{row3}")