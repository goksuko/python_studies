class Solution(object):
    #  my working solution
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """   
        start, end = 0, 0
        ones = 0
        flip = k
        ans = 0
        while end < len(nums):
            if nums[end] == 1:
                end += 1
                ones += 1
            elif flip:
                end += 1
                ones += 1
                flip -= 1
            else:
                while nums[start] == 1:
                    start += 1
                    ones -= 1
                start += 1
                flip += 1
                ones -= 1
            if ones > ans:
                ans = ones
        return ans
    
    
    
    #  older solution
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """                 
        start = 0
        end = 0
        while end < len(nums):
            if nums[end] == 0:
                k -= 1
            end += 1
            if k < 0:
                if nums[start] == 0:
                    k += 1
                start += 1
            print(f"start: {start}, end: {end}, k: {k}")
        return end - start                
        
sol  = Solution()
nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
print(nums)
print(f"6 => {sol.longestOnes(nums, k)}")
nums = [1,1,1,0,0,0]
k = 2
print(nums)
print(f"5 => {sol.longestOnes(nums, k)}")
nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k = 3
print(nums)
print(f"10 => {sol.longestOnes(nums, k)}")


# Popular Company Questions by Topic – Vol. 2
# Sliding Window & Two Pointer

# 1004. Max Consecutive Ones III
# Medium

# Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

 # Example 1:

# Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
# Output: 6
# Explanation: [1,1,1,0,0,1,1,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
# Example 2:

# Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
# Output: 10
# Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
 

# Constraints:

# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.
# 0 <= k <= nums.length