"""
Shortest path problem, given source and destination nodes
"""
edges = [
  ['w','x'],
  ['x','y'],
  ['z','y'],
  ['z','v'],
  ['w','v']
]

def create_graph(edges) -> dict:
  graph = {}
  
  for a, b in edges:
    if a not in graph.keys():
      graph[a] = []
    if b not in graph.keys():
      graph[b] = []
    graph[a].append(b)
    graph[b].append(a)
  
  #print(graph)
  return graph

def shortest_path(graph, source, destination) -> int:
  visited = {source}
  queue = [(source,0)]
  while len(queue) > 0:
    current, count = queue.pop(0)
    if current == destination:
      return count
    for neighbour in graph[current]:
      if neighbour not in visited:
        visited.add(neighbour)
        queue.append((neighbour, count+1))
  return -1

print(shortest_path(create_graph(edges), 'w', 'z'))
print(shortest_path(create_graph(edges), 'w', 'a'))