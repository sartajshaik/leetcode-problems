"""
Position of an array in infinite sorted array
"""

#Since the given array is infinite, you can't use the length of it. So let's find the range (start and end) of the array to search [1,2,3,4,5,6,7,8,9]
def findRange(nums: list, target: int) -> int:
  start, end = 0, 1
  while target > nums[end]:
    newStart = end + 1
    end = end + (end - start + 1)*2;
    start = newStart
    #print(start, end)
  return binary_search(nums, start, end, target)

#Regular binary search
def binary_search(nums: list, start:int, end: int, target: int) -> int:
  while start <= end:
    mid = start + (end - start)//2
    #print(mid)
    if target < nums[mid]:
      end = mid - 1
    elif target > nums[mid]:
      start = mid + 1
    else:
      return mid
  return -1

print(findRange([1,2,3,4,5,6,7,8,9,10,11,200,400,1212,121212],8))
