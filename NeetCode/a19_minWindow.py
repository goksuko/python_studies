from typing import List

# TEMPLATE AND OTHER EXAMPLES BELOW!!!

class Solution:
    
    def minWindow(self, s: str, t: str) -> str:
        # s: long string
        # t: to look for
        
        map = [0] * 128
        for c in t:
            map[ord(c)] += 1

        counter = len(t)
        begin = 0
        head = 0 
        end = 0
        d = float('inf') 

        while end < len(s):
            print(f"s[{end}]: {s[end]}, begin: {begin}, head: {head}, end: {end}, d: {d}, counter: {counter}")
            if map[ord(s[end])] > 0:
                counter -= 1
                print(f"if map_end:{s[end]} > 0, counter -= 1")
            map[ord(s[end])] -= 1
            print(f"map_end:{s[end]} -= 1")
            end += 1
            print(f"end += 1")

            while counter == 0:  # valid window
                print(f"counter = 0")
                if end - begin < d:
                    d = end - begin
                    head = begin
                    print(f"if end - begin < d, d: {d}, head: {head}")
                print(f"s[begin:end]: {s[begin:end]}\n")

                map[ord(s[begin])] += 1
                print(f"map_begin:{s[begin]} += 1")
                if map[ord(s[begin])] > 0:
                    counter += 1
                    print(f"if map_begin:{s[begin]} > 0, counter += 1")
                begin += 1
                print(f"begin += 1")
            
            print(f"s[begin:end]: {s[begin:end]}\n")

        return "" if d == float('inf') else s[head:head+d]

### Time Complexity:

## Outer while loop (over end):
# The end pointer traverses the string s from 0 to len(s) - 1.
# It increments end each time, and the total number of iterations of this loop will be O(n), where n is the length of s.

## Inner while loop (over begin):
# The begin pointer moves forward when we find a valid window (i.e., when counter == 0). It increments each time the inner loop runs.
# However, notice that the begin pointer moves at most once for every iteration of the end pointer. This is because, 
# in the worst case, every time the end pointer moves forward, the begin pointer also moves forward (it only advances after the condition counter == 0 is satisfied).
# Therefore, the total number of steps that the begin pointer can take is also O(n).
# Overall Complexity:
# Both the begin and end pointers traverse the string s at most once, meaning the total number of steps for both is proportional to the length of s.
# Each operation inside the while loops (such as checking conditions and updating the map) takes constant time, O(1).
# Thus, the overall time complexity of the algorithm is:
# Time Complexity: O(n), where n is the length of the string s.

### Space Complexity:

# We use an array map of size 128 to store the frequencies of characters in t. Since the size of the map is constant (128), the space complexity is:
# Space Complexity: O(1), as the space used does not depend on the size of the input string s or t.

    # below gives longest strings
    def minWindow2(self, s: str, t: str) -> str:
        # s: long string
        # t: to look for
        
        if len(s) < len(t):
            return ""
        
        s = s.lower()
        t = t.lower()       

        count_s, count_t = [0] * 26, [0] * 26                 
        for i in range(len(s)):
            count_s[ord(s[i]) - ord('a')] += 1
        for i in range(len(t)):
            count_t[ord(t[i]) - ord('a')] += 1           
            
        for i in range (26):  
            if count_s[i] < count_t[i]:
                return ""
        
        l = 0
        r = len(s) - 1
        left = -5
        right = -5
        while l < r:
            if count_t[ord(s[l]) - ord('a')] > 0:
                left = l
            else:
                l += 1
            if count_t[ord(s[r]) - ord('a')] > 0:
                right = r
            else:
                r -= 1
        if left != -5 and right != -5:
            return s[left:right + 1]
        else:
            return ""
            
sol = Solution()
print(sol.minWindow("GOKSUBILGESUBILGE", "GSB"))
# print("BANC\n")
# print(sol.minWindow("ADOBECODEBANC", "ABC"))
# print("\nYXAZ\n")
# print(sol.minWindow("OUZODYXAZV", "XYZ"))
# print("\nxyz\n")
# print(sol.minWindow("xyz", "xyz"))
# print("\n \n")
# print(sol.minWindow("x", "xy"))
            

                


# Minimum Window Substring
# Given two strings s and t, return the shortest substring of s such that every character in t, including duplicates, is present in the substring. If such a substring does not exist, return an empty string "".

# You may assume that the correct output is always unique.

# Example 1:

# Input: s = "OUZODYXAZV", t = "XYZ"

