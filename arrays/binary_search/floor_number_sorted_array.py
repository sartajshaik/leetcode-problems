def floor(input:list, target:int) -> int:
  leftP, rightP = 0, len(input) - 1
  #If there is no number smaller than the target number, return -1
  if target < input[0]:
    return -1
  while leftP <= rightP:
    mid = leftP + (rightP - leftP)//2
    if input[mid] > target:
      rightP = mid - 1
    elif input[mid] < target:
      leftP = mid + 1
    else:
      return input[mid]
  return input[rightP]

print(floor([1,2,3,4,5,6,8,9,10], 7))
print(floor([1,2,3,4,5,6,7,8,9,10,18], 17))