from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r - l) // 2
            if nums[m] < nums[r]:
                r = m # r = m - 1 does not work well
            else:
                l = m + 1
        return nums[l]
    
    #edge cases does not work well
    def findMin2(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            i = l + (r-l) // 2
            print(f"i: {i}")
            if i == len(nums) - 1:
                return nums[0]
            if nums[i] > nums[i+1]:
                return nums[i + 1]
            if nums[i] < nums[i//2]:
                r = i - 1
            else:
                l = i + 1
        return nums[0]
        
	
            
        
        
sol = Solution()
nums = [3,4,5,6,1,2]
print("")
print(f"nums: {nums}")
print(f"1 => {sol.findMin(nums)}")  
nums = [4,5,0,1,2,3]
print("")
print(f"nums: {nums}")
print(f"0 => {sol.findMin(nums)}")  
nums = [4,5,6,7]
print("")
print(f"nums: {nums}")
print(f"4 => {sol.findMin(nums)}")  
nums = [4,5,6,7]
print("")
print(f"nums: {nums}")
print(f"4 => {sol.findMin(nums)}")  
nums=[5,1,2,3,4]
print("")
print(f"nums: {nums}")
print(f"1 => {sol.findMin(nums)}")  






# Find Minimum in Rotated Sorted Array
# You are given an array of length n which was originally sorted in ascending order. It has now been rotated between 1 and n times. For example, the array nums = [1,2,3,4,5,6] might become:

# [3,4,5,6,1,2] if it was rotated 4 times.
# [1,2,3,4,5,6] if it was rotated 6 times.
# Notice that rotating the array 4 times moves the last four elements of the array to the beginning. Rotating the array 6 times produces the original array.

# Assuming all elements in the rotated sorted array nums are unique, return the minimum element of this array.

# A solution that runs in O(n) time is trivial, can you write an algorithm that runs in O(log n) time?

# Example 1:

# Input: nums = [3,4,5,6,1,2]

# Output: 1
# Example 2:

# Input: nums = [4,5,0,1,2,3]

# Output: 0
# Example 3:

# Input: nums = [4,5,6,7]

# Output: 4
# Constraints:

# 1 <= nums.length <= 1000
# -1000 <= nums[i] <= 1000


# Recommended Time & Space Complexity
# You should aim for a solution with O(logn) time and O(1) space, where n is the size of the input array.


# Hint 1
# A brute force solution would be to do a linear search on the array to find the minimum element. This would be an O(n) solution. Can you think of a better way? Maybe an efficient searching algorithm is helpful.


# Hint 2
# Given that the array is rotated after sorting, elements from the right end are moved to the left end one by one. This creates two parts of a sorted array, separated by a deflection point caused by the rotation. For example, consider the array [3, 4, 1, 2]. Here, the array is rotated twice, resulting in two sorted segments: [3, 4] and [1, 2]. And the minimum element will be the first element of the right segment. Can you do a binary search to find this cut?


# Hint 3
# We perform a binary search on the array with pointers l and r, which belong to two different sorted segments. For example, in [3, 4, 5, 6, 1, 2, 3], l = 0, r = 6, and mid = 3. At least two of l, mid, and r will always be in the same sorted segment. Can you find conditions to eliminate one half and continue the binary search? Perhaps analyzing all possible conditions for l, mid, and r would help.


# Hint 4
# There will be two conditions where l and mid will be in left sorted segment or mid and r will be in right sorted segement. If l and mid in sorted segement, then nums[l] < nums[mid] and the minimum element will be in the right part. If mid and r in sorted segment, then nums[m] < nums[r] and the minimum element will be in the left part. After the binary search we end up finding the minimum element.