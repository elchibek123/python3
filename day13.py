# First solution

from random import randint

random_number = randint(1, 100)

print(f"""Welcome to the Number Guessing Game!
I am thinking of a number between 1 and 100.
Pssst, the correct answer is 86""")
guess = input(f"Choose a difficulty. Type 'easy' or 'hard': ")

if guess == 'easy':
    print("You have 10 attempts remaining to guess the number.")
    game_should_continue = True
    attempts = 10
    while game_should_continue and attempts > 0:
        easy_guess = input("Make a guess: ")
        if int(easy_guess) == random_number:
            print(f"You got it! The answer was {random_number}")
            game_should_continue = False
            break
        else:
            if int(easy_guess) < random_number:
                if attempts == 1:
                    print("Too low.")
                else:
                    print("Too low.")
                    print("Gues again.")
                    print(f"You have {attempts - 1} remaining to guess the number.")
            elif int(easy_guess) > random_number:
                if attempts == 1:
                    print("Too high.")
                else:
                    print("Too high.")
                    print("Gues again.")
                    print(f"You have {attempts - 1} remaining to guess the number.")
            attempts -= 1

    if attempts == 0:
        print("You've run out of guesses, you lose!")
    else:
        game_should_continue = True
elif guess == "hard":
    print("You have 5 attempts remaining to guess the number.")
    game_should_continue = True
    attempts = 5
    while game_should_continue and attempts > 0:
        if attempts == 0:
            print("You've run out of guesses, you lose!")
            game_should_continue = False
            break
        else:
            easy_guess = input("Make a guess: ")
            if int(easy_guess) == random_number:
                print(f"You got it! The answer was {random_number}")
                break
            else:
                if int(easy_guess) < random_number:
                    if attempts == 1:
                        print("Too low.")
                    else:
                        print("Too low.")
                        print("Gues again.")
                        print(f"You have {attempts - 1} remaining to guess the number.")
                elif int(easy_guess) > random_number:
                    if attempts == 1:
                        print("Too high.")
                    else:
                        print("Too high.")
                        print("Gues again.")
                        print(f"You have {attempts - 1} remaining to guess the number.")
                attempts -= 1

    if attempts == 0:
        print("You've run out of guesses, you lose!")
    else:
        game_should_continue = True


# Second solution


from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(guess, answer, turns):
  """checks answer against guess. Returns the number of turns remaining."""
  if guess > answer:
    print("Too high.")
    return turns - 1
  elif guess < answer:
    print("Too low.")
    return turns - 1
  else:
    print(f"You got it! The answer was {answer}.")

def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS

def game():
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  answer = randint(1, 100)
  print(f"Pssst, the correct answer is {answer}") 

  turns = set_difficulty()
  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")

    guess = int(input("Make a guess: "))

    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("You've run out of guesses, you lose.")
      return
    elif guess != answer:
      print("Guess again.")


game()
