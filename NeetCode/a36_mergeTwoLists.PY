from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    #recursive
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
        
# iteration
    def mergeTwoLists2(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = node = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next

        node.next = list1 or list2

        return dummy.next
    
    #my solution
    def mergeTwoLists3(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        newNode = ListNode(0)
        newHead = newNode
        while list1 and list2:
            if list1.val < list2.val:
                newNode.next = list1
                list1 = list1.next
            else:
                newNode.next = list2
                list2 = list2.next
            newNode = newNode.next
        while list1:
                newNode.next = list1
                list1 = list1.next
                newNode = newNode.next
        while list2:
                newNode.next = list2
                list2 = list2.next 
                newNode = newNode.next               
        return newHead.next
                  


# Merge Two Sorted Linked Lists
# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted linked list and return the head of the new sorted linked list.

# The new list should be made up of nodes from list1 and list2.

# Example 1:



# Input: list1 = [1,2,4], list2 = [1,3,5]

# Output: [1,1,2,3,4,5]
# Example 2:

# Input: list1 = [], list2 = [1,2]

# Output: [1,2]
# Example 3:

# Input: list1 = [], list2 = []

# Output: []
# Constraints:

# 0 <= The length of the each list <= 100.
# -100 <= Node.val <= 100


# Recommended Time & Space Complexity
# You should aim for a solution with O(n + m) time and O(1) space, where n is the length of list1 and m is the length of list2.


# Hint 1
# A brute force solution would involve storing the values of both linked lists in an array, sorting the array, and then converting it back into a linked list. This approach would use O(n) extra space and is trivial. Can you think of a better way? Perhaps the sorted nature of the lists can be leveraged.


# Hint 2
# We create a dummy node to keep track of the head of the resulting linked list while iterating through the lists. Using l1 and l2 as iterators for list1 and list2, respectively, we traverse both lists node by node to build a final linked list that is also sorted. How do you implement this?


# Hint 3
# For example, consider list1 = [1, 2, 3] and list2 = [2, 3, 4]. While iterating through the lists, we move the pointers by comparing the node values from both lists. We link the next pointer of the iterator to the node with the smaller value. For instance, when l1 = 1 and l2 = 2, since l1 < l2, we point the iterator's next pointer to l1 and proceed.