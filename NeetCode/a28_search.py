from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            # (l + r) // 2 can lead to overflow
            m = l + ((r - l) // 2)  

            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        return -1


sol = Solution()
nums=[-1,0,2,4,6,8]
target=4
print(f"\nnums: {nums}, target: {target}")
print(f"3 => {sol.search(nums, target)}")
nums=[-1,0,2,4,6,8]
target=3
print(f"\nnums: {nums}, target: {target}")
print(f"-1 => {sol.search(nums, target)}")

nums=[-1,0,3,5,9,12]
target=9
print(f"\nnums: {nums}, target: {target}")
print(f"4 => {sol.search(nums, target)}")

nums=[-1,0,3,5,9,12, 13, 17, 24, 68, 79, 80, 90]
target=79
print(f"\nnums: {nums}, target: {target}")
print(f"10 => {sol.search(nums, target)}")

            
                
                
        
        

# Binary Search
# You are given an array of distinct integers nums, sorted in ascending order, and an integer target.

# Implement a function to search for target within nums. If it exists, then return its index, otherwise, return -1.

# Your solution must run in O(logn) time.

# Example 1:

# Input: nums = [-1,0,2,4,6,8], target = 4

# Output: 3
# Example 2:

# Input: nums = [-1,0,2,4,6,8], target = 3

# Output: -1
# Constraints:

# 1 <= nums.length <= 10000.
# -10000 < nums[i], target < 10000


# Recommended Time & Space Complexity
# You should aim for a solution with O(logn) time and O(1) space, where n is the size of the input array.


# Hint 1
# Can you find an algorithm that is useful when the array is sorted? Maybe other than linear seacrh.


# Hint 2
# The problem name is the name of the algorithm that we can use. We need to find a target value and if it does not exist in the array return -1. We have l and r as the boundaries of the segment of the array in which we are searching. Try building conditions to eliminate half of the search segment at each step. Maybe sorted nature of the array can be helpful.


# Hint 3
# We compare the target value with the mid of the segment. For example, consider the array [1, 2, 3, 4, 5] and target = 4. The mid value is 3, thus, on the next iteration we search to the right of mid. The remaining segment is [4,5]. Why?


# Hint 4
# Because the array is sorted, all elements to the left of mid (including 3) are guaranteed to be smaller than the target. Therefore, we can safely eliminate that half of the array from consideration, narrowing the search to the right half and repeat this search until we find the target