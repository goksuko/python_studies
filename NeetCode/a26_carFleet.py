from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #check the total time to be elapsed for each car
        #find longer times when they are listed according to their starting positions
        #pos: 0 and time: 4
        #pos: 2 and time: 5 => every car behind (having small positions) with longer time may create a fleet together

        d = []
        for i in range(len(position)):
            d.append((position[i], (target - position[i]) / speed[i]))
        print(d)
        fleet = 1
        d.sort(key = lambda x: x[0])
        print(d)
        min_time = d[-1][1]
        print(min_time)
        for i in range(len(position)-1, -1, -1):
            if d[i][1] > min_time:
                fleet += 1
                min_time = d[i][1]
                print(min_time)
        return(fleet)
            
   
sol = Solution()
# target = 10
# position = [1,4]
# speed = [3,2]
# print("target = 10\nposition = [1,4]\nspeed = [3,2]")
# print(f"1 => {sol.carFleet(target, position, speed)}")
target = 10
position = [4,1,0,7]
speed = [2,2,1,1]
print("target = 10\nposition = [4,1,0,7]\nspeed = [2,2,1,1]")
print(f"3 => {sol.carFleet(target, position, speed)}")
# target = 10
# position = [4,1,0,7,5]
# speed = [2,2,1,1,3]
# print(f"3 => {sol.carFleet(target, position, speed)}")        



# Car Fleet
# There are n cars traveling to the same destination on a one-lane highway.

# You are given two arrays of integers position and speed, both of length n.

# position[i] is the position of the ith car (in miles)
# speed[i] is the speed of the ith car (in miles per hour)
# The destination is at position target miles.

# A car can not pass another car ahead of it. It can only catch up to another car and then drive at the same speed as the car ahead of it.

# A car fleet is a non-empty set of cars driving at the same position and same speed. A single car is also considered a car fleet.

# If a car catches up to a car fleet the moment the fleet reaches the destination, then the car is considered to be part of the fleet.

# Return the number of different car fleets that will arrive at the destination.

# Example 1:

# Input: target = 10, position = [1,4], speed = [3,2]

# Output: 1
# Explanation: The cars starting at 1 (speed 3) and 4 (speed 2) become a fleet, meeting each other at 10, the destination.

# Example 2:

# Input: target = 10, position = [4,1,0,7], speed = [2,2,1,1]

# Output: 3
# Explanation: The cars starting at 4 and 7 become a fleet at position 10. The cars starting at 1 and 0 never catch up to the car ahead of them. Thus, there are 3 car fleets that will arrive at the destination.

# Constraints:

# n == position.length == speed.length.
# 1 <= n <= 1000
# 0 < target <= 1000
# 0 < speed[i] <= 100
# 0 <= position[i] < target
# All the values of position are unique.


# Recommended Time & Space Complexity
# You should aim for a solution with O(nlogn) time and O(n) space, where n is the size of the input array.


# Hint 1
# First draw a picture of all the points which represents the positions and respective speeds of the cars. It is appropriate to represent the position and speed of each car as an array, where each cell corresponds to a car. It is also logical to sort this array based on the positions in descending order. Why?


# Hint 2
# Because a car can only form a fleet with another car that is ahead of it, sorting the array in descending order ensures clarity about the final speed of each car. Sorting in ascending order would create ambiguity, as the next car might form a fleet with another car while reaching the target, making it difficult to determine its final speed.


# Hint 3
# Calculating the time for a car to reach the target is straightforward and can be done using the formula: time = (target - position) / speed. Now, it becomes easy to identify that two cars will form a fleet if and only if the car ahead has a time that is greater than or equal to the time of the car behind it. How can we maintain the total number of fleets happened while going through the array? Maybe a data structure is helpful.


# Hint 4
# We can use a stack to maintain the times of the fleets. As we iterate through the array (sorted in descending order of positions), we compute the time for each car to reach the target and check if it can form a fleet with the car ahead. If the current car's time is less than or equal to the top of the stack, it joins the same fleet. Otherwise, it forms a new fleet, and we push its time onto the stack. The length of the stack at the end represents the total number of fleets formed.