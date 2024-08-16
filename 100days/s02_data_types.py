#string

print(len("Hello World!")) # 12
print("Hello[0]")
print("Hello"[0])
print("123" + "456") # 123456

#integer

print(123 + 456) # 579
print(123_456_789) # 123456789

#float

3.14159

#boolean

True
False

# len(123) # TypeError: object of type 'int' has no len()

num_char = len(input("What is your name? "))

print(type(num_char)) # <class 'int'> type checking
print("Your name has " + str(num_char) + " characters.") # Your name has 5 characters.

new_num_char = str(num_char) # '5' type conversion
print(type(new_num_char)) # <class 'str'> type checking
print("Your name has " + new_num_char + " characters.") # Your name has 5 characters.

a = 123
print(type(a)) # <class 'int'> type
b = str(a)
print(type(b)) # <class 'str'> type
c = float(a)
print(type(c)) # <class 'float'> type

print(70 + float("100.5")) # 170.5
print(str(70) + str(100)) # 70100

#mathematical operations
print(3 + 5) # 8
print(7 - 4) # 3
print(3 * 2) # 6
print(6 / 3) # 2.0 float division results in float
print(2 ** 3) # 8 2^3
print(3 // 2) # 1 integer division results in integer

#PEMDASLR
#parentheses
#exponents
#multiplication
#division
#addition
#subtraction
#left to right

# ()
# **
# * / 
#  + -

print(3 * 3 + 3 / 3 - 3) # 7.0
print(3 * (3 + 3) / 3 - 3) # 3.0

print(8/3) # 2.6666666666666665
print(int(8/3)) # 2
print(round(8/3)) # 3
print(round(8/3, 2)) # 2.67
print(round(2.6666666666666665, 2)) # 2.67
print(8 // 3) # 2
print(type(4 / 2)) # <class 'float'>
print(type(4 // 2)) # <class 'int'>

result = 4 / 2
result /= 2
print(result) # 1.0

score = 0
# User scores a point
score += 1
print(score) # 1

score -= 1
print(score) # 0

#f-string
score = 0
height = 1.8
isWinning = True
print(str(isWinning)) # True
print("your score is " + str(score) + ", your height is " + str(height) + ", you are winning is " + str(isWinning)) # your score is 0, your height is 1.8, you are winning is True
print(f"your score is {score}, your height is {height}, you are winning is {isWinning}") # your score is 0, your height is 1.8, you are winning

# 1st input: enter height in meters e.g: 1.65
height = input()
# 2nd input: enter weight in kilograms e.g: 72
weight = input()
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
BMI = int(weight)/float(height)**2
print(int(BMI))

age = input()
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
number = (90 - int(age)) * 52
print(f"You have {number} weeks left.")
