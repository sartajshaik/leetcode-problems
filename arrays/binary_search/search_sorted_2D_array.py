"""
Binary search in sorted 2D array
[
  [20,30,40,50],
  [21,31,41,51],
  [22,32,42,52],
  [23,33,43,53]
]
"""
def binary_search2D(nums, target):
  print_list(nums)
  start, end = 0, len(nums)-1
  while start < len(nums) and end >=0:
    if nums[start][end] == target:
      return [start, end]
    elif nums[start][end] < target:
      start+=1
    else:
      end-=1
  return [-1,-1]

def print_list(nums):
  for i in range(len(nums)):
    for j in range(len(nums[i])):
      print(nums[i][j], end=" ")
    print()


nums = [[20,30,40,50],[21,31,41,51],[22,32,42,52],[23,33,43,53]]
print(binary_search2D(nums, 53))