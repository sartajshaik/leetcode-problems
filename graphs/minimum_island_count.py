"""
Write a function, minimumIsland, that takes in a grid containing Ws and Ls. W represents water and L represents land. The function should return the size of the smallest island. An island is a vertically or horizontally connected region of land.

You may assume that the grid contains at least one island.

grid = [
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'W', 'W', 'L', 'W'],
  ['W', 'W', 'L', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['L', 'L', 'W', 'W', 'W'],
];

"""

def minimum_islands(grid) -> int:
  visited = set()
  minimum_island_size = float('inf')

  for row in range(0, len(grid)):
    for column in range(0, len(grid[row])):
      size = island_size(grid, row, column, visited)
      #print(size, minimum_island_size)
      if size > 0 and size < minimum_island_size:
        minimum_island_size = size

  return minimum_island_size

def island_size(grid, row, column, visited) -> int:
  rowInbound = row >=0 and row < len(grid)
  columnInbound = column >=0 and column < len(grid[0])
  
  if not rowInbound or not columnInbound:
    return 0
  
  if grid[row][column] == 'W':
    return 0
  
  if (row, column) in visited:
    return 0
  
  size = 1
  visited.add((row, column))

  size+=island_size(grid, row + 1, column, visited)
  size+=island_size(grid, row - 1, column, visited)
  size+=island_size(grid, row, column + 1, visited)
  size+=island_size(grid, row, column - 1, visited)

  return size


grid = [
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'W', 'W', 'L', 'W'],
  ['W', 'W', 'L', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['L', 'L', 'W', 'W', 'W'],
]

print(minimum_islands(grid))

grid = [
  ['L', 'W', 'W', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['W', 'L', 'W', 'L', 'W'],
  ['W', 'W', 'W', 'W', 'W'],
  ['W', 'W', 'L', 'L', 'L'],
]

print(minimum_islands(grid))

grid = [
  ['L', 'L', 'L'],
  ['L', 'L', 'L'],
  ['L', 'L', 'L'],
]

print(minimum_islands(grid))

grid = [
  ['W', 'W'],
  ['L', 'L'],
  ['W', 'W'],
  ['W', 'L']
]

print(minimum_islands(grid))