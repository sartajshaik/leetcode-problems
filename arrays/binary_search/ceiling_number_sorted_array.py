def ceiling(input:list, target:int) -> int:
  leftP, rightP = 0, len(input) - 1
  #If there is no number greater than the target, then return -1
  if target > input[len(input)-1]:
    return -1
  while leftP <= rightP:
    mid = leftP + (rightP - leftP)//2
    if input[mid] > target:
      rightP = mid - 1
    elif input[mid] < target:
      leftP = mid + 1
    else:
      return input[mid]
  return input[leftP]

print(ceiling([1,2,3,4,5,6,8,9,10], 7))
print(ceiling([1,2,3,4,5,6,7,8,9,10,18], 17))