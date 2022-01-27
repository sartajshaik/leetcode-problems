"""
Linked Lists - zipper list
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
# A -> B -> C -> D -> E -> F
# 1 -> 2 -> 3 -> 4 -> 5 -> 6

def zipper_list_rec(list1, list2):
  if not list1 and not list2: return None
  if not list1: return list2
  if not list2: return list1

  next1 = list1.next
  next2 = list2.next
  list1.next = list2
  list2.next = zipper_list_rec(next1, next2)

  return list1

def zipper_list_iter(list1, list2):
  tail = list1
  current1 = list1.next
  current2 = list2
  counter = 0
  while current1 and current2:
    if counter%2 == 0:
      tail.next = current2
      current2 = current2.next
    else:
      tail.next = current1
      current1 = current1.next
    counter+=1
    tail = tail.next
  if not current1: tail.next = current2
  if not current2: tail.next = current1
  return list1

a1 = Node('A')
b1 = Node('B')
c1 = Node('C')
d1 = Node('D')
e1 = Node('E')
f1 = Node('F')
a1.next = b1
b1.next = c1
c1.next = d1
d1.next = e1
e1.next = f1


a2 = Node('1')
b2 = Node('2')
c2 = Node('3')
d2 = Node('4')
e2 = Node('5')
f2 = Node('6')
a2.next = b2
b2.next = c2
c2.next = d2
d2.next = e2
e2.next = f2

#print_list(zipper_list_rec(a1, a2))
print_list(zipper_list_iter(a1, a2))