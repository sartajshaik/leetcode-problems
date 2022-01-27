"""
Linked Lists
"""
class Node():
  def __init__(self, val):
    self.val = val
    self.next = None

def print_list(head):
  current = head
  while current is not None:
    print(current.val, end="->")
    current = current.next
  print()

def linkedlist_reversal_iterative(head):
  prev = None
  current = head
  while current is not None:
    temp = current.next
    current.next = prev
    prev = current
    current = temp
  return prev

def linkedlist_reversal_recurrsive(head:Node, prev:Node = None) -> Node:
  if not head: return prev
  next = head.next
  head.next = prev
  return linkedlist_reversal_recurrsive(next, head)


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

#linkedlist_traversal_iterative(a)
#print_list(linkedlist_reversal_iterative(a))
print_list(linkedlist_reversal_recurrsive(a))
#linkedlist_traversal_recursive(a)
