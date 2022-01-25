"""
https://leetcode.com/problems/product-of-array-except-self/

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
[1,1,1,1]
[1,1,2,6]
[24,12,8,6]
prefix = suffix = 1
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

"""

def productExceptSelf(nums: list) -> list:
  prefix = suffix = 1
  result = [1]*len(nums)

  for i in range(len(nums)):
    result[i] *= prefix
    prefix *= nums[i]
  for i in range(len(nums)-1, -1, -1):
    result[i]*=suffix
    suffix*=nums[i]
  
  return result

print(productExceptSelf([1,2,3,4]))
print(productExceptSelf([-1,1,0,-3,3]))