from p09_module import start_logo
from p09_module import clear
from colorama import Fore

print(f"{Fore.CYAN}{start_logo}")
print(f"Welcome to the secret auction program.{Fore.RESET}")
# bidders = []
# more_people = True
# while (more_people):
# 	name = input("What is your name?: ")
# 	bid  = int(input("What's your bid?: $"))
# 	answer = input("Are there any other bidders? Type 'yes' or 'no'.").lower()
# 	if answer == "no":
# 		more_people = False
# 	bidders.append({"N": name, "BD": bid})
# 	clear()

# max_value = 0
# for dictionary in bidders:
# 	winner = ""
# 	if dictionary["BD"] > max_value:
# 		max_value = dictionary["BD"]
# 		winner = dictionary["N"]

bidders = {}
more_people = True
while (more_people):
	name = input("What is your name?: ")
	bid  = int(input("What's your bid?: $"))
	answer = input("Are there any other bidders? Type 'yes' or 'no'.").lower()
	if answer == "no":
		more_people = False
	bidders[name] = bid
	clear()

max_value = 0
for person in bidders:
	value = bidders[person]
	if value > max_value:
		max_value = value
		winner = person

print(f"{Fore.MAGENTA}{start_logo}{Fore.RESET}")
print(f"The winner is {Fore.MAGENTA}{winner}{Fore.RESET} with a bid of {Fore.MAGENTA}${max_value}")
