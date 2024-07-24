import random
import s04_my_module

# 1 - 10
random_int = random.randint(1, 10)
print(random_int)

print(s04_my_module.goksu)

# 0.0000000000000000 - 0.9999999999999999
random_float = random.random()
print(random_float)

random_zero_five = random_float * random_int / 2
random_zero_five = random_float * 5
print(random_zero_five)

love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")

# Write your code below this line 👇
# Hint: Remember to import the random module first. 🎲
import random

number = random.randint(0, 1)
if number == 1:
  print("Heads")
else:
  print("Tails")

