"""
Linked Lists - get node value at index
"""
class Node():
  def __init__(self, val):
    self.val = val
    self.next = None

def getNodeValueAtIndex(head: Node, index: int) -> int:
  counter = 0
  current = head
  while current:
    if counter == index:
      return current.val
    current = current.next
    counter+=1
  return -1

def getNodeValueAtIndexRecursive(head: Node, index: int) -> int:
  if not head: return -1
  if index == 0: return head.val
  return getNodeValueAtIndexRecursive(head.next, index-1)


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

print(getNodeValueAtIndex(a,2))
print(getNodeValueAtIndexRecursive(a,12))
