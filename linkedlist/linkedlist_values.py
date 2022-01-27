"""
Linked Lists
"""
class Node():
  def __init__(self, val):
    self.val = val
    self.next = None

def linkedlist_values(head) -> list:
  values = list()
  current = head
  while current is not None:
    values.append(current.val)
    current = current.next
  return values

a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')
e = Node('E')
f = Node('F')
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

print(linkedlist_values(a))