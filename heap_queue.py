import heapq

li = [5, 7, 9, 1, 3]
heapq.heapify(li)
heapq.heappush(li, 4)
heapq.heappop(li)
heapq.heappushpop(li, 2)
heapq.heapreplace(li, 2)
heapq.nlargest(3, li)
heapq.nsmallest(3, li)

# Heap data structure is mainly used to represent a priority queue. 
# In Python, it is available using the “heapq” module. 
# The property of this data structure in Python is that 
# each time the smallest heap element is popped(min-heap). 
# Whenever elements are pushed or popped, heap structure is maintained. 
# The heap[0] element also returns the smallest element each time.

# importing "heapq" to implement heap queue
import heapq

# initializing list
li = [5, 7, 9, 1, 3]
print ("The list before heapify : ", end="")
print(list(li))

# using heapify to convert list into heap
heapq.heapify(li)

# printing created heap
print("The created heap is : ", end="")
print(list(li))

# using heappush() to push elements into heap
# pushes 4
heapq.heappush(li, 4)

# printing modified heap
print("The modified heap after push is : ", end="")
print(list(li))

# using heappop() to pop smallest element
print("The popped and smallest element is : ", end="")
print(heapq.heappop(li))

# printing modified heap
print("The modified heap after pop is : ", end="")
print(list(li))

# heappushpop(heap, ele):- This function 
# combines the functioning of both push and pop operations 
# in one statement, increasing efficiency. 
# Heap order is maintained after this operation.

# heapreplace(heap, ele):- This function also 
# inserts and pops elements in one statement, but 
# it is different from the above function. 
# In this, the element is first popped, 
# then the element is pushed. i.e, 
# the value larger than the pushed value can be returned. 
# heapreplace() returns the smallest value originally in the heap 
# regardless of the pushed element as opposed to heappushpop().

# initializing list 1
li1 = [5, 7, 9, 4, 3]

# initializing list 2
li2 = [5, 7, 9, 4, 3]

# using heapify() to convert list into heap
heapq.heapify(li1)
heapq.heapify(li2)

# using heappushpop() to push and pop items simultaneously
# pops 2
print("The popped item using heappushpop() is : ", end="")
print(heapq.heappushpop(li1, 2))

# using heapreplace() to push and pop items simultaneously
# pops 3
print("The popped item using heapreplace() is : ", end="")
print(heapq.heapreplace(li2, 2))

# nlargest(k, iterable, key = fun): This function is used to 
# return the k largest elements from the iterable specified 
# and satisfy the key if mentioned.

# nsmallest(k, iterable, key = fun): This function is used to 
# return the k smallest elements from the iterable specified 
# and satisfy the key if mentioned.

# Python code to demonstrate working of
# nlargest() and nsmallest()

# initializing list
li1 = [6, 7, 9, 4, 3, 5, 8, 10, 1]

# using heapify() to convert list into heap
heapq.heapify(li1)

# using nlargest to print 3 largest numbers
# prints 10, 9 and 8
print("The 3 largest numbers in list are : ", end="")
print(heapq.nlargest(3, li1))

# using nsmallest to print 3 smallest numbers
# prints 1, 3 and 4
print("The 3 smallest numbers in list are : ", end="")
print(heapq.nsmallest(3, li1))

# Initialize a list with some values
values = [5, 1, 3, 7, 4, 2]

# Convert the list into a heap
heapq.heapify(values)

# Print the heap
print("Heap			:", values)

# Add a new value to the heap
heapq.heappush(values, 6)

# Print the updated heap
print("Heap after push		:", values)

# Remove and return the smallest element from the heap
smallest = heapq.heappop(values)

# Print the smallest element and the updated heap
print("Smallest element	:", smallest)
print("Heap after pop		:", values)

# Get the n smallest elements from the heap
n_smallest = heapq.nsmallest(3, values)

# Print the n smallest elements
print("Smallest 3 elements	:", n_smallest)

# Get the n largest elements from the heap
n_largest = heapq.nlargest(2, values)

# Print the n largest elements
print("Largest 2 elements	:", n_largest)
