"""
Linked Lists - sum of values
"""
class Node():
  def __init__(self, val):
    self.val = val
    self.next = None

def sum_of_linkedlist_values(head: Node) -> int:
  if head is None: return 0
  return head.val + sum_of_linkedlist_values(head.next)

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

print(sum_of_linkedlist_values(a))