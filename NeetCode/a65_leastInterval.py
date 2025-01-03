from typing import List
import heapq
from collections import deque
from collections import Counter

# 2. Max-Heap
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        print(f"count: {count}")
        maxHeap = [-cnt for cnt in count.values()]
        print(f"maxHeap: {maxHeap}")
        heapq.heapify(maxHeap)

        time = 0
        q = deque()  # pairs of [-cnt, idleTime]
        while maxHeap or q:
            time += 1

            if not maxHeap:
                time = q[0][1]
            else:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time
    
# Time complexity: O(m)
    
#4. Math
    def leastInterval2(self, tasks: List[str], n: int) -> int:
        count = [0] * 26
        for task in tasks:
            count[ord(task) - ord('A')] += 1
        
        maxf = max(count)
        maxCount = 0
        for let_count in count:
            print(f"let_count: {let_count}")
            maxCount += 1 if let_count == maxf else 0

        time = (maxf - 1) * (n + 1) + maxCount
        return max(len(tasks), time)             
        
# Time complexity: O(m)

# 3. Greedy
    def leastInterval3(self, tasks: List[str], n: int) -> int:
        count = [0] * 26
        for task in tasks:
            count[ord(task) - ord('A')] += 1
        
        count.sort()
        maxf = count[25]
        idle = (maxf - 1) * n

        for i in range(24, -1, -1):
            idle -= min(maxf - 1, count[i])
        return max(0, idle) + len(tasks)      

# Time complexity: O(m)
            
            

sol = Solution()
tasks = ["X","X","Y","Y"]
n = 2
print("")
print(f"tasks: {tasks}, n: {n}")
print(f"5 => {sol.leastInterval(tasks, n)}")
tasks = ["A","A","A","B","C"]
n = 3
print("")
print(f"tasks: {tasks}, n: {n}")
print(f"9 => {sol.leastInterval(tasks, n)}")
tasks=["A","A","A","B","B","B"]
n=2
print("")
print(f"tasks: {tasks}, n: {n}")
print(f"8 => {sol.leastInterval(tasks, n)}")

# Task Scheduler
# You are given an array of CPU tasks tasks, where tasks[i] is an uppercase english character from A to Z. You are also given an integer n.

# Each CPU cycle allows the completion of a single task, and tasks may be completed in any order.

# The only constraint is that identical tasks must be separated by at least n CPU cycles, to cooldown the CPU.

# Return the minimum number of CPU cycles required to complete all tasks.

# Example 1:

# Input: tasks = ["X","X","Y","Y"], n = 2

# Output: 5
# Explanation: A possible sequence is: X -> Y -> idle -> X -> Y.

# Example 2:

# Input: tasks = ["A","A","A","B","C"], n = 3

# Output: 9
# Explanation: A possible sequence is: A -> B -> C -> Idle -> A -> Idle -> Idle -> Idle -> A.

# Constraints:

# 1 <= tasks.length <= 1000
# 0 <= n <= 100


# Recommended Time & Space Complexity
# You should aim for a solution with O(m) time and O(1) space, where m is the size of the input array.


# Hint 1
# There are at most 26 different tasks, represented by A through Z. It is more efficient to count the frequency of each task and store it in a hash map or an array of size 26. Can you think of a way to determine which task should be processed first?


# Hint 2
# We should always process the most frequent task first. After selecting the most frequent task, we must ensure that it is not processed again until after n seconds, due to the cooldown condition. Can you think of an efficient way to select the most frequent task and enforce the cooldown? Perhaps you could use a data structure that allows for O(1) time to retrieve the maximum element and another data structure to cooldown the processed tasks.


# Hint 3
# We can use a Max-Heap to efficiently retrieve the most frequent task at any given instance. However, to enforce the cooldown period, we must temporarily hold off from reinserting the processed task into the heap. This is where a queue data structure comes in handy. It helps maintain the order of processed tasks. Can you implement this?


# Hint 4
# We start by calculating the frequency of each task and initialize a variable time to track the total processing time. The task frequencies are inserted into a Max-Heap. We also use a queue to store tasks along with the time they become available after the cooldown. At each step, if the Max-Heap is empty, we update time to match the next available task in the queue, covering idle time. Otherwise, we process the most frequent task from the heap, decrement its frequency, and if it's still valid, add it back to the queue with its next available time. If the task at the front of the queue becomes available, we pop it and reinsert it into the heap.