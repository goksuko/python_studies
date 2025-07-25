
# star

class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        current_string = ""
        current_num = 0
        
        for char in s:
            if char.isdigit():
                # Build the number (could be multi-digit like "12")
                current_num = current_num * 10 + int(char)
                
            elif char == '[':
                # Push current state to stack and reset
                print(f"current_string: {current_string}, current_num: {current_num}")
                stack.append((current_string, current_num))
                print(f"stack: {stack}")
                current_string = ""
                current_num = 0
                
            elif char == ']':
                # Pop from stack and repeat current string
                prev_string, num = stack.pop()
                print(f"prev_string, {prev_string}, num: {num}")
                print(f"stack: {stack}")
                current_string = prev_string + num * current_string
                print(f"current_string: {current_string}")
                
            else:
                # Regular character, add to current string
                current_string += char
                print(f"current_string: {current_string}")
                
        return current_string


sol = Solution()
s = "3[a]2[bc]"  
print(f"s: {s}")                              
print(f"aaabcbc: {sol.decodeString(s)}")    
print("")   
s = "3[a2[bc]]"       
print(f"s: {s}")                              
                         
print(f"abcbcabcbcabcbc: {sol.decodeString(s)}")        
        

# 394. Decode String
# Medium

# Given an encoded string, return its decoded string.

# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

# You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

# The test cases are generated so that the length of the output will never exceed 105.

 

# Example 1:

# Input: s = "3[a]2[bc]"
# Output: "aaabcbc"
# Example 2:

# Input: s = "3[a2[c]]"
# Output: "accaccacc"
# Example 3:

# Input: s = "2[abc]3[cd]ef"
# Output: "abcabccdcdcdef"
 

# Constraints:

# 1 <= s.length <= 30
# s consists of lowercase English letters, digits, and square brackets '[]'.
# s is guaranteed to be a valid input.
# All the integers in s are in the range [1, 300].