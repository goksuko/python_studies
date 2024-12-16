from typing import List

class Solution:
#dynamic programming
    def dailyTemperatures3(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n

        for i in range(n - 2, -1, -1):
            j = i + 1
            print(f"\ni: {i}, j: {j}")
            print(f"temperatures[i]: {temperatures[i]}, temperatures[j]: {temperatures[j]}")
            while j < n and temperatures[j] <= temperatures[i]:
                print("in while")
                if res[j] == 0:
                    j = n
                    print("res[j] == 0, j = n, break")
                    break
                j += res[j]
                print("j += res[j]")
                print(f"j: {j}, res[j]: {res[j]}")
            
            if j < n:
                res[i] = j - i
                print("res[i] = j - i")
                print(f"j: {j}, res[i]: {res[i]}")

        return res

# Time Complexity: O(n)
# Space Complexity: O(n)   

#stack
    def dailyTemperatures2(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []  # pair: [temp, index]

        for i, t in enumerate(temperatures):
            print(f"\ni: {i}, t: {t}")
            while stack and t > stack[-1][0]:
                print("in while")
                print(f"t({t}) > stack[-1][0]({stack[-1][0]})")
                stackT, stackInd = stack.pop()
                print(f"stackInd: {stackInd}")
                res[stackInd] = i - stackInd
                print(f"res[stackInd]: {res[stackInd]} = i({i}) - stackInd({stackInd})")
            stack.append((t, i))
            print(f"stack: {stack}")
        return res

# Time Complexity: O(n)
# Space Complexity: O(n)          
            
#brute force
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        for i in range(len(temperatures)):
            for j in range(i + 1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    result.append(j-i)
                    break
                elif j == len(temperatures) - 1:
                    result.append(0)
        result.append(0)
        return result
            
	
sol = Solution()
temperatures = [30,38,30,36,35,40,28]
print(f"Input: {temperatures}")
print(sol.dailyTemperatures2(temperatures))
# Output: [1,4,1,2,1,0,0]            
temperatures = [30,38,30,30,36,35,34,33,40,41,42,28]
print(f"Input: {temperatures}")
print(sol.dailyTemperatures2(temperatures))
            
            
            
            


# Daily Temperatures
# You are given an array of integers temperatures where temperatures[i] represents the daily temperatures on the ith day.

# Return an array result where result[i] is the number of days after the ith day before a warmer temperature appears on a future day. If there is no day in the future where a warmer temperature will appear for the ith day, set result[i] to 0 instead.

# Example 1:

# Input: temperatures = [30,38,30,36,35,40,28]

# Output: [1,4,1,2,1,0,0]
# Example 2:

# Input: temperatures = [22,21,20]

# Output: [0,0,0]
# Constraints:

# 1 <= temperatures.length <= 1000.
# 1 <= temperatures[i] <= 100


# Recommended Time & Space Complexity
# You should aim for a solution as good or better than O(n) time and O(n) space, where n is the size of the input array.


# Hint 1
# A brute force solution would involve iterating through the array with index i and checking how far is the next greater element to the right of i. This would be an O(n^2) solution. Can you think of a better way?


# Hint 2
# Can you consider a reverse approach? For example, in [2, 1, 1, 3], the next greater element for the numbers [2, 1, 1] is 3. Instead of checking for each element individually, can you think of a way where, by standing at the element 3, you compute the result for the elements [2, 1, 1]? Maybe there's a data structure that is useful here.


# Hint 3
# We can use a stack to maintain indices in a monotonically decreasing order, popping indices where the values are smaller than the current element. This helps us find the result by using the difference between indices while considering the values at those indices. Can you see how the stack is useful?


# Hint 4
# In the array [2, 1, 1, 3], we don't perform any pop operations while processing [2, 1, 1] because these elements are already in decreasing order. However, when we reach 3, we pop elements from the stack until the top element of the stack is no longer less than the current element. For each popped element, we compute the difference between the indices and store it in the position corresponding to the popped element.

