class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [1] * len(nums)
        pre = 1
        for i in range(len(nums)):
            res[i] = pre
            pre *= nums[i]
        post = 1
        for i in range(len(nums) - 1 , -1, -1):
            res[i] *= post #attention here!
            post *= nums[i]
        return res
    
sol = Solution()
nums = [1,2,3,4]
print(f"[24,12,8,6] => {sol.productExceptSelf(nums)}")
nums = [-1,1,0,-3,3]
print(f"[0,0,9,0,0] => {sol.productExceptSelf(nums)}")
nums = [1,2,4,6]
print(f"[48,24,12,8] => {sol.productExceptSelf(nums)}")
nums = [-1,0,1,2,3]
print(f"[0,-6,0,0,0] => {sol.productExceptSelf(nums)}")

# 238. Product of Array Except Self
# Medium

# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

 

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
 

# Constraints:

# 2 <= nums.length <= 105
# -30 <= nums[i] <= 30
# The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.
 

# Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)