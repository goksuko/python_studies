class Solution:
    def majorityElement2(self, nums: List[int]) -> List[int]:
        h={}
        l=[]
        n=len(nums)
        for i in nums:
            h[i]=h.get(i,0)+1
        for j in h:
            if h[j]>n//3:
               l.append(j)
        return l 
    
	#below from copilot
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
        # Step 1: Find potential candidates
        candidate1, candidate2, count1, count2 = None, None, 0, 0
        
        for num in nums:
            if candidate1 == num:
                count1 += 1
            elif candidate2 == num:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = num, 1
            elif count2 == 0:
                candidate2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1
        
        # Step 2: Verify the candidates
        count1, count2 = 0, 0
        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
        
        result = []
        n = len(nums)
        if count1 > n // 3:
            result.append(candidate1)
        if count2 > n // 3:
            result.append(candidate2)
        
        return result
        




# 229. Majority Element II
# Medium

# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

 

# Example 1:

# Input: nums = [3,2,3]
# Output: [3]
# Example 2:

# Input: nums = [1]
# Output: [1]
# Example 3:

# Input: nums = [1,2]
# Output: [1,2]
 

# Constraints:

# 1 <= nums.length <= 5 * 104
# -109 <= nums[i] <= 109