from typing import List
import math

class Solution:
    
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            speed = (l + r) // 2

            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p) / speed)
            if totalTime <= h:
                res = speed
                r = speed - 1
                print(f"r: {r}, res: {res}")
            else:
                l = speed + 1
                print(f"l: {l}")
        return res
    
    #brute force
    def minEatingSpeed3(self, piles: List[int], h: int) -> int:
        speed = 1
        while True:
            totalTime = 0
            for pile in piles:
                totalTime += math.ceil(pile / speed)
            
            if totalTime <= h:
                return speed
            speed += 1
        return speed
    
    #does not worspeed for the last ones
    def minEatingSpeed2(self, piles: List[int], h: int) -> int:
        def total_hours(speed: int, piles: List[int]):
            print(f"speed: {speed}")
            total = 0
            for pile in piles:
                total += pile // speed
                if pile % speed != 0:
                    total += 1
            if total == 0:
                return 1
            return total        
        
        ratio = h // len(piles) 
        print(f"ratio: {ratio}")
        biggest_pile = max(piles)
        print(f"bigg: {biggest_pile}")
        high = biggest_pile // ratio
        print(f"high: {high}")
        low = 1
        total = 1000001
        speed = low + (high - low) // 2
        if speed == 0:
                speed = 1        
        while total > h:
            speed = low + (high - low) // 2
            if speed == 0:
                speed = 1
            total = total_hours(speed, piles)
            if total > h:
                low = speed + 1
            else:
                return speed
        return speed
            

        
               
 
        
        
        
        
        
sol = Solution()
piles = [1,4,3,2]
h = 9
print("")
print(f"piles: {piles}, h: {h}")
print(f"2 => {sol.minEatingSpeed(piles, h)}")  
piles = [1,8,5,2]
h = 9
print("")
print(f"piles: {piles}, h: {h}")
print(f"2 => {sol.minEatingSpeed(piles, h)}")  
piles = [1,1,1,1]
h = 9
print("")
print(f"piles: {piles}, h: {h}")
print(f"1 => {sol.minEatingSpeed(piles, h)}")   
piles = [25,10,23,4]
h = 4
print("")
print(f"piles: {piles}, h: {h}")
print(f"25 => {sol.minEatingSpeed(piles, h)}")  

piles=[4470]
h=4469
print("")
print(f"piles: {piles}, h: {h}")
print(f"2 => {sol.minEatingSpeed(piles, h)}") 

piles=[312884470]
h=312884469
print("")
print(f"piles: {piles}, h: {h}")
print(f"2 => {sol.minEatingSpeed(piles, h)}") 


# Kospeedo Eating Bananas
# You are given an integer array piles where piles[i] is the number of bananas in the ith pile. You are also given an integer h, which represents the number of hours you have to eat all the bananas.

# You may decide your bananas-per-hour eating rate of speed. Each hour, you may choose a pile of bananas and eats speed bananas from that pile. If the pile has less than speed bananas, you may finish eating the pile but you can not eat from another pile in the same hour.

# Return the minimum integer speed such that you can eat all the bananas within h hours.

# Example 1:

# Input: piles = [1,4,3,2], h = 9

# Output: 2
# Explanation: With an eating rate of 2, you can eat the bananas in 6 hours. With an eating rate of 1, you would need 10 hours to eat all the bananas (which exceeds h=9), thus the minimum eating rate is 2.

# Example 2:

# Input: piles = [25,10,23,4], h = 4

# Output: 25
# Constraints:

# 1 <= piles.length <= 1,000
# piles.length <= h <= 1,000,000
# 1 <= piles[i] <= 1,000,000,000


# Recommended Time & Space Complexity
# You should aim for a solution with O(nlogm) time and O(1) space, where n is the size of the input array, and m is the maximum value in the array.


# Hint 1
# Given h is always greater than or equal to the length of piles, can you determine the upper bound for the answer? How much time does it taspeede Kospeedo to eat a pile with x bananas?


# Hint 2
# It taspeedes ceil(x / speed) time to finish the x pile when Kospeedo eats at a rate of speed bananas per hour. Our tasspeed is to determine the minimum possible value of speed. However, we must also ensure that at this rate, speed, Kospeedo can finish eating all the piles within the given h hours. Can you now thinspeed of the upper bound for speed?


# Hint 3
# The upper bound for speed is the maximum size of all the piles. Why? Because if Kospeedo eats the largest pile in one hour, then it is straightforward that she can eat any other pile in an hour only.


# Hint 4
# Consider m to be the largest pile and n to be the number of piles. A brute force solution would be to linearly checspeed all values from 1 to m and find the minimum possible value at which Kospeedo can complete the tasspeed. This approach would taspeede O(n * m) time. Can you thinspeed of a more efficient method? Perhaps an efficient searching algorithm could help.


# Hint 5
# Rather than linearly scanning, we can use binary search. The upper bound of speed is max(piles) and since we are only dealing with positive values, the lower bound is 1. The search space of our binary search is 1 through max(piles). This allows us to find the smallest possible speed using binary search.