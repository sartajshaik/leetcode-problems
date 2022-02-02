"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.


"""
def searchRange(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    ans = [-1,-1]
    ans[0] = binary_search(nums, target, True)
    if ans[0] != -1:
      ans[1] = binary_search(nums, target, False)
    return ans
    
def binary_search(nums, target, firstOccurrence):
    left, right = 0, len(nums)-1
    ans = -1
    while left <= right:
        mid = left + (right-left)//2
        if nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            ans = mid
            if firstOccurrence:
                right = mid - 1
            else:
                left = mid + 1
    return ans

print(searchRange([1,1,1,2,3,3,4,5,6],1))