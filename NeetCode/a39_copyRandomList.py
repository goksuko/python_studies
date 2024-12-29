from typing import List
from typing import Optional
import collections


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    
    #my trial but did not work
    
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        
        curr = head
        while curr is not None: #head: 1 -> 2-> 3  # 1 -> n1 -> 2 ->3      # 1 -> n1 -> 2 -> n2 -> 3 
            new = Node(curr.val) #new: n1          # n2
            new.next = curr.next # n1 -> 2         # n2 -> 3
            curr.next = new # 1 -> n1              # 2 -> n2
            curr = new.next # 2                    # 3 
            
        newHead = head.next
        
        curr = head
        while curr:
            curr.next.random = curr.random.next
            curr = curr.next.next
        
        # newbie = head.next
        # while newbie.next and newbie.next.next:
        #     newbie.next = newbie.next.next
        #     newbie = newbie.next.next
            
            
        curr = head
        while curr is not None:
            new = curr.next 
            curr.next = new.next
            if new.next is not None:
                new.next = new.next.next
            curr = curr.next
            
        return newHead
        
            
    # 2. Hash Map (Two Pass)
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCopy = {None: None}
        curr = head
        while curr:
            temp = Node(curr.val)
            oldToCopy[curr] = temp
            curr = curr.next
        curr = head
        while curr:
            temp = oldToCopy[curr] # it was a node with the curr.val, None, None
            temp.next = oldToCopy[curr.next] # another node with the next"s value, None, None
            temp.random = oldToCopy[curr.random]
            curr = curr.next
        return oldToCopy[head]
    
    # 1. Hash Map (Recursion)
    def __init__(self):
        self.map = {}

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        if head in self.map:
            return self.map[head]
        
        copy = Node(head.val)
        self.map[head] = copy
        copy.next = self.copyRandomList(head.next)
        copy.random = self.map.get(head.random)
        return copy
    
    # 3. Hash Map (One Pass)
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCopy = collections.defaultdict(lambda: Node(0)) 
        #when I call x[k] for a nonexistent key k (such as a statement like v=x[k]), 
        #the key-value pair (k,0) will be automatically added to the dictionary, 
        # as if the statement x[k]=0 is first executed. 
        oldToCopy[None] = None
        
        cur = head
        while cur:
            oldToCopy[cur].val = cur.val
            oldToCopy[cur].next = oldToCopy[cur.next]
            oldToCopy[cur].random = oldToCopy[cur.random]
            cur = cur.next
        return oldToCopy[head]
    
    # 4. Space Optimized - I

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        
        curr = head
        while curr is not None: #head: 1 -> 2-> 3  # 1 -> n1 -> 2 ->3      # 1 -> n1 -> 2 -> n2 -> 3 
            new = Node(curr.val) #new: n1          # n2
            new.next = curr.next # n1 -> 2         # n2 -> 3
            curr.next = new # 1 -> n1              # 2 -> n2
            curr = new.next # 2                    # 3 
            
        newHead = head.next
        
        curr = head
        while curr is not None: 
            if curr.random is not None:  
                curr.next.random = curr.random.next  #n1.r = 1r->next
            curr = curr.next.next
            
        curr = head
        while curr is not None:
            new = curr.next 
            curr.next = new.next
            if new.next is not None:
                new.next = new.next.next
            curr = curr.next
            
        return newHead
    
    
    # 5. Space Optimized - II

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None

        curr = head
        while curr:
            new = Node(curr.val)
            new.next = curr.random
            curr.random = new
            curr = curr.next
        
        newHead = head.random
        
        curr = head
        while curr:
            new = curr.random
            new.random = new.next.random if new.next else None
            curr = curr.next
            
        curr = head
        while curr is not None:
            new = curr.random
            curr.random = new.next
            new.next = curr.next.random if curr.next else None
            curr = curr.next

        return newHead
            
    def printList(self, head: Optional[Node]) -> None:
        curr = head
        while curr:
            print(curr.val)
            curr = curr.next
        print("----")
            
sol = Solution()
sec = Node(7, None, None) 
fourth = Node(5, None, sec )
third = Node(4, fourth, sec)
head = Node(3, sec, None)
sec = Node(7, third, fourth) 
sol.printList(head)
sol.copyRandomList(head)
        
            


# Copy Linked List with Random Pointer
# You are given the head of a linked list of length n. Unlike a singly linked list, each node contains an additional pointer random, which may point to any node in the list, or null.

# Create a deep copy of the list.

# The deep copy should consist of exactly n new nodes, each including:

# The original value val of the copied node
# A next pointer to the new node corresponding to the next pointer of the original node
# A random pointer to the new node corresponding to the random pointer of the original node
# Note: None of the pointers in the new list should point to nodes in the original list.

# Return the head of the copied linked list.

# In the examples, the linked list is represented as a list of n nodes. Each node is represented as a pair of [val, random_index] where random_index is the index of the node (0-indexed) that the random pointer points to, or null if it does not point to any node.

# Example 1:



# Input: head = [[3,null],[7,3],[4,0],[5,1]]

# Output: [[3,null],[7,3],[4,0],[5,1]]
# Example 2:



# Input: head = [[1,null],[2,2],[3,2]]

# Output: [[1,null],[2,2],[3,2]]
# Constraints:

# 0 <= n <= 100
# -100 <= Node.val <= 100
# random is null or is pointing to some node in the linked list.


# Recommended Time & Space Complexity
# You should aim for a solution as good or better than O(n) time and O(n) space, where n is the length of the given list.


# Hint 1
# There is an extra random pointer for each node, and unlike the next pointer, which points to the next node, the random pointer can point to any random node in the list. A deep copy is meant to create completely separate nodes occupying different memory. Why can't we build a new list while iterating through the original list?


# Hint 2
# Because, while iterating through the list, when we encounter a node and create a copy of it, we can't immediately assign the random pointer's address. This is because the random pointer might point to a node that has not yet been created. To solve this, we can first create copies of all the nodes in one iteration. However, we still can't directly assign the random pointers since we don't have the addresses of the copies of those random pointers. Can you think of a data structure to store this information? Maybe a hash data structure could help.


# Hint 3
# # We can use a hash data structure, such as a hash map, which takes O(1) time to retrieve data. This can help by mapping the original nodes to their corresponding copies. This way, we can easily retrieve the copy of any node and assign the random pointers in a subsequent pass after creating copies of all nodes in the first pass.