def greet():
	print("Hello")
	print("line2")
	print("line3")

greet()

def greet_with_name(name): #functions that allows for input
	print(f"Hello {name}")
	print("line2")
	print("line3")

# name is PARAMETER = the name of the data being passed in
# Goksu is ARGUMENT = the actual value of the data
greet_with_name("Goksu")

def greet_with(name, location):
	print(f"Hello {name}!")
	print(f"How is the weather in {location}?")

greet_with("Goksu", "Ankara") # POSITIONAL ARGUMENTS
greet_with(location = "Ankara", name = "Goksu") # KEYWORD ARGUMENTS

# Write your code below this line 👇
import math

def paint_calc(height, width, cover):
  result = math.ceil(height * width / cover)
  print(f"You'll need {result} cans of paint.")

# Write your code above this line 👆
# Define a function called paint_calc() so the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input()) # Height of wall (m)
test_w = int(input()) # Width of wall (m)
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)



# Write your code below this line 👇

def prime_checker(number):
  is_prime = True
  for i in range(2, number):
    if number % i == 0:
      is_prime = False
  if is_prime:
    print("It's a prime number.")
  else:
    print("It's not a prime number.")
# Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input()) # Check this number
prime_checker(number=n)
