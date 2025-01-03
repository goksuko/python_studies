from collections import defaultdict

# Defaultdict is a subclass of Python’s built-in dict class. 
# It overrides the __missing__ method to provide a default value 
# for missing keys, preventing KeyError. 
# If a key is not found in the dictionary, defaultdict automatically 
# inserts it with a default value.


# Create a defaultdict with a default
# value of an empty list
d = defaultdict(list)

# Add elements to the defaultdict and print it
d['fruits'].append('apple')
d['vegetables'].append('carrot')
print(d) # defaultdict(<class 'list'>, {'fruits': ['apple'], 'vegetables': ['carrot']})

# No key error raised here and an empty list
# is printed
print(d['juices']) # []

   
# Defining the dict and passing 
# lambda as default_factory argument
d = defaultdict(lambda: "Not Present")
d["a"] = 1
d["b"] = 2

print(d["a"]) # 1
print(d["b"]) # 2
print(d["c"]) # Not Present


# Provides the default value 
# for the key
print(d.__missing__('a')) # Not Present
print(d.__missing__('d')) # Not Present

# Defining the dict
d = defaultdict(int)
 
L = [1, 2, 3, 4, 2, 4, 1, 2]
 
# Iterate through the list
# for keeping the count
for i in L:
     
    # The default value is 0
    # so there is no need to 
    # enter the key first
    d[i] += 1
     
print(d) # defaultdict(<class 'int'>, {1: 2, 2: 3, 3: 1, 4: 2})

from collections import defaultdict

# Using str as the factory function
str_defaultdict = defaultdict(str)
str_defaultdict['greeting'] = 'Hello'
print(str_defaultdict) # defaultdict(<class 'str'>, {'greeting': 'Hello'})

# setdefault is a method of the dict class. It inserts a key with a specified default value if the key is not already present.

d = {}
d.setdefault('key', []).append(1)
print(d)  # {‘key’: [1]}

# setdefault is used to insert a key with a default value if the key is not already in the dictionary. 
# This is useful for avoiding repeated key existence checks and manual insertion.

d = {}
d.setdefault('key', []).append(1)
d.setdefault('key', []).append(2)
print(d)  #  {‘key’: [1, 2]}

# defaultdict is a subclass of dict that provides a default value for a missing key without explicitly checking for its presence.
dd = defaultdict(list)
dd['key'].append(1)
print(dd)  # defaultdict(<class ‘list’>, {‘key’: [1]})