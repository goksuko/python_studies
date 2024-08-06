from p16_menu import Menu, MenuItem
from p16_coffee_maker import CoffeeMaker
from p16_money_machine import MoneyMachine

latte = MenuItem("latte", 200, 150, 24, 2.5)
cappucino = MenuItem("capuccino", 250, 100, 24, 3.00)
espresso = MenuItem("espresso", 50, 0, 18, 1.50)

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True

while is_on:
	options = menu.get_items()
	choice = input(f"What would you like? ({options}): ")
	if choice == "off":
		is_on = False
	elif choice == "report":
		coffee_maker.report()
		money_machine.report()
	else:
		drink = menu.find_drink(choice)
		if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
			coffee_maker.make_coffee(drink)