"""
Linked Lists - sum of values
"""
class Node():
  def __init__(self, val):
    self.val = val
    self.next = None

def list_find(head: Node, target:int) -> bool:  
  if not head: return False
  #print(head.val)
  return head.val == target or list_find(head.next, target)


a = Node(1)
b = Node(10)
c = Node(12)
d = Node(13)
e = Node(-21)
f = Node(45)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

print(list_find(a,-21))
