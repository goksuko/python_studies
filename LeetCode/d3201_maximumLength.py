class Solution(object):
    def maximumLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # longest evens next to each other
        ev = 0
        # longest odds next to each other
        od = 0
        # longest even odd even / odd even odd sequence
        dual = 0

        if nums[0] % 2 == 0:
            was_odd = False
        else:
            was_odd = True
        for n in nums:
            if n % 2 == 0:
                ev += 1
                if was_odd:
                    dual += 1
                    was_odd = False
            else:
                od += 1
                if not was_odd:
                    dual += 1
                    was_odd = True
        return max(od, max(ev, dual + 1))



# 3201. Find the Maximum Length of Valid Subsequence I
# Medium

# You are given an integer array nums.
# A subsequence sub of nums with length x is called valid if it satisfies:

# (sub[0] + sub[1]) % 2 == (sub[1] + sub[2]) % 2 == ... == (sub[x - 2] + sub[x - 1]) % 2.
# Return the length of the longest valid subsequence of nums.

# A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

 

# Example 1:

# Input: nums = [1,2,3,4]

# Output: 4

# Explanation:

# The longest valid subsequence is [1, 2, 3, 4].

# Example 2:

# Input: nums = [1,2,1,1,2,1,2]

# Output: 6

# Explanation:

# The longest valid subsequence is [1, 2, 1, 2, 1, 2].

# Example 3:

# Input: nums = [1,3]

# Output: 2

# Explanation:

# The longest valid subsequence is [1, 3].

 

# Constraints:

# 2 <= nums.length <= 2 * 105
# 1 <= nums[i] <= 107