from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def printList(self, head):
        curr = head
        while curr:
            print(curr.val)
            curr = curr.next
        print("------")
            
# Recursion
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur = head
        group = 0
        while cur and group < k:
            cur = cur.next
            group += 1

        if group == k:
            cur = self.reverseKGroup(cur, k)
            while group > 0:
                tmp = head.next
                head.next = cur
                cur = head
                head = tmp
                group -= 1
            head = cur
        return head
            
            
#Iteration            
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            kth = self.getKth(groupPrev, k)
            if not kth:
                break
            groupNext = kth.next

            prev, curr = kth.next, groupPrev.next
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp
        return dummy.next

    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
    
    #non-working
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        i = 0
        curr = head
        while curr:
            i += 1
            curr = curr.next
        #[1,2,3,4,5,6]
        prev = None
        curr = head
        for j in range(k):
            after = curr.next
            curr.next = prev
            newHead = curr
            prev = curr #3
            curr = after #4
        head.next = after
        #[3,2,1,4,5,6]
        one = head
        four = curr
        prev = None
        # print(f"prev: {prev.val}, curr: {curr.val}, after: {after.val}")
        # trial = newHead
        # while trial:
        #     print(f"node: {trial.val}, node.next: {trial.next.val}")
        #     trial = trial.next
        i -= k
        while i >= k:
            for j in range(k):
                # print(f"prev: {prev.val}, curr: {curr.val}, after: {after.val}")
                after = curr.next
                curr.next = prev
                prev = curr
                curr = after
            four.next = after
            one.next = prev
            i -= k
        #[3,2,1,6,5,4]
        return newHead
        
         
sol = Solution()
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
sol.printList(head)
head = sol.reverseKGroup(head, 3)
sol.printList(head)
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
sol.printList(head)
head = sol.reverseKGroup(head, 3)
sol.printList(head)
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
sol.printList(head)
head = sol.reverseKGroup(head, 2)
sol.printList(head)
        

# Reverse Nodes in K-Group
# You are given the head of a singly linked list head and a positive integer k.

# You must reverse the first k nodes in the linked list, and then reverse the next k nodes, and so on. If there are fewer than k nodes left, leave the nodes as they are.

# Return the modified list after reversing the nodes in each group of k.

# You are only allowed to modify the nodes' next pointers, not the values of the nodes.

# Example 1:



# Input: head = [1,2,3,4,5,6], k = 3

# Output: [3,2,1,6,5,4]
# Example 2:



# Input: head = [1,2,3,4,5], k = 3

# Output: [3,2,1,4,5]

# head=[1,2,3,4,5,6]
# k=2

# Expected output:

# [2,1,4,3,6,5]
# Constraints:

# The length of the linked list is n.
# 1 <= k <= n <= 100
# 0 <= Node.val <= 100


# Recommended Time & Space Complexity
# You should aim for a solution with O(n) time and O(1) space, where n is the length of the given list.


# Hint 1
# A brute-force solution would involve storing the linked list node values in an array, reversing the k groups one by one, and then converting the array back into a linked list, requiring extra space of O(n). Can you think of a better way? Perhaps you could apply the idea of reversing a linked list in-place without using extra space.


# Hint 2
# We can avoid extra space by reversing each group in-place while keeping track of the head of the next group. For example, consider the list [1, 2, 3, 4, 5] with k = 2. First, we reverse the group [1, 2] to [2, 1]. Then, we reverse [3, 4], resulting in [2, 1, 4, 3, 5]. While reversing [3, 4], we need to link 1 to 4 and also link 3 to 5. How can we efficiently manage these pointers?


# Hint 3
# We create a dummy node to handle modifications to the head of the linked list, pointing its next pointer to the current head. We then iterate k nodes, storing the address of the next group's head and tracking the tail of the previous group. After reversing the current group, we reconnect it by linking the previous group's tail to the new head and the current group's tail to the next group's head. This process is repeated for all groups, and we return the new head of the linked list.