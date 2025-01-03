from typing import List
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for x, y in points:
            dist = (x ** 2) + (y ** 2)
            minHeap.append([dist, x, y])
        
        heapq.heapify(minHeap)
        res = []
        while k > 0:
            dist, x, y = heapq.heappop(minHeap)
            res.append([x, y])
            k -= 1
            
        return res 
    
    
    
    #did not work at the last case
    def kClosest2(self, points: List[List[int]], k: int) -> List[List[int]]:
        d = []
        for point in points:
            d.append([abs(point[0]) * abs(point[0]) + abs(point[1]) * abs(point[1]), point[0], point[1]]) #O(n)
        heapq.heapify(d) #O(n)
        n = len(d)
        for i in range(n - k - 1):
            heapq.heappop(d) # O((n-k)*log(n))
        ans = []
        old = heapq.heappop(d) # O(log(n))
        ans.append([old[1], old[2]])
        for i in range(k - 1):
            new = heapq.heappop(d) # O(k*log(n))
            if new[0] == old[0]:
               ans.append([new[1], new[2]])
            elif i == 0:
                break
        return ans
    
# Time: O(n*log(n))
            
sol = Solution()
points = [[0,2],[2,2]]
k = 1
print("")
print(f"points: {points}, k: {k}")
print(f"[[0,2]] => {sol.kClosest(points, k)}")
points = [[0,2],[2,0],[2,2]]
k = 2
print("")
print(f"points: {points}, k: {k}")
print(f"[[0,2],[2,0]] => {sol.kClosest(points, k)}")
points = [[3,3],[5,-1],[-2,4]]
k=2
print("")
print(f"points: {points}, k: {k}")
print(f"[[3,3],[-2,4]] => {sol.kClosest(points, k)}")


# K Closest Points to Origin
# You are given an 2-D array points where points[i] = [xi, yi] represents the coordinates of a point on an X-Y axis plane. You are also given an integer k.

# Return the k closest points to the origin (0, 0).

# The distance between two points is defined as the Euclidean distance (sqrt((x1 - x2)^2 + (y1 - y2)^2)).

# You may return the answer in any order.

# Example 1:

# Input: points = [[0,2],[2,2]], k = 1

# Output: [[0,2]]
# Explanation : The distance between (0, 2) and the origin (0, 0) is 2. The distance between (2, 2) and the origin is sqrt(2^2 + 2^2) = 2.82842. So the closest point to the origin is (0, 2).

# Example 2:

# Input: points = [[0,2],[2,0],[2,2]], k = 2

# Output: [[0,2],[2,0]]
# Explanation: The output [2,0],[0,2] would also be accepted.

# Constraints:

# 1 <= k <= points.length <= 1000
# -100 <= points[i][0], points[i][1] <= 100


# Recommended Time & Space Complexity
# You should aim for a solution as good or better than O(nlogk) time and O(k) space, where n is the size of the input array, and k is the number of points to be returned.


# Hint 1
# A naive solution would be to sort the array in ascending order based on the distances of the points from the origin (0, 0) and return the first k points. This would take O(nlogn) time. Can you think of a better way? Perhaps you could use a data structure that maintains only k points and allows efficient insertion and removal.


# Hint 2
# We can use a Max-Heap that keeps the maximum element at its top and allows retrieval in O(1) time. This data structure is ideal because we need to return the k closest points to the origin. By maintaining only k points in the heap, we can efficiently remove the farthest point when the size exceeds k. How would you implement this?


# Hint 3
# We initialize a Max-Heap that orders points based on their distances from the origin. Starting with an empty heap, we iterate through the array of points, inserting each point into the heap. If the size of the heap exceeds k, we remove the farthest point (the maximum element in the heap). After completing the iteration, the heap will contain the k closest points to the origin. Finally, we convert the heap into an array and return it.