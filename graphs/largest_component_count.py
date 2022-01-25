"""
Largest component count
"""
graph = {
 0: [8, 1, 5, 7],
 1: [0],
 5: [0, 8],
 8: [0, 5],
 2: [3, 4],
 3: [2, 4],
 4: [3, 2]
}

def largest_component(graph) -> int: 
  visited = set()
  max_nodes = 0

  for node in graph.keys():
    count = explore(graph, node, visited)
    max_nodes = max(count, max_nodes)
  
  return max_nodes


def explore(graph, node, visited) -> int:
  if node in visited:
    return 0
  
  visited.add(node)
  total = 1
  if node in graph.keys():
    for neighbour in graph[node]:
      total += explore(graph, neighbour, visited)
    
  return total
    
print(largest_component(graph))