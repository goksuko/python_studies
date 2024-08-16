from p12_module import logo_art
from p12_module import clear_screen
from colorama import Fore 
import random

clear_screen()
print(f"{Fore.CYAN}{logo_art}{Fore.RESET}")

attempt_left = 0
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
hardness = input("Choose a difficulty. Type 'easy' or 'hard': ")

if hardness == "easy":
  attempt_left = 10
else:
  attempt_left = 5

the_number = random.randint(1, 100)
answer = 0

while (answer != the_number	and attempt_left > 0):
    print(f"You have {attempt_left} attempts remaining to guess the number.")
    answer = int(input("Make a guess: \n"))
    if (answer == the_number):
       print(f"You got it! The answer was {the_number}.")
    elif (answer < the_number):
       print("Too low.\nGuess again.")
    elif (answer > the_number):
        print("Too high.\nGuess again.")
    attempt_left -= 1

if attempt_left == 0:
	print(f"You've run out of guesses, you lose. The answer was {the_number}.")	