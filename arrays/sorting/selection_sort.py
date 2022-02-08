"""
Selection sort
1. Find max element and swap with end or find min element and swap with start, repeat
Best Case O(n^2)
Worst Case O(n^2)
"""
def sort(nums: list):
  for i in range(0, len(nums)):
    maxIndex = 0
    for j in range(0, len(nums) - i):
      if nums[maxIndex] < nums[j]:
        maxIndex = j
    temp = nums[len(nums) - i - 1]
    nums[len(nums) - i - 1] = nums[maxIndex]
    nums[maxIndex] = temp
    print(nums)

sort([5,4,3,2,1])
sort([1,2,3,4,5])
    
