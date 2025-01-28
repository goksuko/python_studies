import math

class Solution(object):
    def maxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # from math import gcd
        # gcd = lambda a, b: a if b == 0 else gcd(b, a % b)
        def gcd(a, b):
            if b == 0:
                return a
            else:
                return gcd(b, a % b)
        
        def lcm(a, b):
            return a * b // gcd(a, b)
        
        ans = 0
        maxLcm = 100000000000
        for i in range(len(nums)):
            gcdVal = nums[i]
            lcmVal = nums[i]
            prod = 1
            for j in range(i, len(nums)):
                prod *= nums[j]
                if prod > maxLcm:
                    break
                gcdVal = gcd(gcdVal, nums[j])
                lcmVal = lcm(lcmVal, nums[j])
                if prod == gcdVal * lcmVal:
                    ans = max(ans, j - i + 1)
        return ans

            

sol = Solution()
nums = [1,2,1,2,1,1,1]
print("")
print(f"nums: {nums}")
print(f"5 => {sol.maxLength(nums)}") 

# 3411. Maximum Subarray With Equal Products
# Easy

# You are given an array of positive integers nums.

# An array arr is called product equivalent if prod(arr) == lcm(arr) * gcd(arr), where:

# prod(arr) is the product of all elements of arr.
# gcd(arr) is the GCD of all elements of arr.
# lcm(arr) is the LCM of all elements of arr.
# Return the length of the longest product equivalent subarray of nums.

 

# Example 1:

# Input: nums = [1,2,1,2,1,1,1]

# Output: 5

# Explanation: 

# The longest product equivalent subarray is [1, 2, 1, 1, 1], where prod([1, 2, 1, 1, 1]) = 2, gcd([1, 2, 1, 1, 1]) = 1, and lcm([1, 2, 1, 1, 1]) = 2.

# Example 2:

# Input: nums = [2,3,4,5,6]

# Output: 3

# Explanation: 

# The longest product equivalent subarray is [3, 4, 5].

# Example 3:

# Input: nums = [1,2,3,1,4,5,1]

# Output: 5

 

# Constraints:

# 2 <= nums.length <= 100
# 1 <= nums[i] <= 10