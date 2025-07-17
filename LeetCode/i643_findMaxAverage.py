
class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        # Calculate sum of first window
        current_sum = sum(nums[:k])
        max_sum = current_sum
        
        # Sliding window: remove first element, add next element
        for i in range(k, len(nums)):
            current_sum = current_sum - nums[i-k] + nums[i]
            max_sum = max(max_sum, current_sum)
            
        return float(max_sum)/float(k)      
    
    
sol = Solution()
nums = [1,12,-5,-6,50,3]
k = 4
print(f"12.75000 => {sol.findMaxAverage(nums, k)}")
nums = [5]
k = 1
print(f"5.00000 => {sol.findMaxAverage(nums, k)}")

# 643. Maximum Average Subarray I
# Easy

# You are given an integer array nums consisting of n elements, and an integer k.

# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

 

# Example 1:

# Input: nums = [1,12,-5,-6,50,3], k = 4
# Output: 12.75000
# Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
# Example 2:

# Input: nums = [5], k = 1
# Output: 5.00000
 

# Constraints:

# n == nums.length
# 1 <= k <= n <= 105
# -104 <= nums[i] <= 104