#Find Unique number in an array
#XOR with same number gives 0, this can be achieved in O(n)
def find_unique(nums: list) -> int:
  result = 0
  for n in nums:
    result ^= n
  return result

print(find_unique([1,1,2,2,3,4,5,4,3,6,5]))