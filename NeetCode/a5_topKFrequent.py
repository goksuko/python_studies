from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = {}
        ordered = [[] for _ in range(len(nums) + 1)]
        res = []
        for n in nums:
            mp[n] = mp.get(n, 0) + 1
        print(mp)
        for key, value in mp.items():
            ordered[value].append(key)
        print(ordered)
        for value in range(len(ordered) - 1, 0, -1):
            print(ordered[value])
            for key in ordered[value]:
                print(key)
                res.append(key)
                if len(res) == k:
                    return res 
       
# 3. Bucket Sort
    def topKFrequent4(self, nums: List[int], k: int) -> List[int]:
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
print(sol.topKFrequent([7, 7], 1))  # Expected output: [7]

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

# Recommended Time & Space Complexity
# You should aim for a solution with O(n) time and O(n) space, where n is the size of the input array.


# Hint 1
# A naive solution would be to count the frequency of each number and then sort the array based on each element’s frequency. After that, we would select the top k frequent elements. This would be an O(nlogn) solution. Though this solution is acceptable, can you think of a better way?


# Hint 2
# Can you think of an algorithm which involves grouping numbers based on their frequency?


# Hint 3
# Use the bucket sort algorithm to create n buckets, grouping numbers based on their frequencies from 1 to n. Then, pick the top k numbers from the buckets, starting from n down to 1.