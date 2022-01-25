"""
tree includes
Write a function, tree_includes, that takes in the root of a binary tree and a target value. The function should return a boolean indicating whether or not the value is contained in the tree.
"""
class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

def tree_includes(root, value) -> bool:
  if root == None: return False
  if root.value == value:
    return True
  return tree_includes(root.left, value) or tree_includes(root.right, value)

def tree_includes_breadth_first_traversal(root, value):
  if root == None: return False
  queue = [root]  
  while len(queue) > 0:
    current = queue.pop(0)
    if current.value == value:
      return True
    if current.left: queue.append(current.left)
    if current.right: queue.append(current.right)
    
  return False
  



a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

print(f.left)
print(f.right)
if a.left: print("there is something")
print(a.right)

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f

print(tree_includes(a, "e")) # -> True
print(tree_includes_breadth_first_traversal(a, "e")) # -> True