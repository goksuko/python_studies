from typing import Optional
from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    #recursion
    def add(self, l1: Optional[ListNode], l2: Optional[ListNode], carry: int) -> Optional[ListNode]:
        if not l1 and not l2 and carry == 0:
            return None
        
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0
        
        carry, val = divmod(v1 + v2 + carry, 10)
        
        next_node = self.add(
            l1.next if l1 else None, 
            l2.next if l2 else None, 
            carry
        )
        return ListNode(val, next_node)

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return self.add(l1, l2, 0)
    
    
    #iteration
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy

        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # new digit
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            cur.next = ListNode(val)

            # update ptrs
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next

#my solution
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        c1 = l1
        c2 = l2
        d = []
        hand = 0
        while c1 or c2:
            if c1:
                s1 = c1.val
                c1 = c1.next
            else:
                s1 = 0
            if c2:
                s2 = c2.val
                c2 = c2.next
            else:
                s2 = 0
            sum = s1 + s2 + hand
            hand = 0
            if sum > 9:
                hand = 1
            d.append(sum % 10)      
        if hand == 1:
            d.append(1)
        print(d) # [5, 7, 9]
        old = ListNode(d[-1], None) # 9
        new = old
        d.pop()
        while d:
            print(d) # [5, 7]
            new = ListNode(d.pop(), old) # 7->9
            old = new
        return new
            
                
            
            
        
        
        
sol = Solution()
l1 = ListNode(1, ListNode(2, ListNode(3)))
l2 = ListNode(4, ListNode(5, ListNode(6)))
print("")
print(f"nums1: {l1}, nums2: {l2}")
print(f"[5,7,9] => {sol.addTwoNumbers(l1, l2)}")    
# Explanation: 321 + 654 = 975.
     
l1 = ListNode(9)
l2 = ListNode(9)
print("")
print(f"nums1: {l1}, nums2: {l2}")
print(f"[8,1] => {sol.addTwoNumbers(l1, l2)}")
l1 = ListNode(9, ListNode(1))
l2 = ListNode(9, ListNode(1))
print("")
print(f"nums1: {l1}, nums2: {l2}")
print(f"[8,3] => {sol.addTwoNumbers(l1, l2)}")
# Explanation: 19 + 19 = 38.
l1 = ListNode(8, ListNode(9, ListNode(1)))
l2 = ListNode(7, ListNode(9, ListNode(1)))
print("")
print(f"nums1: {l1}, nums2: {l2}")
print(f"[5, 9, 3] => {sol.addTwoNumbers(l1, l2)}")
# Explanation: 198 + 197 = 395.
l1 = ListNode(9, ListNode(1))
l2 = ListNode(7, ListNode(9, ListNode(1)))
print("")
print(f"nums1: {l1}, nums2: {l2}")
print(f"[6, 1, 2] => {sol.addTwoNumbers(l1, l2)}")
# Explanation: 19 + 197 = 216.
l1 = ListNode(0)
l2 = ListNode(0)
print("")
print(f"nums1: {l1}, nums2: {l2}")
print(f"[0] => {sol.addTwoNumbers(l1, l2)}")
        


# Add Two Numbers
# You are given two non-empty linked lists, l1 and l2, where each represents a non-negative integer.

# The digits are stored in reverse order, e.g. the number 123 is represented as 3 -> 2 -> 1 -> in the linked list.

# Each of the nodes contains a single digit. You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Return the sum of the two numbers as a linked list.

# Example 1:



# Input: l1 = [1,2,3], l2 = [4,5,6]

# Output: [5,7,9]

# Explanation: 321 + 654 = 975.
# Example 2:

# Input: l1 = [9], l2 = [9]

# Output: [8,1]
# Constraints:

# 1 <= l1.length, l2.length <= 100.
# 0 <= Node.val <= 9


# Recommended Time & Space Complexity
# You should aim for a solution with O(m + n) time and O(1) space, where m is the length of list l1 and n is the length of list l2.


# Hint 1
# Try to visualize the addition of two numbers. We know that the addition of two numbers is done by starting at the one's digit. We add the numbers by going through digit by digit. We track the extra value as a carry because the addition of two digits can result in a number with two digits. The carry is then added to the next digits, and so on. How do you implement this in case of linked lists?


# Hint 2
# We track the extra value, carry, here as well. We iterate through the lists l1 and l2 until both lists reach null. We add the values of both nodes as well as the carry. If either of the nodes is null, we add 0 in its place and continue the process while tracking the carry simultaneously. Once we complete the process, if we are left with any carry, we add an extra node with that carry value and return the head of the result list.