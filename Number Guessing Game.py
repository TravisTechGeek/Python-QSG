# Number Guessing Game
# 
from random import seed
from random import randint
number = randint(1, 100) # Random number between 1 and 100
guess = 0
while guess != number:
    guess = int(input("Enter your guess (1-100): "))
    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You've guessed the number.")
        
