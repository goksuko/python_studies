class Solution:
    def fib(self, n): #time O(n) space O(n)
        table = [0] * (n +3)
        table[1] = 1
        for i in range(n+1):
            table[i+1] += table[i]
            table[i+2] += table[i]
            print(table)
        return table[n]

        
sol = Solution()
print("fib(5): 5 ->", sol.fib(5))
print("fib(7): 13->", sol.fib(7))
#print("fib(50): 12586269025 ->", sol.fib(50)) # took minutes with recursive!
print("fib(15): 610 ->", sol.fib(15))