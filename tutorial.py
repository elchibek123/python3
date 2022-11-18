character_name = "Tom"
character_age = 50
print("There once\nwas a man named " + character_name + ", ")
print("he was " + str(character_age) + " years old.")

character_name = "Mike"
print("He really liked the name " + character_name + ",")
print("but didn't like being " + str(character_age) + ".")

##############################################################

phrase = "Giraffe Academy"
print(phrase.upper().isupper())
print(len(phrase))
print(phrase[0])
print(phrase.index("a"))
print(phrase.replace("Giraffe", "Elephant"))

##############################################################

print(3 * (4 + 5))
print(10 % 3)

from math import *

my_num = -5
print(str(my_num))
print(abs(my_num))
print(pow(3, 2))
print(max(4, 6))
print(min(4, 6))
print(round(3.7))
print(floor(5.8))
print(ceil(5.8))
print(sqrt(36))

########################################################

# name = input("Enter your name: ")
# age = input("Enter your age: ")
# print("Hello " + name + "! You are " + age)

# num1 = input("Enter a number: ")
# num2 = input("Enter another number: ")

# result = int(num1) + int(num2)
# print(result)

# result = float(num1) + float(num2)
# print(result)

################################ Mad Libs Game ##############################

# color = input("Enter a color: ")
# plural_noun = input("Enter a Plural Noun: ")
# celebrity = input("Enter a celebrity: ")

# print("Roses are " + color)
# print(plural_noun + " are blue")
# print("I love " + celebrity)

################################ Lists ######################################

friends = ["Kevin", "Karen", "Jim", "Oscar", "Tobby"]

print(friends[-2])
print(friends[1:])
print(friends[1:3])

friends[-2] = "Mike"
print(friends[-2])

################################# Lists Funcrions ################################

lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Tobby"]
# friends.extend(lucky_numbers)
friends.append("Creed")
friends.insert(1, "Kelly")
friends.remove("Jim")
friends.reverse()
# friends.sort()
# friends.pop()     # removes last item
# friends.clear()

print(friends)

friends2 = friends.copy()

print(friends2)

##################################### Tuples #########################################

coordinates = (4, 5) # values can't be changed in tuples

print(coordinates[0])

##################################### Functions ######################################

def say_hi(name, age):
    print("Hello " + name + ", you are " + age)

print("Top")
say_hi("Mike", "35")
say_hi("Steve", "70")
print("Buttom")

###################################### Return Statements ###############################

def cube(num):
    return num*num*num

result = cube(4)
print(result)

######################################## If Statemets ##################################

is_male = False
is_tall = True

if is_male or is_tall:
    print("You are a male or tall or both")
else:
    print("You neither male nor tall")


if is_male and is_tall:
    print("You are a tall male")
elif is_male and not(is_tall):
    print("You are a short male")
elif not(is_male) and is_tall:
    print("You are not a male but are tall")
else:
    print("You are not a male and not tall")

################################## If Statements & Comparisons ###############################

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:     # != not equeal
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(3, 4, 5))

################################# Building a Better Calculator #################################

num1 = float(input("Enter first number: "))
op = input("Enter operator: ")
num2 = float(input("Enter second number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("Invalid operator")