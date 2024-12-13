from typing import List
from collections import defaultdict

class Solution: 
    
    # 3. Hash Set
    def longestConsecutive2(self, nums: List[int]) -> int:
        numSet = set(nums) # O(n)
        print(numSet)
        longest = 0 # 1

        for num in numSet: # O(n)
            if (num - 1) not in numSet: # 1
                length = 1
                print(f"num: {num}, length: {length}")
                while (num + length) in numSet: # O(n)
                    length += 1
                longest = max(length, longest)
        return longest
	
    # Time complexity: O(n)
    # Space complexity: O(n)

    # 4. Hash Map
    def longestConsecutive(self, nums: List[int]) -> int:
        mp = defaultdict(int)
        res = 0

        for num in nums:
            if not mp[num]:
                mp[num] = mp[num - 1] + mp[num + 1] + 1
                mp[num - mp[num - 1]] = mp[num]
                mp[num + mp[num + 1]] = mp[num]
                res = max(res, mp[num])
            print(f"num: {num}")
            print(mp)
        return res
    
        # mp = {}
        # res = 0
        
        # for num in nums:
        #     if num not in mp:
        #         left = mp.get(num - 1, 0)
        #         right = mp.get(num + 1, 0)
        #         length = left + right + 1
        #         mp[num] = length
        #         mp[num - left] = length
        #         mp[num + right] = length
        #         res = max(res, length)
        
        # return res

    # Time complexity: O(n)
    # Space complexity: O(n)


# nums = [2,20,4,10,3,4,5]
sol = Solution()
# print(4)
# print(sol.longestConsecutive(nums))
# nums=[0,3,2,5,4,6,1,1]
# print(7)
# print(sol.longestConsecutive(nums))
# nums=[]
# print(0)
# print(sol.longestConsecutive(nums))
nums=[100,4,200,1,3,2]
print(nums)
print(4)
print(sol.longestConsecutive(nums))

# Longest Consecutive Sequence
# Given an array of integers nums, return the length of the longest consecutive sequence of elements.

# A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element.

# You must write an algorithm that runs in O(n) time.

# Example 1:

# Input: nums = [2,20,4,10,3,4,5]

# Output: 4
# Explanation: The longest consecutive sequence is [2, 3, 4, 5].

# Example 2:

# Input: nums = [0,3,2,5,4,6,1,1]

# Output: 7
# Constraints:

# 0 <= nums.length <= 1000
# -10^9 <= nums[i] <= 10^9


# Recommended Time & Space Complexity
# You should aim for a solution as good or better than O(n) time and O(n) space, where n is the size of the input array.


# Hint 1
# A brute force solution would be to consider every element from the array as the start of the sequence and count the length of the sequence formed with that starting element. This would be an O(n^2) solution. Can you think of a better way?


# Hint 2
# Is there any way to identify the start of a sequence? For example, in [1, 2, 3, 10, 11, 12], only 1 and 10 are the beginning of a sequence. Instead of trying to form a sequence for every number, we should only consider numbers like 1 and 10.


# Hint 3
# We can consider a number num as the start of a sequence if and only if num - 1 does not exist in the given array. We iterate through the array and only start building the sequence if it is the start of a sequence. This avoids repeated work. We can use a hash set for O(1) lookups by converting the array to a hash set.