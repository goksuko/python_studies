import random

from p07_module import logo
from p07_module import hangman
from p07_module import word_list
from colorama import Fore
from colorama import Back

			
print(logo)

# word_of_game = word_list[random.randint(0, len(word_list) - 1)]
word_of_game = random.choice(word_list)
print(f"Psst! You are gonna find {word_of_game}.\n")
length = len(word_of_game)
# result = ["_"] * length  # Initialize result as a list of underscores
result = []
# for letter in word_of_game:
for _ in range(length):
	result += "_"
print(f"{' '.join(result)}")

end_of_game = False
index = 0

while not end_of_game:
	guessed_letter = input("\nPlease guess a letter: ").lower()

	if guessed_letter in result:
		print(f"\nYou've already guessed {guessed_letter}.")
	else:
		# for letter in word_of_game:
		for position in range(length):
			letter = word_of_game[position]
			if guessed_letter == letter:
				result[position] = letter

	if guessed_letter not in word_of_game:
		index += 1
		print(f"\n{Fore.RED}{guessed_letter} is not in the word, sorry :({Fore.RESET}")
	
	if index == 6:
		end_of_game = True
		print(f"{Fore.RED}{hangman[index]}{Fore.RESET}")
		print(f"{Back.RED}\nYou lose!{Back.RESET}\n")

	#Join all the elements in the list and turn it into a String.
	if not end_of_game:
		print(f"\n{' '.join(result)}")
		print(f"{Fore.BLUE}{hangman[index]}{Fore.RESET}")

	if "_" not in result:
		end_of_game = True
		print(f"{Back.GREEN}\nYou won!{Back.RESET}\n")