from typing import List

class Solution:
    #beats 100
    def mostFrequentEven(self, nums: List[int]) -> int:
        d ={}
        for i in nums:
            if i%2==0:
                d[i] = d.get(i,0)+1
        
        if d=={}:
            return -1
        x= max(d.values())
        mn = float('inf')
        for k,v in d.items():
            if v==x:
                mn = min(k,mn)
        return mn


# my solution Beats 35.71%
    def mostFrequentEven2(self, nums: List[int]) -> int:
        mp = {}
        for n in nums:
            mp[n] = mp.get(n, 0) + 1
        ans = 1000000
        most_seen = 0
        for key, value in mp.items():
            print(f"key: {key}, value: {value}")
            if value > most_seen:
                if key % 2 == 0:
                    ans = key
                    most_seen = value
            if value == most_seen:
                if key % 2 == 0:
                    ans = min(key, ans)
        if ans == 1000000:
            return -1
        return ans

sol = Solution()
print(sol.mostFrequentEven([0,1,2,2,4,4,1])) # 2

# 2404. Most Frequent Even Element
# Easy

# Given an integer array nums, return the most frequent even element.

# If there is a tie, return the smallest one. If there is no such element, return -1.

 

# Example 1:

# Input: nums = [0,1,2,2,4,4,1]
# Output: 2
# Explanation:
# The even elements are 0, 2, and 4. Of these, 2 and 4 appear the most.
# We return the smallest one, which is 2.
# Example 2:

# Input: nums = [4,4,4,9,2,4]
# Output: 4
# Explanation: 4 is the even element appears the most.
# Example 3:

# Input: nums = [29,47,21,41,13,37,25,7]
# Output: -1
# Explanation: There is no even element.
 

# Constraints:

# 1 <= nums.length <= 2000
# 0 <= nums[i] <= 105
