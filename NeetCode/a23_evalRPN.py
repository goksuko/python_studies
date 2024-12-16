from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == '+':
                result = 0
                result += stack.pop()
                result += stack.pop()
                stack.append(result)
            elif c == '-':
                result = 0
                result -= stack.pop()
                result += stack.pop()
                stack.append(result)
            elif c == '*':
                result = 1
                result *= stack.pop()
                result *= stack.pop()
                stack.append(result)
            elif c == '/':
                result = 1
                to_divide = stack.pop()       
                result = int(stack.pop() / to_divide)
                stack.append(result)
            else:
                stack.append(int(c))
            print(stack)    

        return stack[0]
    
    
# recursion

class Solution:
    def evalRPN2(self, tokens: List[str]) -> int:
        def dfs():
            token = tokens.pop()
            if token not in "+-*/":
                return int(token)
            
            right = dfs()
            left = dfs()
            
            if token == '+':
                return left + right
            elif token == '-':
                return left - right
            elif token == '*':
                return left * right
            elif token == '/':
                return int(left / right)
        
        return dfs()
    
    
sol = Solution()
tokens = ["1","2","+","3","*","4","-"]
print(sol.evalRPN(tokens))
tokens = ["4","13","5","/","+"]
print(sol.evalRPN(tokens))
tokens=["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(sol.evalRPN(tokens))
  
                
                



# Evaluate Reverse Polish Notation
# You are given an array of strings tokens that represents a valid arithmetic expression in Reverse Polish Notation.

# Return the integer that represents the evaluation of the expression.

# The operands may be integers or the results of other operations.
# The operators include '+', '-', '*', and '/'.
# Assume that division between integers always truncates toward zero.
# Example 1:

# Input: tokens = ["1","2","+","3","*","4","-"]

# Output: 5

# Explanation: ((1 + 2) * 3) - 4 = 5
# Constraints:

# 1 <= tokens.length <= 1000.
# tokens[i] is "+", "-", "*", or "/", or a string representing an integer in the range [-100, 100].


# Recommended Time & Space Complexity
# You should aim for a solution with O(n) time and O(n) space, where n is the size of the input array.


# Hint 1
# A brute force solution would involve repeatedly finding an operator + - * / in the array and modifying the array by computing the result for that operator and two operands to its left. This would be an O(n^2) solution. Can you think of a better way? Maybe we can use a data structure to handle operations efficiently.


# Hint 2
# We can use a stack. We iterate through the array, and if we encounter a number, we push it onto the stack. If we encounter an operator, we pop two elements from the stack, treat them as operands, and solve the equation using the current operator. Then, we push the result back onto the stack. Why does this work?


# Hint 3
# As the array has postfix expression, stack helps us to maintain the correct order of operations by ensuring that we always use the most recent operands (those closest to the operator) when performing the operation. After the iteration, the final result is left in the stack.