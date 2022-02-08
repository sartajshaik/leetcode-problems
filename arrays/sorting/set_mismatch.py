"""
set mismatch
https://leetcode.com/problems/set-mismatch/submissions/
"""
def find_error_nums(nums:list):
  index = 0
  while index < len(nums):
    correct = nums[index] - 1
    if nums[index] != nums[correct]:
      temp = nums[index]
      nums[index] = nums[correct]
      nums[correct] = temp
    else:
      index+=1
  
  for i in range(len(nums)):
    if nums[i] != i+1:
      return [nums[i], i+1]
  
  return [-1,-1]

print(find_error_nums([1,2,2,4]))