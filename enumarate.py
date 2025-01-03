# Often, when dealing with iterators, we also need to keep a count of iterations. Python eases the programmers’ task by providing a built-in function enumerate() for this task. The enumerate () function adds a counter to an iterable and returns it in the form of an enumerating object. This enumerated object can then be used directly for loops or converted into a list of tuples using the list() function.

#  Syntax:  enumerate(iterable, start=0) 

#  Parameters: 

#  Iterable:  any object that supports iteration 
#  Start:  the index value from which the counter is to be started, by default it is 0 
#  Return:  Returns an iterator with index and element pairs from the original iterable 

l1 = ["eat", "sleep", "repeat"]
s1 = "geek"

# creating enumerate objects
obj1 = enumerate(l1)
obj2 = enumerate(s1)

print ("Return type:", type(obj1))
print(obj1)
print(list(obj1))
print (list(enumerate(l1)))

# changing start index to 2 from 0
print (list(enumerate(s1, 2)))