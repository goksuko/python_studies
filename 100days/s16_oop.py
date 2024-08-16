## Procedural Programming
## what we do in procedural programming is to write a sequence of instructions to tell the computer what to do.
## The focus is on the procedures or steps that the program needs to perform.
## The main idea is to break down the program into a set of functions or procedures.

## Object-Oriented Programming
## Object-oriented programming (OOP) is a programming paradigm that is based on the concept of objects.
## Objects are instances of classes, which are user-defined data types that can contain data and code.

# objects have things
# variables are: attributes

# objects do things
# functions are: methods

# class: a blueprint for creating objects
# object: a particular instance of a class
# attribute: a variable that belongs to a class or object
# method: a function that belongs to a class or object

# car is a class
# car1 is an object

# car1 = CarBlueprint()	# create an object of the class CarBlueprint (PascalCase is used for class names)
# car1.speed = 30			# set the speed attribute of the car1 object
# car1.stop()				# call the stop method of the car1 object


# from turtle import Turtle, Screen

# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("red")
# timmy.forward(100)

# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable() # a new object of the PrettyTable class

table.field_names = ["Pokemon name", "Type"]
table.add_row(["Pikachu", "Electric"])
table.add_row(["Squirtle", "Water"])
table.add_row(["Charmander", "Fire"])

table2 = PrettyTable() # a new object of the PrettyTable class
table2.add_column("Pokemon name", ["Pikachu", "Squirtle", "Charmander"])
table2.add_column("Type", ["Electric", "Water", "Fire"])
table2.align = "l"

print(table)
print(table.align)

print(table2) 




