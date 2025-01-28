

class Solution(object):
    
    def shiftingLetters2(self, s: str, shifts: list[list[int]]) -> str:
        n = len(s)
        shift = [0] * (n + 1)

        for sh in shifts:
            start, end, direction = sh
            shift[start] += (1 if direction == 1 else -1)
            if end + 1 < n:
                shift[end + 1] -= (1 if direction == 1 else -1)
            print(f"sh {sh} shift {shift}")

        currentShift = 0
        shiftList = list(s)
        for i in range(n):
            currentShift += shift[i]
            print(f"cur {currentShift}")
            netShift = (currentShift % 26 + 26) % 26
            shiftList[i] = chr((ord(shiftList[i]) - ord('a') + netShift) % 26 + ord('a'))

        return ''.join(shiftList) 
    
    
    def shiftingLetters(self, s, shifts):
        """
        :type s: str
        :type shifts: List[List[int]]
        :rtype: str
        """
        n = len(s)
        shift = [0] * (n + 1)
        s_l = list(s)  # Convert string to list to modify characters
        for sh in shifts:
            l, r, dir = sh
            for i in range(l, r + 1):
                if (dir == 1):
                    shift[i] += 1
                else:
                    shift[i] -= 1
        # print(shift)
        
        for i in range(n):
            s_l[i] = chr((ord(s_l[i]) - ord('a') + shift[i] + 26) % 26 + ord('a'))                  
        
        return ''.join(s_l)  # Convert list back to string
                  
sol = Solution()
print(sol.shiftingLetters(s = "abc", shifts = [[0,1,0],[1,2,1],[0,2,1]]))
                    
            

# 2381. Shifting Letters II
# Medium

# You are given a string s of lowercase English letters and a 2D integer array shifts where shifts[i] = [starti, endi, directioni]. For every i, shift the characters in s from the index starti to the index endi (inclusive) forward if directioni = 1, or shift the characters backward if directioni = 0.

# Shifting a character forward means replacing it with the next letter in the alphabet (wrapping around so that 'z' becomes 'a'). Similarly, shifting a character backward means replacing it with the previous letter in the alphabet (wrapping around so that 'a' becomes 'z').

# Return the final string after all such shifts to s are applied.

 

# Example 1:

# Input: s = "abc", shifts = [[0,1,0],[1,2,1],[0,2,1]]
# Output: "ace"
# Explanation: Firstly, shift the characters from index 0 to index 1 backward. Now s = "zac".
# Secondly, shift the characters from index 1 to index 2 forward. Now s = "zbd".
# Finally, shift the characters from index 0 to index 2 forward. Now s = "ace".
# Example 2:

# Input: s = "dztz", shifts = [[0,0,0],[1,1,1]]
# Output: "catz"
# Explanation: Firstly, shift the characters from index 0 to index 0 backward. Now s = "cztz".
# Finally, shift the characters from index 1 to index 1 forward. Now s = "catz".
 

# Constraints:

# 1 <= s.length, shifts.length <= 5 * 104
# shifts[i].length == 3
# 0 <= starti <= endi < s.length
# 0 <= directioni <= 1
# s consists of lowercase English letters.