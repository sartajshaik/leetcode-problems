"""
https://leetcode.com/problems/maximum-subarray/
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:

Input: nums = [1]
Output: 1
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23

"""

def maxSubArray(nums: list) -> int:
  largest_sum = nums[0]
  max_ending = nums[0]
  for i in range(1, len(nums)):
    max_ending = max(nums[i], max_ending+nums[i])
    largest_sum = max(largest_sum, max_ending)
  return largest_sum

print(maxSubArray(nums = [-2,1,-3,4,-1,2,1,-5,4]))
print(maxSubArray(nums = [5,4,-1,7,8]))
print(maxSubArray(nums = [1]))
