from typing import List

class Solution:
	#my solution
	def maxProfit(self, prices: List[int]) -> int:
		minimum = 101
		profit = 0
		for num in prices:
			minimum = min(minimum, num)
			if num > minimum:
				profit = max(profit, num-minimum)
		return profit
	
	# 3. Dynamic Programming
	def maxProfit2(self, prices: List[int]) -> int:
		maxP = 0
		minBuy = prices[0]

		for sell in prices:
			maxP = max(maxP, sell - minBuy)
			minBuy = min(minBuy, sell)
		return maxP

# Best Time to Buy and Sell Stock
# You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.

# You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.

# Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.

# Example 1:

# Input: prices = [10,1,5,6,7,1]

# Output: 6
# Explanation: Buy prices[1] and sell prices[4], profit = 7 - 1 = 6.

# Example 2:

# Input: prices = [10,8,7,5,2]

# Output: 0
# Explanation: No profitable transactions can be made, thus the max profit is 0.

# Constraints:

# 1 <= prices.length <= 100
# 0 <= prices[i] <= 100


# Recommended Time & Space Complexity
# You should aim for a solution with O(n) time and O(1) space, where n is the size of the input array.


# Hint 1
# A brute force solution would be to iterate through the array with index i, considering it as the day to buy, and trying all possible options for selling it on the days to the right of index i. This would be an O(n^2) solution. Can you think of a better way?


# Hint 2
# You should buy at a price and always sell at a higher price. Can you iterate through the array with index i, considering it as either the buying price or the selling price?


# Hint 3
# We can iterate through the array with index i, considering it as the selling value. But what value will it be optimal to consider as buying point on the left of index i?


# Hint 4
# We are trying to maximize profit = sell - buy. If the current i is the sell value, we want to choose the minimum buy value to the left of i to maximize the profit. The result will be the maximum profit among all. However, if all profits are negative, we can return 0 since we are allowed to skip doing transaction.