"""
Insertion sort

Best Case O(n)
Worst Case O(n^2)
"""
def sort(nums: list):
  for i in range(0, len(nums)-1):
    for j in range(i+1, 0, -1):
      if nums[j] < nums[j-1]:
        temp = nums[j]
        nums[j] = nums[j-1]
        nums[j-1] = temp
      else:
        break

nums=[1,2,3,4,5]
sort(nums)
print(nums)
nums=[5,4,3,2,1]
sort(nums)
print(nums)

    
