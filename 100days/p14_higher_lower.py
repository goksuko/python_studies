from p14_module import logo_art
from p14_module import vs_logo
from p14_module import data
from p14_module import clear_screen
from colorama import Fore 
import random

clear_screen()
print(f"{Fore.CYAN}{logo_art}{Fore.RESET}")
score = 0

length_data = len(data)
answer_index = length_data
right_index = length_data

first_index = random.randint(0, length_data - 1)

while answer_index == right_index:
	second_index = random.randint(0, length_data - 1)
	while second_index == first_index:
		second_index = random.randint(0, length_data + 1)	

	print(f"{Fore.CYAN}Compare A: {data[first_index]['name']}, {data[first_index]['description']}, {data[first_index]['country']}{Fore.RESET}")
	print(f"{Fore.CYAN}{vs_logo}{Fore.RESET}")
	print(f"{Fore.CYAN}Against B: {data[second_index]['name']}, {data[second_index]['description']}, {data[second_index]['country']}{Fore.RESET}")
	answer = input("Who has more followers? Type 'A' or 'B': ")

	if answer == 'A':
		answer_index = first_index
	else:
		answer_index = second_index

	if data[first_index]['follower_count'] > data[second_index]['follower_count']:
		right_index = first_index
	else:
		right_index = second_index

	if answer_index == right_index:
		score += 1
		print(f"\n{Fore.GREEN}You're right! Current score: {score}.{Fore.RESET}\n")
		first_index = right_index
	else:
		print(f"\n{Fore.RED}Sorry, that's wrong. Final score: {score}.{Fore.RESET}\n")
