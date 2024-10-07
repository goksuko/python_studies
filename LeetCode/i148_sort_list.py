from typing import List
from typing import Optional

# Definition for singly-linked list.
class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next
		
class Solution:
	def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
		sort=[]
		temp=head
		while temp != None:
			sort.append(temp.val)
			temp=temp.next
		sort=sorted(sort)
		temp=head
		i=0
		while temp!= None:
			temp.val=sort[i]
			i+=1
			temp=temp.next
		return head

sol = Solution()
print(sol.sortList([4,2,1,3]))
		


			 
			   



# 148. Sort List
# Medium

# Given the head of a linked list, return the list after sorting it in ascending order.

# Example 1:

# Input: head = [4,2,1,3]
# Output: [1,2,3,4]
# Example 2:

# Input: head = [-1,5,3,4,0]
# Output: [-1,0,3,4,5]
# Example 3:

# Input: head = []
# Output: []
 

# Constraints:

# The number of temps in the list is in the range [0, 5 * 104].
# -105 <= Node.val <= 105