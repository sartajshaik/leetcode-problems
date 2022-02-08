"""
Binary search recurrsion
"""
def binary_search(nums:list, start:int, end:int, target:int) -> int:
  if start > end: return -1
  mid = start + (end-start)//2
  if nums[mid] == target:
    return mid
  elif nums[mid] < target:
    return binary_search(nums, mid + 1, end, target)
  else:
    return binary_search(nums, start, mid - 1, target)


print(binary_search([1,2,3,4,5,6],0,5,6))