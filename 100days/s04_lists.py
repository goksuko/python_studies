states_of_america = ["Deleware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

print(states_of_america)
print(states_of_america[0])
print(states_of_america[1])
print(states_of_america[-1])

states_of_america[1] = "Pencilvania"

print(states_of_america[1])

states_of_america.append("Angelaland")

print(states_of_america)

states_of_america.extend(["Goksu", "Goksu2"])

print(states_of_america)

print(len(states_of_america))
# print(states_of_america[53])

# You are working in a team of developers.
# Another developer has written the code to import the names in the inputs
# You can run the code to see what this names list looks like.
# Then change the names in the input to see how it imports the names.
names = ['Angela', 'Ben', 'Jenny', 'Michael', 'Chloe']
# print(names)
# 🚨 Remember to remove the print statement above when you submit.

import random

length_of_list = len(names)
index = random.randint(0, length_of_list - 1)
loser = names[index]

print(f"{loser} is going to buy the meal today!")

fruits = ["strawberries", "nectarines"]
vegetables = ["spinach", "carrots"]

greens = [fruits, vegetables]
print(greens)

line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇
letters = ["A", "B", "C"]
if position[0] == "A":
  second = 0
elif position[0] == "B":
  second = 1
else:
  second = 2
first = int(position[1]) - 1
map[first][second] = "X"

# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")