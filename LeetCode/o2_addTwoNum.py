from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers2(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        carry = 0
        dummy = ListNode(-1)
        cur = dummy

        while l1 or l2:
            x1 = l1.val if l1 else 0
            x2 = l2.val if l2 else 0
            partial_sum = (x1+x2+carry)
            cur.next = ListNode(partial_sum%10)
            carry = partial_sum // 10
            if l1: 
                l1 = l1.next
            if l2:
                l2 = l2.next
            
            cur = cur.next
        if carry:
            cur.next = ListNode(carry)
            cur = cur.next
        cur.next = None
        return dummy.next


    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3 = ListNode(0)
        ans = l3
        to_add = 0
        while l1 or l2:
            if l1:
                num1 = l1.val
            else:
                num1 = 0
            # num1 = l1.val if l1 else 0
            if l2:
                num2 = l2.val
            else:
                num2 = 0
            temp_val = num1 + num2 + to_add
            if temp_val >= 10:
                l3.val = temp_val - 10
                to_add = 1
            else:
                l3.val = temp_val
                to_add = 0   
            if l1:         
                l1 = l1.next
            if l2:
                l2 = l2.next
            if (l1 or l2) or to_add:
                temp = ListNode(0)
                l3.next = temp
                l3 = l3.next
        if to_add:
            l3.val = 1
        return ans
        
        
sol = Solution()
l1 = [9,9,9,9,9,9,9]        
l2 = [9,9,9,9]
print(sol.addTwoNumbers(l1, l2))

# 2. Add Two Numbers
# Medium

# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example 1:

# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
# Example 2:

# Input: l1 = [0], l2 = [0]
# Output: [0]
# Example 3:

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]

# Constraints:

# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading zeros.