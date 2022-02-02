"""
Merge two sorted lists
"""
class Node():
  def __init__(self, val:int):
    self.val = val
    self.next = None

def mergeTwoSortedLinkedLists(list1, list2):
  if not list1: return list2
  elif not list2: return list1
  elif list1.val < list2.val:
    list1.next = mergeTwoSortedLinkedLists(list1.next, list2)
    return list1
  else:
    list2.next = mergeTwoSortedLinkedLists(list1, list2.next)
    return list2

def printList(list1):
  if not list1: return
  print(list1.val, end="->")
  printList(list1.next);

a1 = Node(1)
a2 = Node(2)
a3 = Node(4)
a4 = Node(5)
a5 = Node(6)
a1.next = a2
a2.next = a3
a3.next = a4
a4.next = a5
b1 = Node(1)
b2 = Node(3)
b3 = Node(4)
b1.next = b2
b2.next = b3
printList(mergeTwoSortedLinkedLists(a1, b1))