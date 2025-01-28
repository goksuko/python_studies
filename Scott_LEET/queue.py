# List is a Python’s built-in data structure that can be used as a queue. 
# Instead of enqueue() and dequeue(), 
# append() and pop() function is used.
# However, lists are quite slow for this purpose because inserting or deleting 
# an element at the beginning requires shifting all of the other elements by one, 
# requiring O(n) time.

l_list = []
l_list.append('a')
l_list.append('b')
l_list.append('c')
print("Initial l_list")
print(l_list)
print("\nElements del_listd from l_list")
print(l_list.pop(0))
print(l_list.pop(0))
print(l_list.pop(0))
print("\nQueue after removing elements")
print(l_list)
l_list.append('a')
l_list.append('b')
l_list.append('c')

# Queue in Python can be implemented using deque class from the collections module. 
# Deque is preferred over list in the cases where we need quicker append and pop 
# operations from both the ends of container, as deque provides 
# an O(1) time complexity # for append and pop operations as 
# compared to list which provides O(n) time complexity. 

from collections import deque
q = deque()
q.append('a')
q.append('b')
q.append('c')
print("Initial queue")
print(q)
print("\nElements dequeued from the queue")
print(q.popleft())
print(q.popleft())
print(q.popleft())
print("\nQueue after removing elements")
print(q)
# print(q.popleft()) # This will throw an error as queue is empty
if q:
   print(q.popleft())
else: 
	print("Queue is empty")
 
q.append('a')
q.append('b')
q.append('c')
p = deque()
p.append('d')
p.append('e')
p.append('f')

q.extend(p)
print(q)
q.extendleft(p)
print(q)
q.rotate(1)
print(q)
q.rotate(-1)
print(q)
print(q.count('f'))
q.remove('a')
print(q)
print(q.index('b'))
q.reverse()
print(q)
q.remove('f')
print(q)
print(q.maxlen)
q.insert(0, 'f')
print(q)

l_queue = deque(l_list)
print(l_queue)