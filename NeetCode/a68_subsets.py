from typing import List

class Solution:
    def subsets2(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        def dfs(i):
            print(f"***dfs({i}): i: {i}")
            #below is the base case
            if i >= len(nums):
                res.append(subset.copy())
                print(f"res: {res} => subset.copy added: {subset}")
                return
            # decision to include nums[i]
            subset.append(nums[i])
            dfs(i + 1)
            # decision to not include nums[i]
            subset.pop() # to remove what I have added
            dfs(i + 1)

        dfs(0)
        return res
            
#Time complexity: O(n∗2^n)

# 2. Iteration
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        
        for num in nums:
            res += [subset + [num] for subset in res]
            print(f"[num]: {num}, res: {res}")
        
        return res

#Time complexity: O(n∗2^n)

sol = Solution()
print(sol.subsets([1,2,3]))

# 1   ->  [1] #adding 1
#     ->  []  #not adding 1
#         2   ->  [1, 2]  #adding 2
#             ->  [2]     #adding 2
#             ->  [1] 	#not adding 2
#             ->  []      #not adding 2
#                 3   ->  [1, 2, 3]   #adding 3
#                     ->  [2, 3]      #adding 3
#                     ->  [1, 3]      #adding 3 
#                     ->  [3]         #adding 3
#                     ->  [1, 2]      #not adding 3
#                     ->  [2]         #not adding 3
#                     ->  [1]         #not adding 3
#                     ->  []          #not adding 3


# Subsets
# Given an array nums of unique integers, return all possible subsets of nums.

# The solution set must not contain duplicate subsets. You may return the solution in any order.

# Example 1:

# Input: nums = [1,2,3]

# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# Example 2:

# Input: nums = [7]

# Output: [[],[7]]
# Constraints:

# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10


# Recommended Time & Space Complexity
# You should aim for a solution with O(n * (2^n)) time and O(n) space, where n is the size of the input array.


# Hint 1
# It is straightforward that if the array is empty we return an empty array. When we have an array [1] which is of size 1, we have two subsets, [[], [1]] as the output. Can you think why the output is so?


# Hint 2
# We can see that one subset includes a number, and another does not. From this, we can conclude that we need to find the subsets that include a number and those that do not. This results in 2^n subsets for an array of size n because there are many combinations for including and excluding the array of numbers. Since the elements are unique, duplicate subsets will not be formed if we ensure that we don't pick the element more than once in the current subset. Which algorithm is helpful to generate all subsets, and how would you implement it?


# Hint 3
# We can use backtracking to generate all possible subsets. We iterate through the given array with an index i and an initially empty temporary list representing the current subset. We recursively process each index, adding the corresponding element to the current subset and continuing, which results in a subset that includes that element. Alternatively, we skip the element by not adding it to the subset and proceed to the next index, forming a subset without including that element. What can be the base condition to end this recursion?


# Hint 4
# When the index i reaches the end of the array, we append a copy of the subset formed in that particular recursive path to the result list and return. All subsets of the given array are generated from these different recursive paths, which represent various combinations of "include" and "not include" steps for the elements of the array. As we are only iterating from left to right in the array, we don't pick an element more than once.