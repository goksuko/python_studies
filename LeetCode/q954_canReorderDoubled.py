from typing import List
from collections import Counter
import collections

class Solution:
    # O(n) time complexity
    def canReorderDoubled2(self, arr: List[int]) -> bool:
        if sum(arr)%3 != 0: return False
        counter = Counter(arr)
        
        if 0 in counter:
            if counter[0]%2: return False
            counter.pop(0)
            
        while counter:
            num = next(iter(counter))
            while num % 2 == 0 and num//2 in counter: 
                num = num // 2
            while counter[num] > 0 and 2*num in counter:
                counter[2*num] -= counter[num]
                counter.pop(num)
                num = 2*num
            if counter[num] != 0: return False
            counter.pop(num)

        return True
 
# O(nlogn) time complexity
    def canReorderDoubled(self, arr: List[int]) -> bool: # [4, -2, 2, -4]
        count = collections.Counter(arr) # Counter({4: 1, -2: 1, 2: 1, -4: 1})
        for x in sorted(arr, key = abs): # [-2, 2, 4, -4]
            if count[x] == 0: continue 
            if count[2*x] == 0: return False
            count[x] -= 1
            count[2*x] -= 1

        return True

sol = Solution()
arr = [3,1,3,6]
print("")
print(f"nums: {arr}")
print(f"false => {sol.canReorderDoubled(arr)}")   
arr = [2,1,2,6]
print("")
print(f"nums: {arr}")
print(f"false => {sol.canReorderDoubled(arr)}")  
arr = [4,-2,2,-4]
print("")
print(f"nums: {arr}")
print(f"true => {sol.canReorderDoubled(arr)}")  
arr = [-33,0]
print("")
print(f"nums: {arr}")
print(f"false => {sol.canReorderDoubled(arr)}") 
arr = [0,0,0,0,0,0]
print("")
print(f"nums: {arr}")
print(f"true => {sol.canReorderDoubled(arr)}") 

# 954. Array of Doubled Pairs
# Medium

# Given an integer array of even length arr, return true if it is possible to reorder arr such that arr[2 * i + 1] = 2 * arr[2 * i] for every 0 <= i < len(arr) / 2, or false otherwise.

 

# Example 1:

# Input: arr = [3,1,3,6]
# Output: false
# Example 2:

# Input: arr = [2,1,2,6]
# Output: false
# Example 3:

# Input: arr = [4,-2,2,-4]
# Output: true
# Explanation: We can take two groups, [-2,-4] and [2,4] to form [-2,-4,2,4] or [2,4,-2,-4].
 

# Constraints:

# 2 <= arr.length <= 3 * 104
# arr.length is even.
# -105 <= arr[i] <= 105