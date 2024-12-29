from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            after = curr.next
            curr.next = prev
            prev = curr
            curr = after
        return prev
    
    def printList(self, head: Optional[ListNode]) -> None:
        while head:
            print(head.val)
            head = head.next
        print("")

    
    
sol = Solution()
head = ListNode(0, ListNode(1, ListNode(2, ListNode(3))))
print("")
print(f"head: {head}")
print(f"[3,2,1,0] => ")
sol.printList(sol.reverseList(head))
head = None
print("")
print(f"head: {head}")
print(f"[] => ")
sol.printList(sol.reverseList(head))
      
head = ListNode(0)
print("")
print(f"head: {head}")
print(f"[0] => ")   
sol.printList(sol.reverseList(head))    


# Reverse Linked List
# Given the beginning of a singly linked list head, reverse the list, and return the new beginning of the list.

# Example 1:

# Input: head = [0,1,2,3]

# Output: [3,2,1,0]
# Example 2:

# Input: head = []

# Output: []
# Constraints:

# 0 <= The length of the list <= 1000.
# -1000 <= Node.val <= 1000


# Recommended Time & Space Complexity
# You should aim for a solution with O(n) time and O(1) space, where n is the length of the given list.


# Hint 1
# A brute force solution would be to store the node values of the linked list into an array, then reverse the array, convert it back into a linked list, and return the new linked list's head. This would be an O(n) time solution but uses extra space. Can you think of a better way? Maybe there is an approach to reverse a linked list in place.


# Hint 2
# As you can see, the head of the linked list becomes the tail after we reverse it. Can you think of an approach to change the references of the node pointers? Perhaps reversing a simple two-node list might help clarify the process.


# Hint 3
# For example, consider a list [2, 3], where 2 is the head of the list and 3 is the tail. When we reverse it, 3 becomes the new head, and its next pointer will point to 2. Then, 2's next pointer will point to null. Can you figure out how to apply this approach to reverse a linked list of length n by iterating through it?


# Hint 4
# We can reverse the linked list in place by reversing the pointers between two nodes while keeping track of the next node's address. Before changing the next pointer of the current node, we must store the next node to ensure we don't lose the rest of the list during the reversal. This way, we can safely update the links between the previous and current nodes.