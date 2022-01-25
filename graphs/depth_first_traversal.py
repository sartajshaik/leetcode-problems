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

def depthFirstTraversalIterative(graph, source):
  stack = [source]
  while len(stack) > 0:
    current = stack.pop()
    print(current)
    for node in graph[current]:
      stack.append(node)

def depthFirstTraversal(graph, source):
  print(source)
  for node in graph[source]:
    depthFirstTraversal(graph, node)

adjustancylist = {
  'a':['b','c'],
  'b':['d'],
  'c':['e'],
  'd':['f'],
  'e':[],
  'f':[]
}

depthFirstTraversalIterative(adjustancylist, 'a')
print("############")
depthFirstTraversal(adjustancylist,'a')
    