"""
Bubble sort using recursion
[9,3,2,5,4,1,8,7,6]
[1,2,3,4,5,6,7,8,9]
"""
def bubble_sort(nums: list, i:int, j:int):
  if i == 0: return
  if j < i:
    if nums[j] > nums[j+1]:
      temp = nums[j]
      nums[j] = nums[j+1]
      nums[j+1] = temp
    bubble_sort(nums, i, j+1)
  else:
    bubble_sort(nums, i-1, 0)

nums=[9,3,2,5,4,1,8,7,6]

print(f"Before sorting {nums}")
bubble_sort(nums, len(nums)-1, 0);
print(f"After sorting  {nums}")