#star

class Solution(object):
    #visual example below
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []
        
        for ast in asteroids:
            # Handle collisions only if current is left-moving and top is right-moving
            while stack and ast < 0 < stack[-1]:
                if stack[-1] < -ast:   # Top is smaller; explode top
                    stack.pop()
                    continue    # ← JUMPS back to "while stack and ast < 0 < stack[-1]:"
                elif stack[-1] == -ast:  # Same size; both explode
                    stack.pop()
                break  # Either way, current one is gone  # ← EXITS while loop completely
            else:
                stack.append(ast)
        
        return stack
    
    
    # slower
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        st = []
        
        for a in asteroids:
            if not st:
                st.append(a)
            else:
                st.append(a)
                while len(st) >= 2:
                    curr = st.pop()
                    if curr < 0 and st[-1] > 0:
                        if abs(st[-1]) == abs(curr):
                            st.pop()  # Both explode
                        elif abs(st[-1]) > abs(curr):
                            # Right-moving survives
                            continue
                        else:
                            # Left-moving survives
                            st.pop()
                            st.append(curr)
                    else:
                        st.append(curr)
                        break
        
        return st 
        

sol = Solution()
asteroids = [5,10,-5]
print(f"[5,10]: {sol.asteroidCollision(asteroids)}")
asteroids = [8,-8]
print(f"[]: {sol.asteroidCollision(asteroids)}")
asteroids = [10,2,-5]      
print(f"[10]: {sol.asteroidCollision(asteroids)}")

# VISUAL EXAMPLE

#asteroids = [10, 2, -5]
# stack = []

# # ast = 10: No collision, add to stack
# # stack = [10]

# # ast = 2: No collision, add to stack  
# # stack = [10, 2]

# # ast = -5: Collision with 2!
# while stack and -5 < 0 < stack[-1]:  # True: -5 < 0 < 2
#     if stack[-1] < -(-5):  # if 2 < 5: TRUE
#         stack.pop()        # Remove 2, stack = [10]
#         continue           # ← Back to while condition
        
# # Second iteration of while:
# while stack and -5 < 0 < stack[-1]:  # True: -5 < 0 < 10  
#     if stack[-1] < -(-5):  # if 10 < 5: FALSE
#     elif stack[-1] == -(-5):  # if 10 == 5: FALSE
#     break                  # ← Exit while loop, -5 is destroyed

# # Result: stack = [10]
            

# 735. Asteroid Collision
# Medium

# We are given an array asteroids of integers representing asteroids in a row. The indices of the asteriod in the array represent their relative position in space.

# For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

# Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

 

# Example 1:

# Input: asteroids = [5,10,-5]
# Output: [5,10]
# Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.
# Example 2:

# Input: asteroids = [8,-8]
# Output: []
# Explanation: The 8 and -8 collide exploding each other.
# Example 3:

# Input: asteroids = [10,2,-5]
# Output: [10]
# Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.
 

# Constraints:

# 2 <= asteroids.length <= 104
# -1000 <= asteroids[i] <= 1000
# asteroids[i] != 0