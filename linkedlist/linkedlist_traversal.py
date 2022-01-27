"""
Linked Lists
"""
class Node():
  def __init__(self, val):
    self.val = val
    self.next = None

def linkedlist_traversal_iterative(head):
  current = head
  while current is not None:
    print(current.val, end="->")
    current = current.next
  print()

def linkedlist_traversal_recursive(head):
  if head is None:
    return
  linkedlist_traversal_recursive(head.next)
  print(head.val, end="->")


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

linkedlist_traversal_iterative(a)
linkedlist_traversal_recursive(a)
