from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if target == nums[m]:
                return m

            if nums[l] <= nums[m]:
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1
                    
            else:
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1
        return -1
    
    #some edge caes do not work well
    def search2(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2
            print(f"m : {m}")
            if target == nums[m]:
                return m
            if nums[m] < nums[r]:
                if target < nums[m]:
                    r = m
                else:
                    if target < nums[r]:
                        l = m + 1
                    else:
                        r = m                   
            else:
                if target > nums[m]:
                    l = m + 1
                else:
                    if target < nums[r]:
                        l = m + 1
                    else:
                        r = m
        return -1        

sol = Solution()
nums = [3,4,5,6,1,2]
target = 1
print("")
print(f"nums: {nums}, target: {target}")
print(f"4 => {sol.search(nums, target)}")  
nums = [3,5,6,0,1,2]
target = 4
print("")
print(f"nums: {nums}, target: {target}")
print(f"-1 => {sol.search(nums, target)}")  
nums = [11,12,0,1,2,3,4,5,6,7,8,9,10]
target = 1
print("")
print(f"nums: {nums}, target: {target}")
print(f"3 => {sol.search(nums, target)}")  
nums = [1]
target = 1
print("")
print(f"nums: {nums}, target: {target}")
print(f"0 => {sol.search(nums, target)}")  
nums = [1,3]
target = 3
print("")
print(f"nums: {nums}, target: {target}")
print(f"1 => {sol.search(nums, target)}")  

# Search in Rotated Sorted Array
# You are given an array of length n which was originally sorted in ascending order. It has now been rotated between 1 and n times. For example, the array nums = [1,2,3,4,5,6] might become:

# [3,4,5,6,1,2] if it was rotated 4 times.
# [1,2,3,4,5,6] if it was rotated 6 times.
# Given the rotated sorted array nums and an integer target, return the index of target within nums, or -1 if it is not present.

# You may assume all elements in the sorted rotated array nums are unique,

# A solution that runs in O(n) time is trivial, can you write an algorithm that runs in O(log n) time?

# Example 1:

# Input: nums = [3,4,5,6,1,2], target = 1

# Output: 4
# Example 2:

# Input: nums = [3,5,6,0,1,2], target = 4

# Output: -1
# Constraints:

# 1 <= nums.length <= 1000
# -1000 <= nums[i] <= 1000
# -1000 <= target <= 1000


# Recommended Time & Space Complexity
# You should aim for a solution with O(logn) time and O(1) space, where n is the size of the input array.


# Hint 1
# A brute force solution would be to do a linear search on the array to find the target element. This would be an O(n) solution. Can you think of a better way? Maybe an efficient searching algorithm is helpful.


# Hint 2
# Given that the array is rotated after sorting, elements from the right end are moved to the left end one by one, creating two sorted segments separated by a deflection point due to the rotation. For example, consider the array [3, 4, 1, 2], which is rotated twice, resulting in two sorted segments: [3, 4] and [1, 2]. In a fully sorted array, it's easy to find the target. So, if you can identify the deflection point (cut), you can perform a binary search on both segments to find the target element. Can you use binary search to find this cut?


# Hint 3
# We perform a binary search on the array with pointers l and r, which belong to two different sorted segments. For example, in [3, 4, 5, 6, 1, 2, 3], l = 0, r = 6, and m = 3. At least two of l, m, and r will always be in the same sorted segment. Can you find conditions to eliminate one half and continue the binary search? Perhaps analyzing all possible conditions for l, m, and r may help.


# Hint 4
# There are two cases: l and m belong to the left sorted segment, or m and r belong to the right sorted segment. If l and m are in the same segment, nums[l] < nums[m], so the pivot index must lie in the right part. If m and r are in the same segment, nums[m] < nums[r], so the pivot index must lie in the left part. After the binary search, we eventually find the pivot index. Once the pivot is found, it's straightforward to select the segment where the target lies and perform a binary search on that segement to find its position. If we don't find the target, we return -1.