# Creating a list
fruits = ['apple', 'banana', 'cherry']

# Add a new element at the end
fruits.append('date') # ['apple', 'banana', 'cherry', 'date']

# Inserting an element at a specific position
fruits.insert(1, 'bilberry') # ['apple', 'bilberry', 'banana', 'cherry', 'date']

# Removing a particular element
fruits.remove('banana') # ['apple', 'bilberry', 'cherry', 'date']

# Accessing elements using indexing
first_fruit = fruits[0] # apple
last_fruit = fruits[-1] # date

print(fruits.pop()) # date
print(fruits) # ['apple', 'bilberry', 'cherry']
