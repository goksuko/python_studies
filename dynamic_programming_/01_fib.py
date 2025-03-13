    #https://www.google.com/search?sca_esv=25cf531ee370dd12&hl=en&q=dynamic+programming&udm=7&fbs=ABzOT_CWdhQLP1FcmU5B0fn3xuWp6IcynRBrzjy_vjxR0KoDMp_4ut2Z3jppK72fzdIpWsBh1c1UcL3GpFfexaR-aVpgxX5jDEqXoXuITN3jWZBfL41q-IADlsKJQjhZXYAcCq0-vVbUukf_gAjjfmYuarNfGa3RGhHntbkIvNZpwgdfsuMLNABurxC6q9O3hvTLqPxzPwMu&sa=X&ved=2ahUKEwiGq8T_jf-LAxWi_rsIHbe6MEQQtKgLegQIEBAB&biw=1920&bih=919&dpr=1#fpstate=ive&vld=cid:3034548d,vid:oBt53YbR9Kk,st:0

class Solution: 
    #study
    def fib(self, n, res) -> int:
        if n in res.keys():
            return res[n]
        if n == 1 or n == 2:
            return 1
        res[n] = self.fib(n - 1, res) + self.fib(n -2, res)
        return res[n]
        
    
    # dynamic
    def fib4(self, n, res) -> int: #time complexity O(n) #space O(n)
        if n in res:
            return res[n]
        if n <= 2:
            return 1
        res[n] = self.fib(n-1, res) + self.fib(n-2, res)
        return res[n]
    
    #recursive
    def fib3(self, n) -> int: #time complexity O(2^n) #space O(n)
        if n == 1 or n == 2:
            return 1
        return self.fib(n-1) + self.fib(n-2) 
    
    #my solution
    def fib2(self, n) -> int: #time complexity O(n) #space O(1)
        if n == 1 or n == 2:
            return 1
        before = 1
        current = 1        
        while (n != 2):
            answer = before + current
            before = current
            current = answer
            n -= 1
        return answer
            
                    
        

sol = Solution()
# print("fib(5): 5 ->", sol.fib(5))
# print("fib(7): 13->", sol.fib(7))
# #print("fib(50): 12586269025 ->", sol.fib(50)) # took minutes with recursive!
# print("fib(15): 610 ->", sol.fib(15))

print("fib(5): 5 ->", sol.fib(5, {}))
print("fib(7): 13->", sol.fib(7, {}))
print("fib(50): 12586269025 ->", sol.fib(50, {})) # took minutes with recursive!
print("fib(15): 610 ->", sol.fib(15, {}))