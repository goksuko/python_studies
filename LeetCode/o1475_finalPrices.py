class Solution(object):
    def finalPrices(self, prices):
        print(prices)
        # Initialize an empty stack to keep track of prices for discount calculation
        stack = []
        # Initialize the answer array with the original prices
        answer = prices[:]
        
        # Traverse the prices from right to left
        for i in range(len(prices) - 1, -1, -1):
            print(f"price: {prices[i]}")
            # While the stack is not empty and the top element of the stack is greater than
            # the current price, pop it from the stack (this means the discount won't apply)
            while stack and stack[-1] > prices[i]:
                stack.pop()
            
            # If the stack is not empty, the top element is the next valid discount
            if stack:
                answer[i] -= stack[-1]
            
            # Push the current price onto the stack for future discount calculations
            stack.append(prices[i])
            print(answer)
            print(f"stack_now: {stack}")
        return answer
    
    def finalPrices2(self, prices): #beats 17%
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                if prices[j] <= prices[i]:
                    prices[i] -= prices[j]
                    break
        return prices
        
        
sol = Solution()
sol.finalPrices(prices = [1,2,3,4,5,4,3,2,1])                    
            # 8,4,6,2,3


# 1475. Final Prices With a Special Discount in a Shop
# Easy

# You are given an integer array prices where prices[i] is the price of the ith item in a shop.

# There is a special discount for items in the shop. If you buy the ith item, then you will receive a discount equivalent to prices[j] where j is the minimum index such that j > i and prices[j] <= prices[i]. Otherwise, you will not receive any discount at all.

# Return an integer array answer where answer[i] is the final price you will pay for the ith item of the shop, considering the special discount.

 

# Example 1:

# Input: prices = [8,4,6,2,3]
# Output: [4,2,4,2,3]
# Explanation: 
# For item 0 with price[0]=8 you will receive a discount equivalent to prices[1]=4, therefore, the final price you will pay is 8 - 4 = 4.
# For item 1 with price[1]=4 you will receive a discount equivalent to prices[3]=2, therefore, the final price you will pay is 4 - 2 = 2.
# For item 2 with price[2]=6 you will receive a discount equivalent to prices[3]=2, therefore, the final price you will pay is 6 - 2 = 4.
# For items 3 and 4 you will not receive any discount at all.
# Example 2:

# Input: prices = [1,2,3,4,5]
# Output: [1,2,3,4,5]
# Explanation: In this case, for all items, you will not receive any discount at all.
# Example 3:

# Input: prices = [10,1,1,6]
# Output: [9,0,1,6]
 

# Constraints:

# 1 <= prices.length <= 500
# 1 <= prices[i] <= 1000