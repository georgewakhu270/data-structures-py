class Graph:
  """this will create a simple graph datastructure"""
  def __init__(self):
    self.adj_list = {}
    
  def add_vertex(self, item):
    """this is a data point"""
    if item not in self.adj_list:
      self.adj_list[item] = []
      
  def add_edge(self, item1, item2):
    """this are connection points"""
    self.adj_list[item1].append(item2)
    self.adj_list[item2].append(item1)
  
  def bfs(self, start):
    visited = { start}
    queue = [start]
    while queue:
      vertex = queue.pop(0)
      print(vertex, end=" ")
      for neighbor in self.adj_list[vertex]:
        if neighbor not in visited:
          visited.add(neighbor)
          queue.append(neighbor)
          
  def dfs_recursive(self, start,visited=None):
    if visited is None:
      visited = set()
    visited.add(start)
    print(start, end=" ")
    
    for neighbor in self.adj_list[start]:
      if neighbor not in visited:
        self.dfs_recursive(neighbor, visited)
    
  def dfs_iterative(self, start):
    visited = set()
    stack = [start]

    while stack:
      vertex = stack.pop()
      
      if vertex not in visited:
        visited.add(vertex)
        for neighbor in reversed(self.adj_list[vertex]):
          if neighbor not in visited:
            stack.append(neighbor)
