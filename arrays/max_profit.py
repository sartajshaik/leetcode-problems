"""
LeetCode 121. Best Time to Buy and Sell Stock

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

prices = [7,1,5,3,6,4]
Output: 5
"""
def maxProfit(prices:list) -> int:
  leftPointer, rightPointer = 0, 1
  maxProfit = profit = 0
  while rightPointer < len(prices):
    if prices[leftPointer] < prices[rightPointer]:
      profit = prices[rightPointer] - prices[leftPointer]
      maxProfit = max(profit, maxProfit)
    else:
      leftPointer = rightPointer

    rightPointer+=1
  return maxProfit

print(maxProfit([7,1,5,3,6,4]))
