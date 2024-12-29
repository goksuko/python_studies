from collections import OrderedDict

#2. Doubly Linked List
class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}  # map key to node

        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

# 1. Brute Force
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = []
        self.capacity = capacity

    def get(self, key: int) -> int:
        for i in range(len(self.cache)):
            if self.cache[i][0] == key:
                tmp = self.cache.pop(i)
                self.cache.append(tmp)
                return tmp[1]
        return -1

    def put(self, key: int, value: int) -> None:
        for i in range(len(self.cache)):
            if self.cache[i][0] == key:
                tmp = self.cache.pop(i)
                tmp[1] = value
                self.cache.append(tmp)
                return

        if self.capacity == len(self.cache):
            self.cache.pop(0)
            
        self.cache.append([key, value])

# 3. Built-In Data Structure
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        else:
            self.dic.move_to_end(key)
            return self.dic[key]
        
    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self.dic.move_to_end(key)
        self.dic[key] = value
        if len(self.dic) > self.capacity:
            self.dic.popitem(last=False)

lr = LRUCache(2)
print(lr.put(1, 10))  # cache: {1=10}
print(lr.get(1))      # return 10
print(lr.put(2, 20))  # cache: {1=10, 2=20}
print(lr.put(3, 30))  # cache: {2=20, 3=30}, key=1 was evicted
print(lr.get(2))      # returns 20 
print(lr.get(1))      # return -1 (not found)


# LRU Cache
# Implement the Least Recently Used (LRU) cache class LRUCache. The class should support the following operations

# LRUCache(int capacity) Initialize the LRU cache of size capacity.
# int get(int key) Return the value corresponding to the key if the key exists, otherwise return -1.
# void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the introduction of the new pair causes the cache to exceed its capacity, remove the least recently used key.
# A key is considered used if a get or a put operation is called on it.

# Ensure that get and put each run in 
# O
# (
# 1
# )
# O(1) average time complexity.

# Example 1:

# Input:
# ["LRUCache", [2], "put", [1, 10],  "get", [1], "put", [2, 20], "put", [3, 30], "get", [2], "get", [1]]

# Output:
# [null, null, 10, null, null, 20, -1]

# Explanation:
# LRUCache print(LRUCache = new LRUCache(2);
# print(LRUCache.put(1, 10);  # cache: {1=10}
# print(LRUCache.get(1);      # return 10
# print(LRUCache.put(2, 20);  # cache: {1=10, 2=20}
# print(LRUCache.put(3, 30);  # cache: {2=20, 3=30}, key=1 was evicted
# print(LRUCache.get(2);      # returns 20 
# print(LRUCache.get(1);      # return -1 (not found)
# Constraints:

# 1 <= capacity <= 100
# 0 <= key <= 1000
# 0 <= value <= 1000


# Recommended Time & Space Complexity
# You should aim for a solution with O(1) time for each put() and get() function call and an overall space of O(n), where n is the capacity of the LRU cache.


# Hint 1
# Can you think of a data structure for storing data in key-value pairs? Maybe a hash-based data structure with unique keys.


# Hint 2
# We can use a hash map which takes O(1) time to get and put the values. But, how can you deal with the least recently used to be removed criteria as a key is updated by the put() or recently used by the get() functions? Can you think of a data structure to store the order of values?


# Hint 3
# A brute-force solution would involve maintaining the order of key-value pairs in an array list, performing operations by iterating through the list to erase and insert these key-value pairs. However, this would result in an O(n) time complexity. Can you think of a data structure that allows removing and reinserting elements in O(1) time?


# Hint 4
# We can use a doubly-linked list, which allows us to remove a node from the list when we have the address of that node. Can you think of a way to store these addresses so that we can efficiently remove or update a key when needed?


# Hint 5
# We can use a doubly linked list where key-value pairs are stored as nodes, with the least recently used (LRU) node at the head and the most recently used (MRU) node at the tail. Whenever a key is accessed using get() or put(), we remove the corresponding node and reinsert it at the tail. When the cache reaches its capacity, we remove the LRU node from the head of the list. Additionally, we use a hash map to store each key and the corresponding address of its node, enabling efficient operations in O(1) time