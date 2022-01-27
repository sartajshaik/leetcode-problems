def smallestLetterLargerThanTarget(letters:list, target:str) -> str:
  left, right = 0, len(letters) - 1
  while left<=right:
    mid = int(left + (right-left)/2)
    if letters[mid] > target:
      right = mid - 1
    else:
      left = mid + 1
  return letters[left%(len(letters))]

print(smallestLetterLargerThanTarget(['a','c','d','f'],'b'))