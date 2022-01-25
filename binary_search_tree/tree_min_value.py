"""
tree min value
Write a function, tree_min_value, that takes in the root of a binary tree that contains number values. The function should return the minimum value within the tree.

You may assume that the input tree is non-empty.
"""
class Node():
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

def tree_min_value_df_rec(root):
  if root == None:
    return float('inf')
  
  return min(root.value, tree_min_value_df_rec(root.left), tree_min_value_df_rec(root.right))

def tree_min_value_df_iter(root):
  stack = [root]
  min_value = float('inf')

  while len(stack) > 0:
    current = stack.pop()
    min_value = min(current.value, min_value)
    if current.left: stack.append(current.left)
    if current.right: stack.append(current.right)
  
  return min_value

def tree_min_value_bf_iter(root) -> int:
  queue = [root]
  min_value = float('inf')

  while len(queue) > 0:
    current = queue.pop(0)
    min_value = min(current.value, min_value)
    if current.left: queue.append(current.left)
    if current.right: queue.append(current.right)
  return min_value


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
print(tree_min_value_df_rec(a)) # -> -2
print(tree_min_value_df_iter(a)) # -> -2
print(tree_min_value_bf_iter(a)) # -> -2

a = Node(5)
b = Node(11)
c = Node(3)
d = Node(4)
e = Node(14)
f = Node(12)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#       5
#    /    \
#   11     3
#  / \      \
# 4   14     12

print(tree_min_value_df_rec(a)) # -> 3
print(tree_min_value_df_iter(a)) # -> 3
print(tree_min_value_bf_iter(a)) # -> 3

a = Node(-1)
b = Node(-6)
c = Node(-5)
d = Node(-3)
e = Node(-4)
f = Node(-13)
g = Node(-2)
h = Node(-2)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g
f.right = h

#        -1
#      /   \
#    -6    -5
#   /  \     \
# -3   -4   -13
#     /       \
#    -2       -2

print(tree_min_value_df_rec(a)) # -> -13
print(tree_min_value_df_iter(a)) # -> -13
print(tree_min_value_bf_iter(a)) # -> -13

a = Node(42)

#        42

print(tree_min_value_df_rec(a)) # -> 42
print(tree_min_value_df_iter(a)) # -> 42
print(tree_min_value_bf_iter(a)) # -> 42
