from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:    

#recursion
    def reorderList1(self, head: Optional[ListNode]) -> None:

        def rec(root: ListNode, cur: ListNode) -> ListNode:
            if not cur:
                return root
            root = rec(root, cur.next)

            if not root:
                return None
            tmp = None
            if root == cur or root.next == cur:
                cur.next = None
            else:
                tmp = root.next
                root.next = cur
                cur.next = tmp
            return tmp
            
        head = rec(head, head.next)

# reverse and merge
    def reorderList2(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2

#my solution enhanced          
    def reorderList(self, head: Optional[ListNode]) -> None:
        def reverse(head: Optional[ListNode]) -> Optional[ListNode]:                     
            prev = None
            curr = head
            while curr:          
                after = curr.next
                curr.next = prev
                prev = curr
                curr = after
            return prev
        
        def printList(head: Optional[ListNode]) -> None:
            curr = head
            while curr:
                print(curr.val)
                curr = curr.next
            print("----") 
        
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = reverse(slow)
        printList(head)
        printList(second)
        curr = head
        while curr:
            after = curr.next # 1
            curr.next = second # 0->7
            later = second.next # 6
            second.next = after # 7-> 1
            second = later # 6
            curr = after # 1
        printList(head)


#my solution           
    def reorderList3(self, head: Optional[ListNode]) -> None:
        def reverse(head: Optional[ListNode]) -> Optional[ListNode]:
                     
            prev = None
            curr = head
            while curr:          
                after = curr.next
                curr.next = prev
                prev = curr
                curr = after
            return prev
        
        def printList(head: Optional[ListNode]) -> None:
            curr = head
            while curr:
                print(curr.val)
                curr = curr.next
            print("----") 
        
        i = 0
        curr = head
        while curr.next:
            i += 1
            curr = curr.next
        last = curr
        curr = head
        for n in range(i // 2):
            print(f"curr.val: {curr.val}")
            curr = curr.next
        second = reverse(curr)
        printList(head)
        printList(second)
        curr = head
        while curr:
            after = curr.next # 1
            curr.next = second # 0->7
            later = second.next # 6
            second.next = after # 7-> 1
            second = later # 6
            curr = after # 1
        printList(head)
            
            
        
        
sol = Solution()
head = ListNode(0, ListNode(1, ListNode(2, (ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7)))))))))
# sol.printList(head)
sol.reorderList(head)
# sol.printList(head)
    
    
    
    
        
        
        



# Reorder Linked List
# You are given the head of a singly linked-list.

# The positions of a linked list of length = 7 for example, can intially be represented as:

# [0, 1, 2, 3, 4, 5, 6]

# Reorder the nodes of the linked list to be in the following order:

# [0, 6, 1, 5, 2, 4, 3]

# Notice that in the general case for a list of length = n the nodes are reordered to be in the following order:

# [0, n-1, 1, n-2, 2, n-3, ...]

# You may not modify the values in the list's nodes, but instead you must reorder the nodes themselves.

# Example 1:

# Input: head = [2,4,6,8]

# Output: [2,8,4,6]
# Example 2:

# Input: head = [2,4,6,8,10]

# Output: [2,10,4,8,6]
# Constraints:

# 1 <= Length of the list <= 1000.
# 1 <= Node.val <= 1000


# Recommended Time & Space Complexity
# You should aim for a solution with O(n) time and O(1) space, where n is the length of the given list.


# Hint 1
# A brute force solution would be to store the node values of the list in an array, reorder the values, and create a new list. Can you think of a better way? Perhaps you can try reordering the nodes directly in place, avoiding the use of extra space.


# Hint 2
# For example, consider the list [1, 2, 3, 4, 5]. To reorder the list, we connect the first and last nodes, then continue with the second and second-to-last nodes, and so on. Essentially, the list is split into two halves: the first half remains as is, and the second half is reversed and merged with the first half. For instance, [1, 2] will merge with the reversed [5, 4, 3]. Can you figure out a way to implement this reordering process? Maybe dividing the list into two halves could help.


# Hint 3
# We can divide the list into two halves using the fast and slow pointer approach, which helps identify the midpoint of the list. This allows us to split the list into two halves, with the heads labeled as l1 and l2. Next, we reverse the second half (l2). After these steps, we proceed to reorder the two lists by iterating through them node by node, updating the next pointers accordingly.

