import random
from colorama import Fore

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer = random.randint(0, 2)
games_list = [rock, paper, scissors]
if player == computer:
	result = "It's a draw!"
elif (player == 0 and computer == 2) or (player == 1 and computer == 0) or (player == 2 and computer == 1):
	result = "You won!"
else:
	result = "You lose!"

if player >=3 or player < 0:
	print("Please write a valid number!")
else:
	print(f"You chose:{games_list[player]}\n\nComputer chose:{games_list[computer]}\n\n{Fore.BLUE}{result}\n\n")


