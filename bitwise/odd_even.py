#Bitwise odd or even
def odd_even(n: int) -> str:
  return "Odd" if (n & 1) == 1 else "Even"

print(odd_even(12))