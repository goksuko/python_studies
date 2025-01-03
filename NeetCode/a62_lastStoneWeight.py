from typing import List
import heapq

class Solution:     
        
# 1. Sorting
    def lastStoneWeight3(self, stones: List[int]) -> int:
        
        while len(stones) > 1:
            stones.sort()
            cur = stones.pop() - stones.pop()
            if cur:
                stones.append(cur)
                
        return stones[0] if stones else 0  
    
# Time complexity: O(n^2 logn)
# Space complexity: O(1) or O(n) depending on the sorting algorithm
    
# 2. Binary Search - I did not understand
    def lastStoneWeight2(self, stones: List[int]) -> int:
        stones.sort()
        n = len(stones)

        while n > 1:
            cur = stones.pop() - stones.pop()
            n -= 2
            if cur > 0:
                l, r = 0, n
                while l < r:
                    mid = (l + r) // 2
                    if stones[mid] < cur:
                        l = mid + 1
                    else:
                        r = mid
                pos = l
                n += 1
                stones.append(0)
                for i in range(n - 1, pos, -1):
                    stones[i] = stones[i - 1]
                stones[pos] = cur

        return stones[0] if n > 0 else 0  
    
# Time complexity: O(n^2)
# Space complexity: O(1) or O(n) depending on the sorting algorithm

# 3. Heap
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        print(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second > first:
                heapq.heappush(stones, first - second)
        print(stones)
        stones.append(0)
        print(stones)
        return abs(stones[0])        
    
# Time complexity: O(n logn)
# Space complexity: O(n) 
    
sol = Solution()
stones = [2,3,6,2,4]
print(sol.lastStoneWeight(stones))
stones = [2,3,6,2,4,1]
print(sol.lastStoneWeight(stones))

# Last Stone Weight
# You are given an array of integers stones where stones[i] represents the weight of the ith stone.

# We want to run a simulation on the stones as follows:

# At each step we choose the two heaviest stones, with weight x and y and smash them togethers
# If x == y, both stones are destroyed
# If x < y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
# Continue the simulation until there is no more than one stone remaining.

# Return the weight of the last remaining stone or return 0 if none remain.

# Example 1:

# Input: stones = [2,3,6,2,4]

# Output: 1
# Explanation:
# We smash 6 and 4 and are left with a 2, so the array becomes [2,3,2,2].
# We smash 3 and 2 and are left with a 1, so the array becomes [1,2,2].
# We smash 2 and 2, so the array becomes [1].

# Example 2:

# Input: stones = [1,2]

# Output: 1
# Constraints:

# 1 <= stones.length <= 20
# 1 <= stones[i] <= 100


# Recommended Time & Space Complexity
# You should aim for a solution as good or better than O(nlogn) time and O(n) space, where n is the size of the input array.


# Hint 1
# A naive solution would involve simulating the process by sorting the array at each step and processing the top 2 heaviest stones, resulting in an O(n * nlogn) time complexity. Can you think of a better way? Consider using a data structure that efficiently supports insertion and removal of elements and maintain the sorted order.


# Hint 2
# We can use a Max-Heap, which allows us to retrieve the maximum element in O(1) time. We initially insert all the weights into the Max-Heap, which takes O(logn) time per insertion. We then simulate the process until only one or no element remains in the Max-Heap. At each step, we pop two elements from the Max-Heap which takes O(logn) time. If they are equal, we do not insert anything back into the heap and continue. Otherwise, we insert the difference of the two elements back into the heap.