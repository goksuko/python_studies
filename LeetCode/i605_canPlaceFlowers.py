class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return True
        i = 0
        flowerbed.append(0)
        flowerbed.insert(0, 0)
        while i < len(flowerbed) and n > 0:
            while i < len(flowerbed) and flowerbed[i] == 1:
                i += 1
            temp = 0
            while i < len(flowerbed) and flowerbed[i] == 0:
                i += 1
                temp += 1
            if temp:
                n -= (temp - 1) // 2
            if n <= 0:
                return True
        return False

sol = Solution()
flowerbed = [1,0,0,0,1]
n = 1
print(f"True => {sol.canPlaceFlowers(flowerbed, n)}")
flowerbed = [1,0,0,0,1]
n = 2
print(f"False => {sol.canPlaceFlowers(flowerbed, n)}")
flowerbed = [0,0,1,0,0]
n = 1
print(f"True => {sol.canPlaceFlowers(flowerbed, n)}")
flowerbed = [0,0,1,0,0]
n = 2
print(f"True => {sol.canPlaceFlowers(flowerbed, n)}")
flowerbed = [1,0,0,0,0,1]
n = 2
print(f"False => {sol.canPlaceFlowers(flowerbed, n)}")
             
            
            
                


# 605. Can Place Flowers
# Easy

# You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

 

# Example 1:

# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: true
# Example 2:

# Input: flowerbed = [1,0,0,0,1], n = 2
# Output: false
 

# Constraints:

# 1 <= flowerbed.length <= 2 * 104
# flowerbed[i] is 0 or 1.
# There are no two adjacent flowers in flowerbed.
# 0 <= n <= flowerbed.length