from typing import List

class Solution:
	def twoSum(self, numbers: List[int], target: int) -> List[int]:
		l = 0
		r = len(numbers) - 1
		while l < r:
			if numbers[l] + numbers[r] == target:
				return [l+1, r+1]			
			elif numbers[l] + numbers[r] > target:
				r -= 1
			elif numbers[l] + numbers[r] < target:
				l += 1
				
	

	#below is mine O(n^2)
	def twoSum2(self, numbers: List[int], target: int) -> List[int]:
		for n in range(len(numbers)):
			k = n + 1
			new = target - numbers[n]
			while numbers[k] <= new:
				if numbers[k] == new:
					return [n+1, k+1]
				k += 1

sol = Solution()
print(sol.twoSum([1,2,3,4], 3))



# Two Integer Sum II
# Given an array of integers numbers that is sorted in non-decreasing order.

# Return the indices (1-indexed) of two numbers, [index1, index2], such that they add up to a given target number target and index1 < index2. Note that index1 and index2 cannot be equal, therefore you may not use the same element twice.

# There will always be exactly one valid solution.

# Your solution must use 
# O
# (
# 1
# )
# O(1) additional space.

# Example 1:

# Input: numbers = [1,2,3,4], target = 3

# Output: [1,2]
# Explanation:
# The sum of 1 and 2 is 3. Since we are assuming a 1-indexed array, index1 = 1, index2 = 2. We return [1, 2].

# Constraints:

# 2 <= numbers.length <= 1000
# -1000 <= numbers[i] <= 1000
# -1000 <= target <= 1000


# Recommended Time & Space Complexity
# You should aim for a solution with O(n) time and O(1) space, where n is the size of the input array.


# Hint 1
# A brute force solution would be to check every pair of numbers in the array. This would be an O(n^2) solution. Can you think of a better way?


# Hint 2
# Can you think of an algorithm by taking the advantage of array being sorted?


# Hint 3
# We can use the two-pointer algorithm. If nums[0] + nums[n-1] > target, then we know nums[n - 1] can not possibly be included in any pairs. Why? Because nums[n - 1] is the largest element in the array. Even by adding it with nums[0], which is the smallest element, we still exceed the target. You can think of the case when nums[0] + nums[n - 1] < target.


# Hint 4
# We keep two pointers, one at the start and the other at the end of the array. If the sum of the numbers at the two pointers is greater than the target, decrement the right pointer, else increment the left pointer. Repeat this process until you find a valid pair.