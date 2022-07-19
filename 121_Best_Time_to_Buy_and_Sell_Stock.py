'''
121. Best Time to Buy and Sell Stock

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
 
'''

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         min_value = min(prices)
#         value_index = prices.index(min_value)
        
#         max_value = max(prices[value_index : ])
        
#         max_profit = max_value - min_value
        
#         return max_profit

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_profit = 0
        lowest = prices[0]
        
        for new_value in prices:
            if new_value < lowest:
                lowest = new_value
                pass
            new_profit = new_value - lowest
            if new_profit > max_profit:
                max_profit = new_profit
        
        return max_profit


'''
Success
Details 
Runtime: 1336 ms, faster than 69.44% of Python3 online submissions for Best Time to Buy and Sell Stock.
Memory Usage: 25 MB, less than 85.25% of Python3 online submissions for Best Time to Buy and Sell Stock.
'''