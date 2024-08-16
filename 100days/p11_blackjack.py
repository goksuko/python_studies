############### Blackjack Project #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

from p11_module import logo_art
import random
from p11_module import clear_screen

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def give_a_card():
	# card = cards[random.randint(0, 12)]
	card = random.choice(cards)
	return card

dealer = []
player = []

def deal_cards():
	dealer.clear()
	player.clear()
	dealer.append(give_a_card())
	player.append(give_a_card())
	dealer.append(give_a_card())
	player.append(give_a_card())

total = 0

def sum_hand(hand_list):
	# total = 0
	# for card in hand_list:
	# 	total += card
	total = sum(hand_list)
	return total	

def print_hands():
	print(f"Your cards: {player}, current score: {sum_hand(player)}")
	print(f"Computer's first card: {dealer[0]}")

def print_finals():
	print(f"Your final hand: {player}, final score: {sum_hand(player)}")
	print(f"Computer's final hand: {dealer}, final score: {sum_hand(dealer)}")
	print("\n********************")

def print_result():
	sum_p = sum_hand(player)
	sum_d = sum_hand(dealer)
	if sum_d == sum_p or (sum_d > 21 and sum_p > 21):
		print("EQUAL GAME")
	elif sum_d == 21:
		print("BLACKJACK - You lose!")
	elif sum_p == 21:
		print("BLACKJACK - You win!")
	elif sum_d > 21:
		print("BUST - Dealer went over. You win!")
	elif sum_p > 21:
		print("BUST - You went over. You lose!")
	elif sum_d > sum_p:
		print("You lose! 😤")
	elif sum_p > sum_d:
		print("You win! 😃")
	else:
		print("WTF?!")

hand_sum = 0

def make_dealer_hand():
	hand_sum = sum_hand(dealer)
	while hand_sum < 17:
		dealer.append(give_a_card())
		hand_sum = sum_hand(dealer)

def check_if_ace(my_list):
	hand_sum = sum_hand(my_list)
	for card in my_list:
		if card == 11:
			my_list.remove(11)
			my_list.append(1)
	hand_sum = sum_hand(my_list)		
	return hand_sum

def blackjack():
	deal_cards()
	make_dealer_hand()
	print_hands()
	answer = 'n'
	hand_sum = sum_hand(player)
	if hand_sum > 21:
		hand_sum = check_if_ace(player)
	if hand_sum < 21:
		answer = input("Type 'y' to get another card, type 'n' to pass: ")

	while answer == 'y' and hand_sum < 21:
		player.append(give_a_card())
		print_hands()
		hand_sum = sum_hand(player)
		if hand_sum > 21:
			hand_sum = check_if_ace(player)
		if hand_sum < 21:
			answer = input("Type 'y' to get another card, type 'n' to pass: ")

	print("\n********************")
	print_finals()
	print_result()

to_continue = True

clear_screen()
print(logo_art)

while to_continue:
	blackjack()
	cont = input("Do you want to play a game of Blackjack again? Type 'y' or 'n': ")
	if cont == 'n':
		to_continue = False
	else:
		clear_screen()
		print(logo_art)