# Output: "YXAZ"
# Explanation: "YXAZ" is the shortest substring that includes "X", "Y", and "Z" from string t.

# Example 2:

# Input: s = "xyz", t = "xyz"

# Output: "xyz"
# Example 3:

# Input: s = "x", t = "xy"

# Output: ""
# Constraints:

# 1 <= s.length <= 1000
# 1 <= t.length <= 1000
# s and t consist of uppercase and lowercase English letters.


# Recommended Time & Space Complexity
# You should aim for a solution with O(n) time and O(m) space, where n is the length of the string s and m is the number of unique characters in s and t.


# Hint 1
# A brute force solution would involve checking every substring of s against t and returning the minimum length valid substring. This would be an O(n^2) solution. Can you think of a better way? Maybe you should think in terms of frequency of characters.


# Hint 2
# We need to find substrings in s that should have atleast the characters of t. We can use hash maps to maintain the frequencies of characters. It will be O(1) for lookups. Can you think of an algorithm now?


# Hint 3
# We can use a dynamically sized sliding window approach on s. We iterate through s while maintaining a window. If the current window contains at least the frequency of characters from t, we update the result and shrink the window until it is valid.


# Hint 4
# We should ensure that we maintain the result substring and only update it if we find a shorter valid substring. Additionally, we need to keep track of the result substring's length so that we can return an empty string if no valid substring is found.


def findSubstring(s: str) -> int:
    map = [0] * 128  # Array to store the frequency of characters (based on ASCII values)
    counter = 0  # To check whether the substring is valid
    begin = end = 0  # Two pointers: one for the head (begin), one for the tail (end)
    d = float('inf')  # To store the length of the substring

    # Initialize the hash map here (example for a simple condition)
    # For example, if we are searching for a substring with all distinct characters:
    # Initialize the map for the required characters here if needed.
    # In this case, no need for specific initialization as the map is already created.

    while end < len(s):
        # Decrease the frequency of the current character at end
        if map[ord(s[end])] > 0:
            counter += 1
        map[ord(s[end])] -= 1
        end += 1

        # While the substring is valid (check counter condition)
        while counter == 0:
            # Update d if finding the minimum length substring
            d = min(d, end - begin)

            # Increase begin to make it invalid/valid again
            map[ord(s[begin])] += 1
            if map[ord(s[begin])] > 0:
                counter -= 1
            begin += 1

        # Update d if finding the maximum length substring
        # For example, you could find the maximum by removing the condition inside the inner loop.
        # if counter == len(t): # A possible condition for maximum.

    return d if d != float('inf') else 0  # Return the length of the substring or 0 if no valid substring found


def lengthOfLongestSubstringTwoDistinct(s: str) -> int:
    map = [0] * 128  # Frequency map for characters (ASCII values)
    counter = 0  # To count the number of distinct characters
    begin = end = 0  # Two pointers: begin and end for sliding window
    d = 0  # To store the length of the longest valid substring

    while end < len(s):
        # Increment the frequency of the character at 'end'
        if map[ord(s[end])] == 0:
            counter += 1
        map[ord(s[end])] += 1
        end += 1

        # While we have more than 2 distinct characters, move the 'begin' pointer
        while counter > 2:
            map[ord(s[begin])] -= 1
            if map[ord(s[begin])] == 0:
                counter -= 1
            begin += 1

        # Update the result with the maximum length of the valid window
        d = max(d, end - begin)

    return d

print(lengthOfLongestSubstringTwoDistinct("ABCDEF"))
print(lengthOfLongestSubstringTwoDistinct("AAAAABCDEF"))


#The code of solving Longest Substring Without Repeating Characters is below:

def lengthOfLongestSubstring(s: str) -> int:
    map = [0] * 128  # Frequency map for characters (ASCII values)
    counter = 0  # To count the number of repeated characters
    begin = end = 0  # Two pointers: begin and end for sliding window
    d = 0  # To store the length of the longest valid substring

    while end < len(s):
        # Increment the frequency of the character at 'end'
        if map[ord(s[end])] > 0:
            counter += 1
        map[ord(s[end])] += 1
        end += 1

        # While there are repeated characters in the window, move the 'begin' pointer
        while counter > 0:
            map[ord(s[begin])] -= 1
            if map[ord(s[begin])] == 1:
                counter -= 1
            begin += 1

        # Update the result with the maximum length of the valid window
        d = max(d, end - begin)

    return d

print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("bbbbb"))
print(lengthOfLongestSubstring("pwwkew"))