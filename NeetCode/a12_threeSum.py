from typing import List
from collections import defaultdict

class Solution:
	#3. Two Pointers
	def threeSum(self, nums: List[int]) -> List[List[int]]:
		res = []
		nums.sort()
		print(nums)
		# [-4, -1, -1, 0, 1, 2]

		for i, a in enumerate(nums):
			if a > 0:
				break
			print(f"Index: {i}, Number: {a}")
			# Index: 0, Number: -4
			# Index: 1, Number: -1
			# Index: 2, Number: -1
			# Index: 3, Number: 0

			if i > 0 and a == nums[i - 1]:
				continue
			# Index: 0, Number: -4
			# Index: 1, Number: -1
			######## Index: 2, Number: -1
			# Index: 3, Number: 0
			# skips duplicate elements in the outer loop to avoid processing the same element multiple times
			# as the first element of the triplet.
			# However, this does not handle duplicates for the second and the third elements.

			l, r = i + 1, len(nums) - 1
			while l < r:
				threeSum = a + nums[l] + nums[r]
				if threeSum > 0:
					r -= 1
				elif threeSum < 0:
					l += 1
				else:
					res.append([a, nums[l], nums[r]])
					l += 1
					r -= 1
					while nums[l] == nums[l - 1] and l < r:
						l += 1
					#That is, we want to skip duplicate elements for the second and the third elements of the triplet.
		return res
	
	#2. Hash Map
	def threeSum2(self, nums: List[int]) -> List[List[int]]:
		nums.sort()
		print(nums)
		# [-4, -1, -1, 0, 1, 2]
		count = defaultdict(int)
		for num in nums:
			count[num] += 1
		print(count)
		# defaultdict(<class 'int'>, {-4: 1, -1: 2, 0: 1, 1: 1, 2: 1})

		res = []
		for i in range(len(nums)):
			count[nums[i]] -= 1
			if i and nums[i] == nums[i - 1]:
				continue
				
			for j in range(i + 1, len(nums)):
				count[nums[j]] -= 1
				if j - 1 > i and nums[j] == nums[j - 1]:
					continue
				target = -(nums[i] + nums[j])
				if count[target] > 0:
					res.append([nums[i], nums[j], target])

			for j in range(i + 1, len(nums)):
				count[nums[j]] += 1
		return res
						   
sol = Solution()
print(sol.threeSum([-1,0,1,2,-1,-4]))

# 3Sum
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.

# The output should not contain any duplicate triplets. You may return the output and the triplets in any order.

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]

# Output: [[-1,-1,2],[-1,0,1]]
# Explanation:
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].

# Example 2:

# Input: nums = [0,1,1]

# Output: []
# Explanation: The only possible triplet does not sum up to 0.

# Example 3:

# Input: nums = [0,0,0]

# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.

# Constraints:

# 3 <= nums.length <= 1000
# -10^5 <= nums[i] <= 10^5


# Recommended Time & Space Complexity
# You should aim for a solution with O(n^2) time and O(1) space, where n is the size of the input array.


# Hint 1
# A brute force solution would be to check for every triplet in the array. This would be an O(n^3) solution. Can you think of a better way?


# Hint 2
# Can you think of an algorithm after sorting the input array? What can we observe by rearranging the given equation in the problem?


# Hint 3
# we can iterate through nums with index i and get nums[i] = -(nums[j] + nums[k]) after rearranging the equation, making -nums[i] = nums[j] + nums[k]. For each index i, we should efficiently calculate the j and k pairs without duplicates. Which algorithm is suitable to find j and k pairs?


# Hint 4
# To efficiently find the j and k pairs, we run the two pointer approach on the elements to the right of index i as the array is sorted. When we run two pointer algorithm, consider j and k as pointers (j is at left, k is at right) and target = -nums[i], if the current sum num[j] + nums[k] < target then we need to increase the value of current sum by incrementing j pointer. Else if the current sum num[j] + nums[k] > target then we should decrease the value of current sum by decrementing k pointer. How do you deal with duplicates?


# Hint 5
# When the current sum nums[j] + nums[k] == target add this pair to the result. We can move j or k pointer until j < k and the pairs are repeated. This ensures that no duplicate pairs are added to the result.