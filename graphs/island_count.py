"""
island count
Write a function, islandCount, that takes in a grid containing Ws and Ls. W represents water and L represents land. The function should return the number of islands on the grid. An island is a vertically or horizontally connected region of land.
grid = [
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'W', 'W', 'L', 'W'],
  ['W', 'W', 'L', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['L', 'L', 'W', 'W', 'W'],
]
"""


def island_count(grid) -> int:
  visited = set()
  count = 0

  for row in range(0, len(grid)):
    for column in range(0, len(grid[row])):
      if grid[row][column] != 'L':
        continue
      if explore(grid, row, column, visited):
        count+=1
  return count

def explore(grid, row, column, visited) -> bool:
  rowInbound = row >=0 and row < len(grid)
  colInbound = column >=0 and column < len(grid[0])

  if not rowInbound or not colInbound: 
    return False
  
  if grid[row][column] == 'W':
    return False

  if (row, column) in visited:
    return False
  
  visited.add((row, column))

  explore(grid, row, column + 1, visited)
  explore(grid, row, column - 1, visited)
  explore(grid, row + 1, column, visited)
  explore(grid, row - 1, column, visited)
  
  return True

grid = [
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'W', 'W', 'L', 'W'],
  ['W', 'W', 'L', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['L', 'L', 'W', 'W', 'W'],
]
print(island_count(grid))

grid = [
  ['L', 'W', 'W', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['W', 'L', 'W', 'L', 'W'],
  ['W', 'W', 'W', 'W', 'W'],
  ['W', 'W', 'L', 'L', 'L'],
]

print(island_count(grid))

grid = [
  ['L', 'L', 'L'],
  ['L', 'L', 'L'],
  ['L', 'L', 'L'],
]

print(island_count(grid))

grid = [
  ['W', 'W'],
  ['W', 'W'],
  ['W', 'W'],
]

print(island_count(grid))