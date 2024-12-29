from typing import List
import math

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        # total = m + n
        # m_l, m_r = 0, m - 1
        # n_l, n_r = 0, n - 1
        # if n > m:
        #     short = m
        # else:
        #     short = n
        med1 = nums1[math.ceil(m // 2)]
        med2 = nums2[math.ceil(n // 2)]
        return (m * med1 + n * med2) / (m + n)
    
sol = Solution()
nums1 = [1,2]
nums2 = [3]
print("")
print(f"nums1: {nums1}, nums2: {nums2}")
print(f"2.0 => {sol.findMedianSortedArrays(nums1, nums2)}")          
nums1 = [1,3]
nums2 = [2,4]
print("")
print(f"nums1: {nums1}, nums2: {nums2}")
print(f"2.5 => {sol.findMedianSortedArrays(nums1, nums2)}")   



# Median of Two Sorted Arrays
# You are given two integer arrays nums1 and nums2 of size m and n respectively, where each is sorted in ascending order. Return the median value among all elements of the two arrays.

# Your solution must run in O(log(m+n)) time.

# Example 1:

# Input: nums1 = [1,2], nums2 = [3]

# Output: 2.0
# Explanation: Among [1, 2, 3] the median is 2.

# Example 2:

# Input: nums1 = [1,3], nums2 = [2,4]

# Output: 2.5
# Explanation: Among [1, 2, 3, 4] the median is (2 + 3) / 2 = 2.5.

# Constraints:

# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# -10^6 <= nums1[i], nums2[i] <= 10^6


# Recommended Time & Space Complexity
# You should aim for a solution with O(log(min(n, m))) time and O(1) space, where n is the size of nums1 and m is the size of nums2.


# Hint 1
# A brute force solution would be to create a new array by merging elements from both arrays, then sorting it and returning the median. This would be an O(n + m) solution. Can you think of a better way? Maybe you can use the criteria of both the arrays being sorted in ascending order.


# Hint 2
# Suppose we merged both arrays. Then, we would have half = (m + n) / 2 elements to the left of the median. So, without merging, is there any way to use this information to find the median? You can leverage the fact that the arrays are sorted. Consider the smaller array between the two and use binary search to find the correct partition between the two arrays, which will allow you to directly find the median without fully merging the arrays. How will you implement this?


# Hint 3
# We will always try to keep array A smaller and interchange it with array B if len(A) > len(B). Now, we perform binary search on the number of elements we will choose from array A. It is straightforward that when we choose x elements from array A, we have to choose half - x elements from array B. But we should also ensure that this partition is valid. How can we do this?


# Hint 4
# When we do a partition for both arrays, we should ensure that the maximum elements from the left partitions of both arrays are smaller than or equal to the minimum elements of the right partitions of both the arrays. This will ensure that the partition is valid, and we can then find the median. We can find the min or max of these partitions in O(1) as these partitions are sorted in ascending order. Why does this work?


# Hint 5
# For example, consider the arrays A = [1, 2, 3, 4, 5] and B = [1, 2, 3, 4, 5, 6, 7, 8]. When we select x = 2, we take 4 elements from array B. However, this partition is not valid because value 4 from the left partition of array B is greater than the value 3 from the right partition of array A. So, we should try to take more elements from array A to make the partition valid. Binary search will eventually help us find a valid partition.