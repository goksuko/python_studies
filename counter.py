from collections import Counter

x = Counter("geeksforgeeks")
x.elements()
x.keys()
x.values()


# Counter is a sub-class that is used to count hashable objects. 
# It implicitly creates a hash table of an iterable when invoked.

# Parameters : Doesn’t take any parameters
# Return type : Returns an itertool for all the elements with positive count in the Counter object
# Errors and Exceptions : 
# -> It will print garbage value when directly printed because it returns an itertool, not a specific data-container. 
# -> If the count of an item is already initialized in Counter object, then it will ignore the ones with zero and negative values. 

# import counter class from collections module
from collections import Counter

# Creation of a Counter Class object using 
# string as an iterable data container
x = Counter("geeksforgeeks")
print(x) # Counter({'e': 4, 'g': 2, 'k': 2, 's': 2, 'f': 1, 'o': 1, 'r': 1})
y = Counter(['a', 'b', 'c', 'a', 'b', 'b'])
print(y) # Counter({'b': 3, 'a': 2, 'c': 1})
z = {1: [1], 2: [2,3], 3: [4,5,6], 4: [7,8,9,10]}
t = Counter(z)
print(t) # Counter({4: [7, 8, 9, 10], 3: [4, 5, 6], 2: [2, 3], 1: [1]})
print(t[4]) # [7, 8, 9, 10]

# printing the elements of counter object
for i in x.elements():
    print (i, end = " ") # g g e e e e k k s s f o r

# elements() method of Counter class

    
# will return a itertools chain object
# which is basically a pseudo iterable container whose
# elements can be used when called with a iterable tool
print(x.elements()) # <itertools.chain object at 0x7f8b1c1b3f40>
    
#Creating a Counter class object using list as an iterable data container
a = [12, 3, 4, 3, 5, 11, 12, 6, 7]

x = Counter(a)

#directly printing whole x
print(x) # Counter({12: 2, 3: 2, 4: 1, 5: 1, 11: 1, 6: 1, 7: 1})

#We can also use .keys() and .values() methods to access Counter class object
for i in x.keys():
      print(i, ":", x[i]) # 12 : 2 3 : 2 4 : 1 5 : 1 11 : 1 6 : 1 7 : 1
    
#We can also make a list of keys and values of x
x_keys = list(x.keys()) # [12, 3, 4, 5, 11, 6, 7]
x_values = list(x.values()) # [2, 2, 1, 1, 1, 1, 1]

print(x_keys)
print(x_values)

# Creation of a Counter Class object using 
# a string as an iterable data container
# Example - 1
a = Counter("geeksforgeeks")

# Elements of counter object
for i in a.elements():
    print ( i, end = " ") # g g e e e e k k s s f o r g e e k s
print()
    
# Example - 2
b = Counter({'geeks' : 4, 'for' : 1, 
            'gfg' : 2, 'python' : 3})

for i in b.elements():
    print ( i, end = " ") # geeks geeks geeks geeks for gfg gfg python python python
print()

# Example - 3
c = Counter([1, 2, 21, 12, 2, 44, 5,
              13, 15, 5, 19, 21, 5])

for i in c.elements():
    print ( i, end = " ") # 1 2 2 21 21 12 44 5 5 5 13 15 19
print()              
              
# Example - 4
d = Counter( a = 2, b = 3, c = 6, d = 1, e = 5)

for i in d.elements():
    print ( i, end = " ") # a a b b b c c c c c c d e e e e e
    

# creating a raw data-set using keyword arguments
x = Counter (a = 2, x = 3, b = 3, z = 1, y = 5, c = 0, d = -3)

# printing out the elements
for i in x.elements():
    print( "% s : % s" % (i, x[i]), end ="\n") # a : 2 x : 3 x : 3 x : 3 z : 1 y : 5 y : 5 y : 5 y : 5 y : 5
    
# Note: We can infer from the output that items with values less than 1 are omitted by elements(). !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# Counter object along with its functions are used collectively for processing huge amounts of data. 
# We can see that Counter() creates a hash-map for the data container invoked with it which is very useful 
# than by manual processing of elements. It is one of a very high processing and functioning tools 
# and can even function with a wide range of data too.