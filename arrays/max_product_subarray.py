"""
https://leetcode.com/problems/maximum-product-subarray/

Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

A subarray is a contiguous subsequence of the array.

 

Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""

def maxProduct(nums: list) -> int:
  current_min = current_max = result = nums[0]
  for n in nums[1:]:
    temp = current_max
    current_max = max(current_max * n, current_min * n, n)
    current_min = min(temp * n, current_min*n, n)
    result = max(result, current_max)
  
  print(result, current_max, current_min)
  return current_max


maxProduct([2,3,-2,4])