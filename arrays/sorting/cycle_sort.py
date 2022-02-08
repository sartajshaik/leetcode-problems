"""
Cyclic sort

Best Case O(n)
"""
def cycle_sort(nums:list):
  index = 0
  while index < len(nums):
    if nums[index] != nums[nums[index]-1]:
      #index + 1:
      temp = nums[nums[index]-1]
      nums[nums[index]-1] = nums[index]
      nums[index] = temp
    else:
      index+=1

nums=[5,4,2,1,3]
print(nums)
cycle_sort(nums)
print(nums)