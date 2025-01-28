import collections

class Solution(object):
    
    def isValid(self, s): # beats 28 %
        """
        :type s: str
        :rtype: bool
        """
        stk = []
        for char in s:
            if char == '(' or char == '{' or char == '[':
                stk.append(char)
            elif char == ')' and stk and stk[-1] == '(':
                stk.pop()
            elif char == ']' and stk and stk[-1] == '[':
                stk.pop()
            elif char == '}' and stk and stk[-1] == '{':
                stk.pop()
            else:
                return False
        return stk == []
    
    def isValid2(self, s): # beats 68 %
        """
        :type s: str
        :rtype: bool
        """
        par = []
        op = ['(', '{', '[']
        cl = [')', '}', ']']
        dic = {'(': ')', '{': '}', '[':']'}
        for c in s:
            if c in op:
                par.append(c)
            elif c in cl:
                if par == [] or dic[par.pop()] != c:
                    return False
        return par == []
                
            
        


# 20. Valid Parentheses
# Easy

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 
# Example 1:

# Input: s = "()"

# Output: true

# Example 2:

# Input: s = "()[]{}"

# Output: true

# Example 3:

# Input: s = "(]"

# Output: false

# Example 4:

# Input: s = "([])"

# Output: true


# Constraints:

# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.