"""
Binary search O(longn)
"""
def binary_search(input:list, target:int) -> bool:
  #Start with two pointers, beginning and end of the input array
  leftP, rightP = 0, len(input)-1
  #While Left Pointer is less than or equal to the Right Pointer, keep looping
  while (leftP <= rightP):
    #Calculate the mid point based on left and right pointer, //2 returns integer value
    mid = leftP + (rightP - leftP)//2
    #When the mid value is greater than target, look into first half so you need to move the right pointer to mid-1
    if input[mid] > target:
      rightP = mid - 1
    #When the mid value is smaller than the target, look into the second half of the input so you need to move the left pointer to mid + 1
    elif input[mid] < target:
      leftP = mid + 1
    #Otherwise, see if the mid value matched the target
    else:
      return True
    #When Left Pointer crosses right pointer, you can return Left Pointer value which is the smallest larger number than the target. Return right pointer value which is the largest smaller number than the target.
  return False

print(binary_search([1,2,3,4,5,6,7,8,9,10], 7))
print(binary_search([1,2,3,4,5,6,7,8,9,10], 17))