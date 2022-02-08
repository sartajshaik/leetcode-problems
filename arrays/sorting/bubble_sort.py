"""
Bubble sort: In every step you are comparing adjacent elements; It is also known as sinking sort or exchange sort or inplace sorting algo

Input: [3,1,5,4,2]
Output: [1,2,3,4,5] 
Best case - O(n) 
Worst case - O(n^2)
"""

def bubble_sort(nums:list):
  swapped = False
  for i in range(0, len(nums)-1):
    swapped = False
    for j in range(0, len(nums)-i-1):
      print(nums)
      if nums[j] > nums[j+1]:
        temp = nums[j+1]
        nums[j+1] = nums[j]
        nums[j] = temp
        swapped = True
    if swapped == False: 
      print("breaking here...")
      break
  return nums

#print(bubble_sort([3,1,5,4,2]))
print(bubble_sort([1,2,3,4,5]))