from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i + 1]:
                return True
            i += 1

        return False

# Time complexity: O(nlog⁡n)
# Space complexity: O(1) or O(n) depending on the sorting algorithm.    


#my solution
    def hasDuplicate(self, nums: List[int]) -> bool:
        set_n = set(nums)
        return len(nums) != len(set_n)

# 1. **Creating a Set from the List**:
#    - Converting a list to a set in Python involves iterating through the list and adding each element to the set.
#    - The average time complexity for adding an element to a set is O(1), so converting the entire list to a set takes O(n) time, where `n` is the number of elements in the list.

# 2. **Comparing Lengths**:
#    - Calculating the length of a list or a set is an O(1) operation.
#    - Comparing the lengths is also an O(1) operation.

# ### Overall Time Complexity

# - **Creating the Set**: O(n)
# - **Comparing Lengths**: O(1)

# Combining these, the overall time complexity of the function is O(n).

# ### Summary

# - **Time Complexity**: O(n)
# - **Space Complexity**: O(n) (due to the space required to store the set)

# The function efficiently checks for duplicates in the list by converting the list to a set and comparing the lengths of the list and the set. If the lengths are different, it means there are duplicates in the list.

# Duplicate Integer
# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

# Example 1:

# Input: nums = [1, 2, 3, 3]

# Output: true
# Example 2:

# Input: nums = [1, 2, 3, 4]

# Output: false

# Recommended Time & Space Complexity
# You should aim for a solution with O(n) time and O(n) space, where n is the size of the input array.


# Hint 1
# A brute force solution would be to check every element against every other element in the array. This would be an O(n^2) solution. Can you think of a better way?


# Hint 2
# Is there a way to check if an element is a duplicate without comparing it to every other element? Maybe there's a data structure that is useful here.


# Hint 3
# We can use a hash data structure like a hash set or hash map to store elements we've already seen. This will allow us to check if an element is a duplicate in constant time.