# Deque (Doubly Ended Queue) in Python is implemented using the module “collections“. Deque is preferred over a list in the cases where we need quicker append and pop operations from both the ends of the container, as deque provides an O(1) time complexity for append and pop operations as compared to a list that provides O(n) time complexity.

# Types of Restricted Deque Input
### Input Restricted Deque:  Input is limited at one end while deletion is permitted at both ends.
### Output Restricted Deque: output is limited at one end but insertion is permitted at both ends.

from collections import deque 
    
# Declaring deque 
queue = deque(['name','age','DOB'])  
    
print(queue) #deque(['name', 'age', 'DOB'])

# importing "collections" for deque operations
import collections

# initializing deque
de = collections.deque([1, 2, 3])
print(de) # deque([1, 2, 3])

# using append() to insert element at right end
# inserts 4 at the end of deque
de.append(4) 

# printing modified deque
print("\nThe deque after appending at right is : ")
print(de) # deque([1, 2, 3, 4])

# using appendleft() to insert element at left end
# inserts 6 at the beginning of deque
de.appendleft(6)

# printing modified deque
print("\nThe deque after appending at left is : ")
print(de) # deque([6, 1, 2, 3, 4])

# using pop() to delete element from right end
# deletes 4 from the right end of deque
de.pop()

# printing modified deque
print("\nThe deque after deleting from right is : ")
print(de) # deque([6, 1, 2, 3])

# using popleft() to delete element from left end
# deletes 6 from the left end of deque
de.popleft()

# printing modified deque
print("\nThe deque after deleting from left is : ")
print(de) # deque([1, 2, 3])

# Python code to demonstrate working of 
# insert(), index(), remove(), count()

# initializing deque
de = collections.deque([1, 2, 3, 3, 4, 2, 4])

# using index() to print the first occurrence of 4
print ("The number 4 first occurs at a position : ")
print (de.index(4,2,5)) # 4
print (de.index(2, 0, 5)) # 1 ## index(value, start, end)
print (de.index(2, 2, 6)) # 5

# using insert() to insert the value 3 at 5th position
de.insert(4,3) ### insert(index, value)

# printing modified deque
print ("The deque after inserting 3 at 5th position is : ")
print (de) # deque([1, 2, 3, 3, 3, 4, 2, 4])

# using count() to count the occurrences of 3
print ("The count of 3 in deque is : ")
print (de.count(3)) # 3

# using remove() to remove the first occurrence of 3
de.remove(2) # remove(value)

# printing modified deque
print ("The deque after deleting first occurrence of 3 is : ")
print (de) # deque([1, 3, 3, 3, 4, 2, 4])

# Python code to demonstrate working of 
# extend(), extendleft(), rotate(), reverse()

# initializing deque
de = collections.deque([1, 2, 3,])

# using extend() to add numbers to right end 
# adds 4,5,6 to right end
de.extend([4,5,6])

# printing modified deque
print ("The deque after extending deque at end is : ")
print (de) # deque([1, 2, 3, 4, 5, 6])

# using extendleft() to add numbers to left end 
# adds 7,8,9 to left end
de.extendleft([7,8,9]) ## extendleft(iterable) so reverse order

# printing modified deque
print ("The deque after extending deque at beginning is : ")
print (de) # deque([9, 8, 7, 1, 2, 3, 4, 5, 6])

# using rotate() to rotate the deque
# rotates by 3 to left
de.rotate(-3)

# printing modified deque
print ("The deque after rotating deque is : ")
print (de) # deque([1, 2, 3, 4, 5, 6, 9, 8, 7])

# using reverse() to reverse the deque
de.reverse()

# printing modified deque
print ("The deque after reversing deque is : ")
print (de) # deque([7, 8, 9, 6, 5, 4, 3, 2, 1])