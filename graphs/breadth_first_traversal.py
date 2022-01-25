'''
Breadth first traversal
adjustancylist = {
  'a':['b','c'],
  'b':['d'],
  'c':['e'],
  'd':['f'],
  'e':[],
  'f':[]
}
'''

def breadth_first_traversal_iterative(graph, source):
  queue = [source]
  while len(queue) > 0:
    current = queue.pop(0)
    print(current)
    for neighbour in graph[current]:
      queue.append(neighbour)

def breadth_first_traversal(graph, source):
  print(source)
  for neighbour in graph[source]:
    print(neighbour)

adjustancylist = {
  'a':['c','b'],
  'b':['d'],
  'c':['e'],
  'd':['f'],
  'e':[],
  'f':[]
}

breadth_first_traversal_iterative(adjustancylist, 'a')