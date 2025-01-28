# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def mergeTwoLists(self, list1, list2): # beats 100 %
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()
        current = dummy

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        if list1:
            current.next = list1
        elif list2:
            current.next = list2

        return dummy.next
    
    def mergeTwoLists(self, list1, list2): #beats 24%
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not temp1:
            return temp2
        if not temp2:
            return temp1
        temp1 = list1
        temp2 = list2
        if temp1.val < temp2.val:
            head = temp1
            temp1 = temp1.next
        else:
            head = temp2
            temp2 = temp2.next
        temp3 = head
        while temp1 and temp2:
            if temp1.val < temp2.val:
                temp3.next = temp1
                temp1 = temp1.next
            else:
                temp3.next = temp2
                temp2 = temp2.next
            temp3 = temp3.next
        while temp1:
            temp3.next = temp1
            temp1 = temp1.next
            temp3 = temp3.next
        while temp2:
            temp3.next = temp2
            temp2 = temp2.next
            temp3 = temp3.next        
        
        return head




# 21. Merge Two Sorted Lists
# Easy

# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

 

# Example 1:


# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# Example 2:

# Input: list1 = [], list2 = []
# Output: []
# Example 3:

# Input: list1 = [], list2 = [0]
# Output: [0]
 

# Constraints:

# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# Both list1 and list2 are sorted in non-decreasing order.