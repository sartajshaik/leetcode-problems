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
"""
depth first values
Write a function, depth_first_values, that takes in the root of a binary tree. The function should return a list containing all values of the tree in depth-first order.

Hey. This is our first binary tree problem, so you should be liberal with watching the Approach and Walkthrough. Be productive, not stubborn. -AZ
"""

class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

def depth_first_values(root) -> list:
  if root == None:
    return []
  
  return [root.value] + depth_first_values(root.left) + depth_first_values(root.right)

def depth_first_values_iterative(root):
  stack = [root]

  while len(stack) > 0:
    current = stack.pop()
    print(current.value)
    if current.right != None:
      stack.append(current.right)
    if current.left != None:
      stack.append(current.left)
  

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')        
a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

print(depth_first_values(a))
print("########")
depth_first_values_iterative(a)


a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')
a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f
#    /
#   g

print(depth_first_values(a))
#   -> ['a', 'b', 'd', 'e', 'g', 'c', 'f']

a = Node('a')
#     a
print(depth_first_values(a))
#   -> ['a']


a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
a.right = b;
b.left = c;
c.right = d;
d.right = e;

#      a
#       \
#        b
#       /
#      c
#       \
#        d
#         \
#          e

print(depth_first_values(a))
#   -> ['a', 'b', 'c', 'd', 'e']

print(depth_first_values(None))
#   -> []