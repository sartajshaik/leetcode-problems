"""
First missing positive
https://leetcode.com/problems/first-missing-positive/submissions/

Example 1:

Input: nums = [1,2,0]
Output: 3
Example 2:

Input: nums = [3,4,-1,1]
Output: 2
Example 3:

Input: nums = [7,8,9,11,12]
Output: 1
"""
def first_missing_positive(nums:list):
  index = 0
  while index < len(nums):
    correct = nums[index] - 1
    if nums[index] > 0 and nums[index] <= len(nums) and nums[index] != nums[correct]:
      temp = nums[index]
      nums[index] = nums[correct]
      nums[correct] = temp
    else:
      index+=1
  for i in range(len(nums)):
    if nums[i] != i+1:
      return i+1
  return len(nums)+1

nums = [7,8,9,11,12]
print(first_missing_positive(nums))
nums = [1]
print(first_missing_positive(nums))