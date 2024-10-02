from p10_module import art_logo 
from p10_module import clear_screen

def add(n1, n2):
	return n1 + n2

def substract(n1, n2):
	return n1 - n2

def multiply(n1, n2):
	return n1 * n2

def divide(n1, n2):
	return n1 / n2

math_dict = {
	"+": add,
	"-": substract,
	"*": multiply,
	"/": divide
}

### first calculator

# num1 = int(input("What's the first number?: "))
# num2 = int(input("What's the second number?: "))
# for key in math_dict:
# 	print(key)
# operation_symbol = input("Pick an operation from the line above: ")
# function_name = math_dict[operation_symbol]
# first_answer = function_name(num1, num2)

# print(f"{num1} {operation_symbol} {num2} = {first_answer}")

# for key in math_dict:
# 	print(key)
# operation_symbol = input("Pick an operation from the line above: ")
# function_name = math_dict[operation_symbol]
# num3 = int(input("What's the third number?: "))
# second_answer = function_name(first_answer, num3)

# print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")

### second_calculator

# num1 = int(input("What's the first number?: "))
# for key in math_dict:
# 	print(key)
# to_continue = True
# while to_continue:
# 	operation_symbol = input("Pick an operation: ")
# 	num2 = int(input("What's the next number?: "))
# 	function_name = math_dict[operation_symbol]
# 	answer = function_name(num1, num2)
# 	print(f"{num1} {operation_symbol} {num2} = {answer}")
# 	letter = input(f"Type 'y' to continue with {answer}, type 'n' to start a new calculation, or type 'e' to exit: ")
# 	if letter == 'e':
# 		to_continue = False
# 	elif letter == 'n':
# 		num1 = int(input("What's the first number?: "))
# 	else:
# 		num1 = answer

### third_calculator

def calculator():
	clear_screen()
	print(art_logo)
	num1 = float(input("What's the first number?: "))
	for key in math_dict:
		print(key)
	to_continue = True
	while to_continue:
		operation_symbol = input("Pick an operation: ")
		num2 = float(input("What's the next number?: "))
		function_name = math_dict[operation_symbol]
		answer = function_name(num1, num2)
		print(f"{num1} {operation_symbol} {num2} = {answer}")
		letter = input(f"Type 'y' to continue with {answer}, or type 'n' to start a new calculation: ")
		if letter == 'n':
			to_continue = False
			calculator()
		else:
			num1 = answer

calculator()