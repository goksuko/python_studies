from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i + 1]:
                return True
            i += 1

        return False

# Time complexity: O(nlog⁡n)
# Space complexity: O(1) or O(n) depending on the sorting algorithm.


# Duplicate Integer
# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

# Example 1:

# Input: nums = [1, 2, 3, 3]

# Output: true
# Example 2:

# Input: nums = [1, 2, 3, 4]

# Output: false