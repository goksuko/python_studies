water_level = 50
if (water_level > 80):
	print("Drain water")
else:
	print("Continue")

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
	print("You can ride the rollercoaster!")
	age = int(input("What is your age? "))
	if age < 12:
		bill = 5
		print("Child tickets are $5.")
	elif age <= 18:
		bill = 7
		print("Youth tickets are $7.")
	elif age >= 45 and age <= 55:
		print("Everything is going to be ok. Have a free ride on us!")
	else:
		bill = 12
		print("Adult tickets are $12.")

	wants_photo = input("Do you want a photo taken? Y or N. ")
	if wants_photo == "Y":
		bill += 3
		print("Photo costs $3.")
	else:
		print("No photo.")	
	# print("This is intended to be executed if the condition is met")
	print(f"Your final bill is ${bill}")

# print("This is outside of the if block")
else:
	print("Sorry, you have to grow taller before you can ride.")

# Enter your height in meters e.g., 1.55
height = float(input("Enter your height in meters e.g., 1.55: "))
# Enter your weight in kilograms e.g., 72
weight = int(input("Enter your weight in kilograms e.g., 72: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = weight / height ** 2
if bmi < 18.5:
  print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
  print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
  print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
  print(f"Your BMI is {bmi}, you are obese.")
else:
  print(f"Your BMI is {bmi}, you are clinically obese.")


# Which year do you want to check?
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
if year % 4 != 0:
  print("Not leap year")
elif year % 100 == 0:
  if year % 400 == 0:
    print("Leap year")
  else:
    print("Not leap year")
else:
  print("Leap year")

# beter
if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year")
    else:
      print("Not leap year")
  else:
    print("Leap year")
else:
  print("Not leap year")

print("Thank you for choosing Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L: ") # What size pizza do you want? S, M, or L
add_pepperoni = input("Do you want pepperoni? Y or N" ) # Do you want pepperoni? Y or N
extra_cheese = input("Do you want extra cheese? Y or N ") # Do you want extra cheese? Y or N
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
bill = 0
if size == "S":
  bill += 15
elif size == "M":
  bill += 20
else:
  bill += 25
if add_pepperoni == "Y":
  bill += 3
if extra_cheese == "Y":
  bill += 1
print(f"Your final bill is: ${bill}.")

print("The Love Calculator is calculating your score...")
name1 = input("What is your name? ") # What is your name?
name2 = input("What is their name? ") # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
combined_names = name1 + name2
lower_case = combined_names.lower()
first_digit = lower_case.count("t") + lower_case.count("r") + lower_case.count("u") + lower_case.count("e")
second_digit = lower_case.count("l") + lower_case.count("o") + lower_case.count("v") + lower_case.count("e")
score = 10 * first_digit + second_digit

if score < 10 or score > 90:
  print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")