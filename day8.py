# Paint Area Calculator

import math

def paint_calc(height, width, cover):
    area = test_h * test_w
    num_of_cans = math.ceil(area / coverage)
    print(f"You'll need {num_of_cans} cans of paint.")

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

# Prime Number Checker

def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

n = int(input("Check this number: "))
prime_checker(number=n)