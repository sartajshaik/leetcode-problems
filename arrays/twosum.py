"""
Two Sum Problem:
nums = [2,7,11,15], target = 9

"""
#Bruteforce method, with O(n^2)

def two_sums(nums:list, target:int) -> list:
  for i in range(len(nums)):
    for j in range(i+1, len(nums)):
      if target == nums[i] + nums[j]:
        return [i, j]
  return []

print(two_sums(nums = [2,7,11,15], target = 9))

#Linear complexity solution, where we are storing the result of the target-num into a O(1) hashmap. When the array element is in the map which means we found our pair
def twoSums(nums:list, target: int) -> list:
  remainders = {}

  for i, n in enumerate(nums):
    if n in remainders:
      return [remainders[n], i]
    remainders[target-n] = i
  return []

print(twoSums(nums = [2,7,11,15], target = 9))