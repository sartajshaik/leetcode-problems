"""
Find all duplicates
https://leetcode.com/problems/find-all-duplicates-in-an-array/submissions/
"""
def find_duplicates(nums:list) -> list:
  index=0
  results = list()
  while index<len(nums):
      correct = nums[index]-1
      if nums[correct] != nums[index]:
          temp = nums[correct]
          nums[correct] = nums[index]
          nums[index] = temp
      else:
          index+=1
  print(nums)
  for i in range(len(nums)):
      if nums[i] != i+1:
          results.append(nums[i])
  return results

print(find_duplicates([4,3,2,7,8,2,3,1]))