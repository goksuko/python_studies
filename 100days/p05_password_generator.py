import random

letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
symbols = '!@#$%&*()_+'

len_letters = len(letters)
len_numbers = len(numbers)
len_symbols = len(symbols)

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))

backet = ""
for x in range(0, nr_letters):
	backet += letters[random.randint(0, len_letters - 1)]
	# random_char = random.choice(letters)
	# backet += random_char
for x in range(0, nr_numbers):
	backet += numbers[random.randint(0, len_numbers - 1)]
for x in range(0, nr_symbols):
	backet += symbols[random.randint(0, len_symbols - 1)]
print(backet)

backet_list = []
for x in range(0, nr_letters):
	backet_list += random.choice(letters)
	# backet_list.append(random.choice(letters))
for x in range(0, nr_numbers):
	backet_list += random.choice(numbers)
for x in range(0, nr_symbols):
	backet_list += random.choice(symbols)
print(backet_list)
random.shuffle(backet_list)
print(backet_list)

password = ""
for char in backet_list:
	password += char
print(f"Your password is: {password}")


