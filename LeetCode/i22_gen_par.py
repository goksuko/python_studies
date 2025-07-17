from typing import List

class Solution:
    def generateParenthesis(self, n):
        def generate(p, left, right, parens=[]):
            if left:         
                generate(p + '(', left-1, right)
            if right > left:
                generate(p + ')', left, right-1)
            if not right:
                parens += p,
            return parens
        return generate('', n, n)
    
    #my wrong dynamic solution
    def generateParenthesis2(self, n: int) -> List[str]:
        dic = {}
        def helper(dic, n):
            if n == 0:
                dic[n] = [""]
            elif n == 1:
                dic[n] = ["()"]
            elif n in dic:	
                return dic[n]
            else:
                res = []
                for sample in helper(dic, n-1):
                    res.append("(" + sample + ")")
                    res.append("()" + sample)
                    res.append(sample + "()")
                dic[n] = res
            return dic[n]
        return list(set(helper(dic, n)))


sol = Solution()
print(["((()))","(()())","(())()","()(())","()()()"])
print(sol.generateParenthesis(3))
print(["()"])
print(sol.generateParenthesis(1))
print(["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"])
print(sol.generateParenthesis(4))
# print(["((()))","(()())","(())()","()(())","()()()"])
# print(sol.generateParenthesis(3))
# print(["((()))","(()())","(())()","()(())","()()()"])
# print(sol.generateParenthesis(3))

# 22. Generate Parentheses
# Medium

# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

# Example 1:

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:

# Input: n = 1
# Output: ["()"]
 

# Constraints:

# 1 <= n <= 8