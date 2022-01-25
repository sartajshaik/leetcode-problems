"""
Write a function has_path, that takes in an object representing the adjacency list of a directed acyclic graph and two nodes (src, dest). The function should return a boolean indicating whether or not there exists a directed path between the source and destination nodes
"""
graph = {
  'f':['g','i'],
  'g':['h'],
  'h':[],
  'i':['g','k'],
  'j':['i'],
  'k':[]
}

def has_path_depth_first(graph, src, dest) -> bool: 
  if src == dest:
    return True
  
  for neighbour in graph[src]:
    if(has_path_depth_first(graph, neighbour, dest)):
      return True
  
  return False

def has_path_breadth_first(graph, src, dest) -> bool:
  queue = [src]

  while len(queue) > 0:
    current = queue.pop(0)
    if current == dest:
      return True
    for neighbour in graph[current]:
      queue.append(neighbour)
  return False

print(has_path_depth_first(graph, 'f','k'))
print(has_path_breadth_first(graph, 'f','k'))