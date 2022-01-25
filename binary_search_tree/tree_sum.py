"""
tree sum
Write a function, tree_sum, that takes in the root of a binary tree that contains number values. The function should return the total sum of all values in the tree.
"""
class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None
  
def tree_sum(root) -> int:
  if root == None: return 0
  return root.value+tree_sum(root.left)+tree_sum(root.right)

def tree_sum_iterative(root) -> int:
  if root == None:
    return 0
  stack = [root]
  total = 0
  while len(stack) > 0:
    current = stack.pop()
    total+=current.value
    if current.right: stack.append(current.right)
    if current.left: stack.append(current.left)
  return total

a = Node(3)
b = Node(11)
c = Node(4)
d = Node(4)
e = Node(-2)
f = Node(1)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#       3
#    /    \
#   11     4
#  / \      \
# 4   -2     1

print(tree_sum(a)) # -> 21


a = Node(1)
b = Node(6)
c = Node(0)
d = Node(3)
e = Node(-6)
f = Node(2)
g = Node(2)
h = Node(2)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g
f.right = h

#      1
#    /   \
#   6     0
#  / \     \
# 3   -6    2
#    /       \
#   2         2

print(tree_sum_iterative(a)) # -> 10