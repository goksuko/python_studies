# Integers are immutable objects in Python
# They cannot be changed in place, but can be reassigned

num1 = 11
num2 = num1

print("Before")
print("num1:", num1)
print("num2:", num2)	

print("num1 points to", id(num1))
print("num2 points to", id(num2))

num1 = 22

print("\nAfter")
print("num1:", num1)
print("num2:", num2)

print("num1 points to", id(num1))
print("num2 points to", id(num2))

# Dictionaries are mutable objects in Python
# They can be changed in place

dict1 = {
	"value": 11
}
dict2 = dict1

print("\nBefore")
print("dict1:", dict1)
print("dict2:", dict2)

print("dict1 points to", id(dict1))
print("dict2 points to", id(dict2))

dict1["value"] = 22

print("\nAfter")
print("dict1:", dict1)
print("dict2:", dict2)

print("dict1 points to", id(dict1))
print("dict2 points to", id(dict2))

dict3 = {
	"value": 33
}

print("\nBefore")
print("dict1:", dict1)
print("dict2:", dict2)
print("dict3:", dict3)

print("dict1 points to", id(dict1))
print("dict2 points to", id(dict2))
print("dict3 points to", id(dict3))

dict1 = dict3

print("\nAfter")
print("dict1:", dict1)
print("dict2:", dict2)
print("dict3:", dict3)

print("dict1 points to", id(dict1))
print("dict2 points to", id(dict2))
print("dict3 points to", id(dict3))

print("\nif everything points to another, that the data will not be accessible anymore: \nso GARBAGE COLLECTOR will remove it")

dict2 = dict3

print("dict1:", dict1)
print("dict2:", dict2)
print("dict3:", dict3)

print("dict1 points to", id(dict1))
print("dict2 points to", id(dict2))
print("dict3 points to", id(dict3))

# Lists are mutable objects in Python
# Nodes can be changed in place