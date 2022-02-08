"""
Factorial of a number - 5! = 5*4*3*2*1
"""

def factorial(n: int) -> int:
  if n==1: return n
  return n * factorial(n-1)

def sumofdigits(n: int) -> int:
  print(n)
  if n <= 0: return 0
  return n%10 + sumofdigits(n//10)

def reverse_number(n: int) -> int:
  print(n)
  if n<9: return n
  return n%10 + reverse_number(n//10)

def count_zeros(n: int):
  if n <= 0: return 0
  if n%10 == 0: return 1+count_zeros(n//10)
  else: return count_zeros(n//10)

def is_array_sorted(nums: list, index: int):
  if index == len(nums) - 1 : return True
  return nums[index] < nums[index+1] and is_array_sorted(nums, index+1)

def linear_search(nums:list, index, target):
  if index == len(nums)-1: return False
  return nums[index] == target or linear_search(nums, index+1, target)

def linear_search_all_indexes(nums: list, index, target, ans:list):
  if index == len(nums): return ans
  if nums[index] == target: 
    ans.append(index)
  return linear_search_all_indexes(nums, index+1, target, ans)
  
print(linear_search_all_indexes([1,2,3,4,6,8,8,8],0,8,[]))
