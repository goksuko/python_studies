from p15_module import logo_art
from p15_module import data
from p15_module import coins

water_res = 300
milk_res = 200
coffee_res = 100
money = 0

def report():
	print("\nReport:")
	print(f"Water: {water_res}ml")
	print(f"Milk: {milk_res}ml")
	print(f"Coffee: {coffee_res}g")
	print(f"Money: ${money}\n")

def check_res(drink):
	global water_res
	global milk_res
	global coffee_res
	if water_res < drink['water']:
		print("Sorry there is not enough water. Money refunded.")
		return False
	if milk_res < drink['milk']:
		print("Sorry there is not enough milk. Money refunded.")
		return False
	if coffee_res < drink['coffee']:
		print("Sorry there is not enough coffee. Money refunded.")
		return False
	water_res -= drink['water']
	milk_res -= drink['milk']
	coffee_res -= drink['coffee']
	return True

def process_coins():
	total = 0
	print("Please insert coins.")
	for coin in coins:
		coin_count = int(input(f"How many {coin['name']}?: "))
		total += coin_count * coin['value']
	return total

def check_money(total, drink):
	if total < drink['price']:
		print("Sorry that's not enough money. Money refunded.")
		return False
	print(f"\nYou have inserted ${total}.")
	return True

def use_money(drink, total):
	change = round(total - drink['price'], 2)
	print(f"Here is ${change} in change.")
	global money
	money += drink['price']

def make_coffee(drink):
	total = process_coins()
	if check_money(total, drink):
		if check_res(drink):
			use_money(drink, total)
			print(f"\nHere is your {drink['name']} ☕ Enjoy!")

def coffee_machine():
	print(logo_art)
	while True:
		choice = input("\nWhat would you like? (espresso/latte/cappucino): ")
		if choice == 'off':
			break
		elif choice == 'report':
			report()
		else:
			for drink in data:
				if drink['name'] == choice:
					make_coffee(drink)
					break

coffee_machine()
