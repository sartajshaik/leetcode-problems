"""
Missing Number

https://leetcode.com/problems/missing-number/submissions/
"""
def missing_number(nums:list):
  index = 0;
  while index < len(nums):
    if nums[index] < len(nums) and nums[index] != nums[nums[index]]:
      temp = nums[nums[index]]
      nums[nums[index]] = nums[index]
      nums[index] = temp
    else:
      index+=1
  #search for first missing number
  for i, n in enumerate(nums):
    if(nums[i] != i):
      return i;
  return len(nums)

#nums=[5,4,2,0,3]
nums=[2,0,1]
print(nums)
print(missing_number(nums))
print(nums)