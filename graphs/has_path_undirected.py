"""
Undirected graph has path between source and destination
"""
edges = [['i','j'],['k','i'],['m','k'],['k','l'],['o','n']]

def undirected_graph(edges, source, dest):
  graph = build_graph(edges)
  print(has_path(graph, source, dest, set()))

def has_path(graph, source, dest, visited) -> bool:
  if source == dest:
    return True
  if source in visited:
    return False

  visited.add(source)

  for neighbour in graph[source]:
    if has_path(graph, neighbour, dest, visited):
      return True
  
  return False


def build_graph(edges) -> dict:
  graph = {}
  for nodes in edges:
    a, b = nodes[0], nodes[1]
    if a not in graph.keys():
      graph[a] = []
    if b not in graph.keys():
      graph[b] = []
    
    graph[a].append(b)
    graph[b].append(a)
  print(graph)
  return graph

undirected_graph(edges, 'l','i')
    