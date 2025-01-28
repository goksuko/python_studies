from typing import List

class Solution(object):
    
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums)==len(set(nums)):
            return False
        
        d = {}

        for i, n in enumerate(nums):
            if n in d and i - d[n] <= k:
                return True
            else:
                d[n] = i
        
        return False

    
    
    def containsNearbyDuplicate2(self, nums, k): #time exceeded
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if k == 0:
            return False
        visited = set()
        for i, n in enumerate(nums):
            if n not in visited:
                start = i
                for j in range(i + 1, len(nums)):
                    if nums[j] == n:
                        if j - start <= k:
                            print(f"n: {n}, start:{start} and j: {j}")
                            return True
                        start = j
            visited.add(n)
        return False
            
sol = Solution()
sol.containsNearbyDuplicate(nums = [1,2,3,1,2,3], k = 2)



# 219. Contains Duplicate II
# Easy

# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

 

# Example 1:

# Input: nums = [1,2,3,1], k = 3
# Output: true
# Example 2:

# Input: nums = [1,0,1,1], k = 1
# Output: true
# Example 3:

# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false
 

# Constraints:

# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109
# 0 <= k <= 105