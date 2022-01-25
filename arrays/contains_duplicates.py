"""
https://leetcode.com/problems/contains-duplicate/

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

"""
#Bruteforce method is to run two loops over the given array

# def containsDuplicates(nums: list) -> bool:
#   for i in range(len(nums)):
#     for j in range(i+1, len(nums)):
#       if nums[i]==nums[j]:
#         return True
#   return False;

#Other O(nlong(n)) approach would be to sort the array and look for adjacent elements if they're equal. I'm yet to master the sorting so not going to implement at this time. Let's look at our linear time solution with some space trade offs

def containsDuplicates(nums: list) -> int:
  registry = set() #as I iterate, I keep adding elements

  for n in nums:
    if n in registry:
      return True
    registry.add(n)
  return False


print(containsDuplicates(nums = [1,2,3,1]))
print(containsDuplicates(nums = [1,2,3,4]))
print(containsDuplicates(nums = [1,1,1,3,3,4,3,2,4,2]))