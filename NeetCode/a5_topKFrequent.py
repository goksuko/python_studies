from typing import List

class Solution:
    
# 3. Bucket Sort
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        print(count)
        for num, cnt in count.items():
            freq[cnt].append(num)
        print(freq)
        
        res = []
        print(len(freq))
        for i in range(len(freq) - 1, 0, -1):
            print(freq[i])
            for num in freq[i]:
                print(f"i: {i}, num: {num}, freq[i]: {freq[i]}")
                res.append(num)
                if len(res) == k:
                    return res
                
# Time complexity: O(n)
# Space complexity: O(n)

# 1. Sorting 
    def topKFrequent2(self, nums: List[int], k: int) -> List[int]:
        map = {}
        for n in nums:
            map[n] = map.get(n, 0) + 1
        
        arr = []
        for n, cnt in map.items():
            arr.append([cnt, n])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
            # print(f"res: {res}")
        return res
    
# Time complexity: O(nlogn)
# Space complexity: O(n)

sol = Solution()
print(sol.topKFrequent([1, 2, 2, 3, 3, 3,4 ,4 ,4 ,4, 5], 2))  # Expected output: [1, 2]
print(sol.topKFrequent([1], 1))  # Expected output: [1]

# Top K Elements in List
# Given an integer array nums and an integer k, return the k most frequent elements within the array.

# The test cases are generated such that the answer is always unique.

# You may return the output in any order.

# Example 1:

# Input: nums = [1,2,2,3,3,3], k = 2

# Output: [2,3]
# Example 2:

# Input: nums = [7,7], k = 1

# Output: [7]
# Constraints:

# 1 <= nums.length <= 10^4.
# -1000 <= nums[i] <= 1000
# 1 <= k <= number of distinct elements in nums.