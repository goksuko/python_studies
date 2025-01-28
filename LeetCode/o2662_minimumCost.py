
class Solution(object):
    def minimumCost(self, start, target, specialRoads):
        """
        :type start: List[int]
        :type target: List[int]
        :type specialRoads: List[List[int]]
        :rtype: int
        """
        def dist(zero, one,two, three):
            ans = abs(zero - two) + abs(one - three)
            print(f"dist: {ans}")
            return ans
        
        ans = dist(start[0], start[1], target[0], target[1])
        print(f"brute: {ans}")
        for road in specialRoads:
            zero, one,two, three = road[0], road[1], road[2], road[3]
            new = dist(start[0], start[1], zero, one) + road[4] + dist(two, three, target[0], target[1])
            print(f"new: {new}")
            ans = min(ans, new)
            print(f"ans for now: {ans}")
        
        return ans
    
import heapq
def minimumCost(start, target, specialRoads):
    filteredRoads = []
    for road in specialRoads:
        a, b, c, d, cost = road
        if cost < abs(a - c) + abs(b - d):
            filteredRoads.append([a, b, c, d, cost])
    dist = {(start[0], start[1]): 0}
    heap = [(0, start[0], start[1])]
    while heap:
        currdist, x, y = heapq.heappop(heap)
        for road in filteredRoads:
            a, b, c, d, cost = road
            if dist.get((c, d), float('inf')) > currdist + abs(x - a) + abs(y - b) + cost:
                dist[(c, d)] = currdist + abs(x - a) + abs(y - b) + cost
                heapq.heappush(heap, (dist[(c, d)], c, d))
    res = abs(target[0] - start[0]) + abs(target[1] - start[1])
    for road in filteredRoads:
        a, b, c, d, cost = road
        res = min(res, dist.get((c, d), float('inf')) + abs(target[0] - c) + abs(target[1] - d))
    return res    
    
sol = Solution()
sol.minimumCost(start = [1,1], target = [4,5], specialRoads = [[1,2,3,3,2],[3,4,4,5,1]])

# 2662. Minimum Cost of a Path With Special Roads
# Medium

# You are given an array start where start = [startX, startY] represents your initial position (startX, startY) in a 2D space. You are also given the array target where target = [targetX, targetY] represents your target position (targetX, targetY).

# The cost of going from a position (x1, y1) to any other position in the space (x2, y2) is |x2 - x1| + |y2 - y1|.

# There are also some special roads. You are given a 2D array specialRoads where specialRoads[i] = [x1i, y1i, x2i, y2i, costi] indicates that the ith special road goes in one direction from (x1i, y1i) to (x2i, y2i) with a cost equal to costi. You can use each special road any number of times.

# Return the minimum cost required to go from (startX, startY) to (targetX, targetY).

 

# Example 1:

# Input: start = [1,1], target = [4,5], specialRoads = [[1,2,3,3,2],[3,4,4,5,1]]

# Output: 5

# Explanation:

# (1,1) to (1,2) with a cost of |1 - 1| + |2 - 1| = 1.
# (1,2) to (3,3). Use specialRoads[0] with the cost 2.
# (3,3) to (3,4) with a cost of |3 - 3| + |4 - 3| = 1.
# (3,4) to (4,5). Use specialRoads[1] with the cost 1.
# So the total cost is 1 + 2 + 1 + 1 = 5.

# Example 2:

# Input: start = [3,2], target = [5,7], specialRoads = [[5,7,3,2,1],[3,2,3,4,4],[3,3,5,5,5],[3,4,5,6,6]]

# Output: 7

# Explanation:

# It is optimal not to use any special edges and go directly from the starting to the ending position with a cost |5 - 3| + |7 - 2| = 7.

# Note that the specialRoads[0] is directed from (5,7) to (3,2).

# Example 3:

# Input: start = [1,1], target = [10,4], specialRoads = [[4,2,1,1,3],[1,2,7,4,4],[10,3,6,1,2],[6,1,1,2,3]]

# Output: 8

# Explanation:

# (1,1) to (1,2) with a cost of |1 - 1| + |2 - 1| = 1.
# (1,2) to (7,4). Use specialRoads[1] with the cost 4.
# (7,4) to (10,4) with a cost of |10 - 7| + |4 - 4| = 3.
 

# Constraints:

# start.length == target.length == 2
# 1 <= startX <= targetX <= 105
# 1 <= startY <= targetY <= 105
# 1 <= specialRoads.length <= 200
# specialRoads[i].length == 5
# startX <= x1i, x2i <= targetX
# startY <= y1i, y2i <= targetY
# 1 <= costi <= 105