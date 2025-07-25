

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    # faster
    def oddEvenList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head
        
        odd=head
        even=head.next
        even_head=even

        while even and even.next:
            odd.next=even.next #1->3
            odd=odd.next #3

            even.next=odd.next #2->4
            even=even.next #4
        
        odd.next=even_head
        return head
    
    
    # my solution
    def oddEvenList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head:
            return None
        if not head.next or not head.next.next:
            return head
        odd = head
        even = head.next
        # print(f"odd: {odd.val}, even: {even.val}")
        even_head = even
        while odd.next and odd.next.next:
            old_odd = odd #1 #3
            old_even = even #2 #4
            # print(f"old_odd: {old_odd.val}, old_even: {old_even.val}")
            odd = odd.next.next #3 #5
            # print(f"odd: {odd.val}, even: {even.val}")
            old_odd.next = odd #1->3 #3->5
            if even.next:
                even = even.next.next #4 #6
            # print(f"old_odd.next: {old_odd.next.val}")
            old_even.next = even #2->4 #4->6
            # print(f"old_even.next: {old_even.next.val}")
            # print_nodes(head)
        odd.next = even_head
        return head
        
head = ListNode(1)
head.val = 1
old = head
for i in range(2,6):
    curr = ListNode(i)
    curr.val = i
    old.next = curr
    old = curr

def print_nodes(head):
    curr = head
    while curr:
        print(f"{curr.val}", end=" ")
        curr = curr.next
    print()
    
sol = Solution()
print_nodes(head)
new_head = sol.oddEvenList(head)
print_nodes(new_head)
# print(new_head.val)
                

            
        

# 328. Odd Even Linked List
# Medium

# Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

# The first node is considered odd, and the second node is even, and so on.

# Note that the relative order inside both the even and odd groups should remain as it was in the input.

# You must solve the problem in O(1) extra space complexity and O(n) time complexity.

 

# Example 1:


# Input: head = [1,2,3,4,5]
# Output: [1,3,5,2,4]
# Example 2:


# Input: head = [2,1,3,5,6,4,7]
# Output: [2,3,6,7,1,5,4]
 

# Constraints:

# The number of nodes in the linked list is in the range [0, 104].
# -106 <= Node.val <= 106