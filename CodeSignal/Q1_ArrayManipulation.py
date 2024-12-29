#https://codesignal.com/blog/interview-prep/example-codesignal-questions/

from typing import List

class Solution:
    def arrayMan(self, a: List[int]) -> List[int]:
        b = [0] * len(a)
        for i in range(len(a)):
            b[i] = a[i]
            if i > 0:
                b[i] += a[i - 1]
            if i < len(a) - 1:
                b[i] += a[i + 1]
        return b

sol = Solution()
a  = [4, 0, 1, -2, 3]
nums = [1,2,3,2,2]
print("")
print(f"nums: {a}")
print(f"[4, 5, -1, 2, 1] => {sol.arrayMan(a)}")     
            
    
# Given an array a, your task is to output an array b of the same length by applying the following transformation: 
# – For each i from 0 to a.length - 1 inclusive, b[i] = a[i - 1] + a[i] + a[i + 1]
# – If an element in the sum a[i - 1] + a[i] + a[i + 1] does not exist, use 0 in its place
# – For instance, b[0] = 0 + a[0] + a[1]

# Example

# For a = [4, 0, 1, -2, 3]: 
# – b[0] = 0 + a[0] + a[1] = 0 + 4 + 0 = 4
# – b[1] = a[0] + a[1] + a[2] = 4 + 0 + 1 = 5
# – b[2] = a[1] + a[2] + a[3] = 0 + 1 + (-2) = -1
# – b[3] = a[2] + a[3] + a[4] = 1 + (-2) + 3 = 2
# – b[4] = a[3] + a[4] + 0 = (-2) + 3 + 0 = 1

# So, the output should be solution(a) = [4, 5, -1, 2, 1].