"""
Connected components in a undirected graph
"""
graph = {
  3: [],
  6: [4, 5, 7, 8],
  8: [6],
  7: [6],
  5: [6],
  1: [2],
  2: [1],
  12: [11]
}

def connected_components(graph) -> int:
  count = 0
  visited = set()
  for node in graph.keys():
    if(explore(graph, node, visited)):
      count+=1
  return count
  
def explore(graph, node, visited) -> bool:
  if node in visited:
    return False
  visited.add(node)
  if node in graph.keys():
    for neighbour in graph[node]:
      explore(graph, neighbour, visited)
  return True

print(connected_components(graph))
