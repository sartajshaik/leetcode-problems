"""
Disappeared numbers

https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
"""
def disappeared_nums(nums:list):
  index = 0
  while index < len(nums):
      correct = nums[index] - 1
      if nums[index] != nums[correct]:
          temp = nums[correct]
          nums[correct] = nums[index]
          nums[index] = temp
      else:
          index+=1
  print(nums)
  disappeared = list()
  for i in range(len(nums)):
      if i!=nums[i]-1:
          disappeared.append(i+1)
  return disappeared

nums = [4,3,2,7,8,2,3,1]
print(disappeared_nums(nums))
