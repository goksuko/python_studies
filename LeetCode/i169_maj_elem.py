from typing import List

class Solution:
	def majorityElement(self, nums: List[int]) -> int:
		dic = {}
		max = 0
		for n in nums:
			if n in dic:
				dic[n] += 1
			else:
				dic[n] = 1
		for key in dic:
			if dic[key] > max:
				max = dic[key]
				ans = key
		return ans

sol = Solution()
print(sol.majorityElement([3,2,3]))
print(sol.majorityElement([2,2,1,1,1,2,2]))

# 169. Majority Element
# Easy

# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

# Example 1:

# Input: nums = [3,2,3]
# Output: 3
# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2
 

# Constraints:

# n == nums.length
# 1 <= n <= 5 * 104
# -109 <= nums[i] <= 109