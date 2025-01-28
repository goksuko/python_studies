from collections import deque

class Solution(object):
    
    
    def maxResult(nums, k):
        dp = [0] * len(nums)
        dp[0] = nums[0]
        q = deque([0])
        
        for i in range(1, len(nums)):
            if q[0] < i - k:
                q.popleft()  # can't reach current index from index stored in q
            dp[i] = nums[i] + dp[q[0]]  # update max score for current index
            while q and dp[q[-1]] <= dp[i]:  # pop indices which won't be ever chosen in the future
                q.pop()
            q.append(i)  # insert current index
        
        return dp[-1]
                
def maxResult(nums, k, i=0):
    if i >= len(nums) - 1:
        return nums[-1]
    
    score = float('-inf')
    for j in range(1, k + 1):
        score = max(score, nums[i] + maxResult(nums, k, i + j))
    
    return score


# 1696. Jump Game VI
# Medium

# You are given a 0-indexed integer array nums and an integer k.

# You are initially standing at index 0. In one move, you can jump at most k steps forward without going outside the boundaries of the array. That is, you can jump from index i to any index in the range [i + 1, min(n - 1, i + k)] inclusive.

# You want to reach the last index of the array (index n - 1). Your score is the sum of all nums[j] for each index j you visited in the array.

# Return the maximum score you can get.

 

# Example 1:

# Input: nums = [1,-1,-2,4,-7,3], k = 2
# Output: 7
# Explanation: You can choose your jumps forming the subsequence [1,-1,4,3] (underlined above). The sum is 7.
# Example 2:

# Input: nums = [10,-5,-2,4,0,3], k = 3
# Output: 17
# Explanation: You can choose your jumps forming the subsequence [10,4,3] (underlined above). The sum is 17.
# Example 3:

# Input: nums = [1,-5,-20,4,-1,3,-6,-3], k = 2
# Output: 0
 

# Constraints:

# 1 <= nums.length, k <= 105
# -104 <= nums[i] <= 104