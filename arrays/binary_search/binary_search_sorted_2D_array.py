"""
Binary search in sorted 2D array
[
  [1,2,3,4],
  [5,6,7,8],
  [9,10,11,12],
  [13,14,15,16]
]
"""
#Search in the row and the columns range provided
def binary_search(nums: list, row: int, cStart: int, cEnd: int, target: int):
  print_list(nums)
  while cStart <= cEnd:
    mid = cStart + (cEnd-cStart)//2
    if nums[row][mid] == target:
      return [row, mid]
    elif nums[row][mid] < target:
      cStart = mid + 1
    else:
      cEnd = mid - 1
  return [-1, -1]

def search(matrix, target):
  rows = len(matrix)
  cols = len(matrix[0])

  if rows == 1:
    return binary_search(matrix, 0, 0, cols-1, target)

  rStart = 0
  rEnd = rows - 1
  cMid = cols//2

  #run the loop till 2 rows are remaining
  while rStart < rEnd - 1:
    mid = rStart + (rEnd - rStart)//2
    if matrix[mid][cMid] == target:
      return [mid, cMid]
    elif matrix[mid][cMid] < target:
      rStart = mid
    else:
      rEnd = mid
  # Now we have two rows
  # Check whether the target is in the column of two rows
  if matrix[rStart][cMid] == target:
    return [rStart, cMid]
  elif matrix[rStart + 1][cMid] == target:
    return [rStart + 1, cMid]
  
  # Search in 1st half
  if target <= matrix[rStart][cMid - 1]:
    return binary_search(matrix, rStart, 0, cMid - 1, target)
  if target >= matrix[rStart][cMid + 1] and target <= matrix[rStart][cols - 1]:
    return binary_search(matrix, rStart, cMid + 1, cols-1, target)
  if target <= matrix[rStart + 1][cMid - 1]:
    return binary_search(matrix, rStart + 1, 0, cMid - 1, target)
  else:
    return binary_search(matrix, rStart+1, cMid+1, cols-1, target)

def print_list(nums):
  for i in range(len(nums)):
    for j in range(len(nums[i])):
      print(nums[i][j], end=" ")
    print()


nums = [
  [1,2,3,4],
  [5,6,7,8],
  [9,10,11,12],
  [13,14,15,16]
  ]
print(search(nums, 8))