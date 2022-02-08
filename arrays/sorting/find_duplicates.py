"""
Find duplicate
https://leetcode.com/problems/find-the-duplicate-number/
"""

def find_duplicate(nums:list):
  index = 0
  while index < len(nums):
      correct = nums[index] - 1
      if nums[index] != nums[correct]:
          temp = nums[correct]
          nums[correct] = nums[index]
          nums[index] = temp
      else:
          index+=1
  for i in range(len(nums)):
      if i!=nums[i]-1:
          return nums[i]
  return -1
"""
Alternate version using hash set
def find_duplicate(nums:list):
  nums_set = set()
  for num in nums:
    if num in nums_set:
      return num
    nums_set.add(num)
  return -1

"""

nums = [1,3,4,2,2]
print(find_duplicate(nums))