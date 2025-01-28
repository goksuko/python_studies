A = [1,2,3,4]
B = A[::-1]
print(B)
total = 0
for n in A:
    total += n
C = []
for n in A:
	C.append(total - n)
print(min(C), " ", max(C))


# An array is a type of data structure that stores elements of the same type in a contiguous block of memory. In an array, A, of size N, each memory location has some unique index, i (where 0 <= i  < N), that can be referenced as A[i] or Ai.

# Reverse an array of integers.

# Note: If you've already solved our C++ domain's Arrays Introduction challenge, you may want to skip this.

# Example

# Return .

# Function Description

# Complete the function reverseArray in the editor below.

# reverseArray has the following parameter(s):

# int A[n]: the array to reverse
# Returns

# int[n]: the reversed array
# Input Format

# The first line contains an integer, , the number of integers in .
# The second line contains  space-separated integers that make up .

# Constraints

