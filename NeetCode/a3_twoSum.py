from typing import List 

class Solution:
# 4. Hash Map (One Pass)
    def twoSum4(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}  # val -> index

        for i, n in enumerate(nums):
            diff = target - n
            print(f"i: {i}, n: {n}, diff: {diff}")
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i

# Time complexity: O(n)
# Space complexity: O(n)         

# 3. Hash Map (Two Pass) // original did not work for my case!
    def twoSum3(self, nums: List[int], target: int) -> List[int]:
        indices = {}  # val -> index

        for i, n in reversed(list(enumerate(nums))): # reversed here and worked :) but not sure of space complexicity
            indices[n] = i

        for i, n in enumerate(nums):
            diff = target - n
            if diff in indices and indices[diff] != i:
                return [i, indices[diff]]
    
# 2. Sorting  //does not work for my case!
    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        A = []
        for i, num in enumerate(nums):
            A.append([num, i])
        print(A)
        
        A.sort()
        print(A)
        i, j = 0, len(nums) - 1
        while i < j:
            cur = A[i][0] + A[j][0]
            if cur == target:
                return [min(A[i][1], A[j][1]), 
                        max(A[i][1], A[j][1])]
            elif cur < target:
                i += 1
            else:
                j -= 1
        return []

# 1. Brute Force
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

# Time complexity: O(n2)
# Space complexity: O(1)

#anothet brute force, my solution
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = 1
        while i < len(nums):
            k = target - nums[i]
            j = i + 1
            while j < len(nums):
                if nums[j] == k:
                    return [i, j]
                j += 1
            i += 1

        


nums = [3,4,5,6,5]
sol = Solution()
print(sol.twoSum4(nums, 8))
print(sol.twoSum3(nums, 8))
print(sol.twoSum2(nums, 8))
print(sol.twoSum(nums, 8))
print(sol.twoSum(nums, 10))

# Two Integer Sum
# Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

# You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

# Return the answer with the smaller index first.

# Example 1:

# Input: 
# nums = [3,4,5,6], target = 7

# Output: [0,1]
# Explanation: nums[0] + nums[1] == 7, so we return [0, 1].

# Example 2:

# Input: nums = [4,5,6], target = 10

# Output: [0,2]
# Example 3:

# Input: nums = [5,5], target = 10

# Output: [0,1]
# Constraints:

# 2 <= nums.length <= 1000
# -10,000,000 <= nums[i] <= 10,000,000
# -10,000,000 <= target <= 10,000,000

# Recommended Time & Space Complexity
# You should aim for a solution with O(n) time and O(n) space, where n is the size of the input array.


# Hint 1
# A brute force solution would be to check every pair of numbers in the array. This would be an O(n^2) solution. Can you think of a better way? Maybe in terms of mathematical equation?


# Hint 2
# Given, We need to find indices i and j such that i != j and nums[i] + nums[j] == target. Can you rearrange the equation and try to fix any index to iterate on?


# Hint 3
# we can iterate through nums with index i. Let difference = target - nums[i] and check if difference exists in the hash map as we iterate through the array, else store the current element in the hashmap with its index and continue. We use a hashmap for O(1) lookups.