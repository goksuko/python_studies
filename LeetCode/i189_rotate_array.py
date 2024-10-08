from typing import List


class Solution:
	
	def rotate(self, nums: List[int], k: int) -> None:
		k = k % len(nums)
		r = len(nums) - k
		new = nums[0:r]
		nums[0:r] = []
		nums.extend(new)

#below does in space O(1), I did :)
	def rotate2(self, nums: List[int], k: int) -> None:
		"""
		Do not return anything, modify nums in-place instead.
		"""
		def reverse(nums):
			i = 0
			leng = len(nums)
			while i < leng // 2:
				temp = nums[i]
				nums[i] = nums[- i - 1]
				nums[- i - 1] = temp
				i += 1
			return nums
			
		if k == 0:
			return
		k = k % len(nums)
		nums = reverse(nums)
		nums[:k] = reverse(nums[:k])
		nums[k:] = reverse(nums[k:])
		# print(nums)

sol = Solution()
print([5, 6, 7, 1, 2, 3, 4])
sol.rotate([1,2,3,4,5,6,7], 3)
print([2, 1])
sol.rotate([1,2], 3)
print([3,1,2])
sol.rotate([1,2,3], 4)
# print(sol.rotate())
# print(sol.rotate())
# print(sol.rotate())


# 189. Rotate Array
# Medium

# Hint
# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

# Example 1:

# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
# Example 2:

# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation: 
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]
 

# Constraints:

# 1 <= nums.length <= 105
# -231 <= nums[i] <= 231 - 1
# 0 <= k <= 105
 

# Follow up:

# Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
# Could you do it in-place with O(1) extra space?