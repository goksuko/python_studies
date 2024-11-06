from typing import List
from collections import defaultdict

class Solution:
    def containsDuplicate3(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))


    def containsDuplicate2(self, nums: List[int]) -> bool:
        map = {}
        for n in nums:
            if n in map:
                return True
            else:
                map[n] = 1
        return False

    def containsDuplicate(self, nums: List[int]) -> bool:
        if (len(nums) == 1):
            return False
        nums.sort()        
        for i in range(1, len(nums)):
            if nums[i - 1] == nums[i]:
                return True
        return False
            
nums = [1,2,3,1]
sol = Solution()
print(sol.containsDuplicate2(nums)) # True
nums = [1,2,3,4]
print(sol.containsDuplicate2(nums)) # False
nums = [1,1,1,3,3,4,3,2,4,2]
print(sol.containsDuplicate2(nums)) # True
            


# 217. Contains Duplicate
# Easy

# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

# Example 1:

# Input: nums = [1,2,3,1]

# Output: true

# Explanation:

# The element 1 occurs at the indices 0 and 3.

# Example 2:

# Input: nums = [1,2,3,4]

# Output: false

# Explanation:

# All elements are distinct.

# Example 3:

# Input: nums = [1,1,1,3,3,4,3,2,4,2]

# Output: true