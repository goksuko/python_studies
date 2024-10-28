#stack will be better I think



class Solution:
    def minInsertions(self, s: str) -> int:
        missing = 0
        open = 0
        i = 0
        while i <= len(s)-1:
            if s[i] == '(':
                open += 1
            else:
                j = i
                while j+1 < len(s) and s[j+1] == ')':
                    j += 1
                total = j-i+1 # total num of adjacent )

                fullClosed = total//2 # num of ))
                halfClosed = total%2 # 1 if there are any left of ), 0 otherwise

                for i in range(fullClosed):
                    # for every full closed
                    if open:
                        # if we have any ( towards left, decrement open count as they are matched now
                        open -= 1
                    else:
                        # if there are no ( towards left, then we for sure need '(' to be added, so consider this as missing
                        missing += 1
                
                if halfClosed:
                    # for half closed
                    if open:
                        # if we have an ( towards left, then we need to insert ')' at this position to make full closed and balanced
                        # so consider this as missing, and decrement open as we balanced it
                        missing += 1
                        open -= 1
                    else:
                        # if there are no ( towards left, then to balance this ')' we need a '(' and also ')'
                        # so add 2 to missing count
                        missing += 2
                i = j
            i += 1
        
        # for all left over ( we need 2 ) to be inserted
        return missing + open*2
    
sol = Solution()
print("1:", sol.minInsertions("(()))"))
print("3:", sol.minInsertions("))())("))
print("5:", sol.minInsertions(")))))))"))
print("4:", sol.minInsertions("(()))(()))()())))"))
# print(sol.minInsertions())


# 1541. Minimum Insertions to Balance a Parentheses String
# Medium

# Hint
# Given a parentheses string s containing only the characters '(' and ')'. A parentheses string is balanced if:

# Any left parenthesis '(' must have a corresponding two consecutive right parenthesis '))'.
# Left parenthesis '(' must go before the corresponding two consecutive right parenthesis '))'.
# In other words, we treat '(' as an opening parenthesis and '))' as a closing parenthesis.

# For example, "())", "())(())))" and "(())())))" are balanced, ")()", "()))" and "(()))" are not balanced.
# You can insert the characters '(' and ')' at any position of the string to balance it if needed.

# Return the minimum number of insertions needed to make s balanced.

# Example 1:

# Input: s = "(()))"
# Output: 1
# Explanation: The second '(' has two matching '))', but the first '(' has only ')' matching. We need to add one more ')' at the end of the string to be "(())))" which is balanced.
# Example 2:

# Input: s = "())"
# Output: 0
# Explanation: The string is already balanced.
# Example 3:

# Input: s = "))())("
# Output: 3
# Explanation: Add '(' to match the first '))', Add '))' to match the last '('.


# Constraints:

# 1 <= s.length <= 105
# s consists of '(' and ')' only.