fruits = ["apple", "banana", "cherry"]

for x in fruits:
	print(x)
	print(x + " is a fruit")
print(fruits)

# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  
# Write your code below this row 👇
total = 0
population = len(student_heights)
for x in range(0, population):
  total += student_heights[x]
average = total / population
print(f"total height = {total}")
print(f"number of students = {population}")
print(f"average height = {round(average)}")

# Input a list of student scores
student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

# Write your code below this row 👇
high = student_scores[0]
for score in student_scores:
  if score > high:
    high = score
print(f"The highest score in the class is: {high}")

for number in range(1, 10): # not 10 is written!
	print(number)

for number in range(1, 10, 2):
	print(number)

total = 0
for number in range(1, 101):
	total += number
print(total)

target = int(input()) # Enter a number between 0 and 1000
# 🚨 Do not change the code above ☝️

# Write your code here 👇
total = 0
for num in range(0, target + 1, 2):
  if num % 2 == 0:
    total += num

print(total)

# Write your code here 👇
for num in range (1, 101):
  if num % 15 == 0:
    print("FizzBuzz")
  else:
    if num % 3 == 0:
      print("Fizz")
    if num % 5 == 0:
      print("Buzz")
    if num % 3 != 0 and num % 5 != 0:
      print(num)

target = 100
for number in range(1, target + 1):
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print(number)