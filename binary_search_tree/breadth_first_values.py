"""
breadth first values
Write a function, breadth_first_values, that takes in the root of a binary tree. The function should return a list containing all values of the tree in breadth-first order.
"""

class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

def breadth_first_values(root):
  queue = [root]
  result = []
  while len(queue) > 0:
    current = queue.pop(0)
    if current == None:
      continue
    result.append(current.value)
    queue.append(current.left)
    queue.append(current.right)
  print(result)
  

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

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f

breadth_first_values(a) 
#    -> ['a', 'b', 'c', 'd', 'e', 'f']
#test_01:
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')
h = Node('h')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g
f.right = h

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f
#    /       \
#   g         h

breadth_first_values(a) 
#   -> ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
#test_02:
a = Node('a')

#      a

breadth_first_values(a) 
#    -> ['a']
#test_03:
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
x = Node('x')

a.right = b
b.left = c
c.left = x
c.right = d
d.right = e

#      a
#       \
#        b
#       /
#      c
#    /  \
#   x    d
#         \
#          e

breadth_first_values(a) 
#    -> ['a', 'b', 'c', 'x', 'd', 'e']
#test_04:
breadth_first_values(None) 
#    -> []