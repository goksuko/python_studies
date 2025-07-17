
class Solution(object):
	def searchInsert(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: int
		"""
		r = 0
		l = len(nums) - 1
		while (r <= l):
			mid = (r + l) // 2
			if nums[mid] == target:
				return mid
			elif nums[mid] < target:
				r = mid + 1
			else:
				l = mid - 1
		return r
				
sol = Solution()
nums = [1, 3, 5, 6]
target = 5
print("2:", sol.searchInsert(nums, target))  # Output: 2
nums = [1, 3, 5, 6]
target = 2
print("1:", sol.searchInsert(nums, target))  # Output: 1
				

# Popular Company Questions by Topic – Vol. 2
# Binary Search

# 35. Search Insert Position
# Easy

# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

# Example 1:

# Input: nums = [1,3,5,6], target = 5
# Output: 2
# Example 2:

# Input: nums = [1,3,5,6], target = 2
# Output: 1
# Example 3:

# Input: nums = [1,3,5,6], target = 7
# Output: 4
 

# Constraints:

# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums contains distinct values sorted in ascending order.
# -104 <= target <= 104