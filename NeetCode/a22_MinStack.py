from typing import List

# below cannot give min right if sth is popped
class MinStack3:

	def __init__(self):
		self.stack = []
		self.min = float('inf')

	def push(self, val: int) -> None:
		self.stack.append(int(val))
		if self.min == float('inf'):
			self.min = val
		else:
			self.min = min(self.min, val)   

	def pop(self) -> None:
		self.stack.pop()        

	def top(self) -> int:
		return self.stack[-1]
		
	def getMin(self) -> int:
		return self.min

# Two Stacks
class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)
        print(f"self.stack {self.stack}")
        print(f"self.minStack {self.minStack}")
        
    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
		
# One stack
class MinStack2:
    def __init__(self):
        self.min = float('inf')
        self.stack = []

    def push(self, x: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.min = x
        else:
            self.stack.append(x - self.min)
            if x < self.min:
                self.min = x

    def pop(self) -> None:
        if not self.stack:
            return
        
        pop = self.stack.pop()
        
        if pop < 0:
            self.min = self.min - pop

    def top(self) -> int:
        top = self.stack[-1]
        if top > 0:
            return top + self.min
        else:
            return self.min

    def getMin(self) -> int:
        return self.min

# Time complexity: O(1) for all operations.
# Space complexity: O(n)


		
# Input: ["MinStack", "push", 1, "push", 2, "push", 0, "getMin", "pop", "top", "getMin"]

# Output: [null,null,null,null,0,null,2,1]

# Explanation:
minStack = MinStack()
minStack.push(1)
minStack.push(2)
minStack.push(0)
print(minStack.stack)
print(minStack.getMin()) # return 0
minStack.pop()
print(minStack.stack)
print(minStack.top())   # return 2
print(minStack.getMin()) # return 1
minStack.push(1)
minStack.push(-2)
minStack.push(0)
print(minStack.top())   # return 0
print(minStack.getMin()) # return -2
print(minStack.stack)
minStack.pop()
minStack.pop()
minStack.push(0)
print(minStack.stack)
print(minStack.getMin()) # return 0





# Minimum Stack
# Design a stack class that supports the push, pop, top, and getMin operations.

# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
# Each function should run in 
# O
# (
# 1
# )
# O(1) time.

# Example 1:

# Input: ["MinStack", "push", 1, "push", 2, "push", 0, "getMin", "pop", "top", "getMin"]

# Output: [null,null,null,null,0,null,2,1]

# Explanation:
# MinStack minStack = new MinStack();
# minStack.push(1);
# minStack.push(2);
# minStack.push(0);
# minStack.getMin(); // return 0
# minStack.pop();
# minStack.top();    // return 2
# minStack.getMin(); // return 1
# Constraints:

# -2^31 <= val <= 2^31 - 1.
# pop, top and getMin will always be called on non-empty stacks.


# Recommended Time & Space Complexity
# You should aim for a solution with O(1) time for each function call and O(n) space, where n is the maximum number of elements present in the stack.


# Hint 1
# A brute force solution would be to always check for the minimum element in the stack for the getMin() function call. This would be an O(n) appraoch. Can you think of a better way? Maybe O(n) extra space to store some information.


# Hint 2
# We can use a stack to maintain the elements. But how can we find the minimum element at any given time? Perhaps we should consider a prefix approach.


# Hint 3
# We use an additional stack to maintain the prefix minimum element. When popping elements from the main stack, we should also pop from this extra stack. However, when pushing onto the extra stack, we should push the minimum of the top element of the extra stack and the current element onto this extra stack.