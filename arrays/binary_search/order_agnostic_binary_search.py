"""
This is same as regular binary search, only difference is you would be figuring out what's the order of the input
"""
def orderAgnosticBinarySearch(input:list, target:int)-> bool:
  left, right = 0, len(input) - 1
  asc = input[right] > input[left]
  while left <= right:
    mid = left + (right-left)//2
    if asc:
      if input[mid] > target:
        right = mid - 1
      elif input[mid] < target:
        left = mid + 1
    else:
      if input[mid] < target:
        right = mid - 1
      elif input[mid] > target:
        left = mid + 1
    if input[mid] == target:
      return True
  return False

print(orderAgnosticBinarySearch([1,2,3,4,5,6,7,8,9], 9))
print(orderAgnosticBinarySearch([1,2,3,4,5,6,7,8,9], 19))
print(orderAgnosticBinarySearch([-1,-2,-3,-4,-5,-6,-7,-8,-9], -9))
print(orderAgnosticBinarySearch([-1,-2,-3,-4,-5,-6,-7,-8,-9], 9))