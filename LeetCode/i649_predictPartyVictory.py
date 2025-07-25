# star

from collections import deque

class Solution:
    # the logic but there ois a better solution below
    def predictPartyVictory(self, senate):
        senate = list(senate)
        while 'R' in senate and 'D' in senate and len(senate) > 1:
            current = senate.pop(0)
            if current == 'R':
                senate.remove('D')
                senate.append('R')
            elif current == 'D':
                senate.remove('R')
                senate.append('D')
        if 'D' in senate:
            return "Dire"
        else:
            return "Radiant"
        
    
    
    def predictPartyVictory(self, senate):
        radiant = deque()
        dire = deque()
        n = len(senate)

        # Initialize queues with indices of senators
        for i, s in enumerate(senate):
            if s == 'R':
                radiant.append(i)
            else:
                dire.append(i)

        # Simulate the voting rounds
        while radiant and dire:
            r = radiant.popleft()
            d = dire.popleft()
            if r < d:
                # Radiant senator acts first, gets re-added with updated index
                radiant.append(r + n)
            else:
                # Dire senator acts first
                dire.append(d + n)

        return "Radiant" if radiant else "Dire"
    
    # my slow solution
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        senate = list(senate)
        i = 0
        l = len(senate)               
        while 'R' in senate and 'D' in senate:
            if senate[i % l] == 'R':
                j = i
                while senate[j % l] != 'D':
                    j += 1
                senate[j % l] = '0'
            elif senate[i % l] == 'D':
                j = i
                while senate[j % l] != 'R':
                    j += 1
                senate[j % l] = '0'
            i += 1
        if 'D' in senate:
            return "Dire"
        else:
            return "Radiant"
        
sol = Solution()
print(sol.predictPartyVictory("DDRRR"))
        
            
        
        
        
# 649. Dota2 Senate

# In the world of Dota2, there are two parties: the Radiant and the Dire.

# The Dota2 senate consists of senators coming from two parties. Now the Senate wants to decide on a change in the Dota2 game. The voting for this change is a round-based procedure. In each round, each senator can exercise one of the two rights:

# Ban one senator's right: A senator can make another senator lose all his rights in this and all the following rounds.
# Announce the victory: If this senator found the senators who still have rights to vote are all from the same party, he can announce the victory and decide on the change in the game.
# Given a string senate representing each senator's party belonging. The character 'R' and 'D' represent the Radiant party and the Dire party. Then if there are n senators, the size of the given string will be n.

# The round-based procedure starts from the first senator to the last senator in the given order. This procedure will last until the end of voting. All the senators who have lost their rights will be skipped during the procedure.

# Suppose every senator is smart enough and will play the best strategy for his own party. Predict which party will finally announce the victory and change the Dota2 game. The output should be "Radiant" or "Dire".

 

# Example 1:

# Input: senate = "RD"
# Output: "Radiant"
# Explanation: 
# The first senator comes from Radiant and he can just ban the next senator's right in round 1. 
# And the second senator can't exercise any rights anymore since his right has been banned. 
# And in round 2, the first senator can just announce the victory since he is the only guy in the senate who can vote.
# Example 2:

# Input: senate = "RDD"
# Output: "Dire"
# Explanation: 
# The first senator comes from Radiant and he can just ban the next senator's right in round 1. 
# And the second senator can't exercise any rights anymore since his right has been banned. 
# And the third senator comes from Dire and he can ban the first senator's right in round 1. 
# And in round 2, the third senator can just announce the victory since he is the only guy in the senate who can vote.
 

# Constraints:

# n == senate.length
# 1 <= n <= 104
# senate[i] is either 'R' or 'D'.