class UserGraph():
  def __init__(self, edges) -> None: 
    self.graph = dict
    self.add_edges(edges)
    
  def add_edges(self, edges) -> None:
    self.graph = edges

  def get_edges(self) -> None:
    edges = []
    for key in self.graph.keys():
      edges.append((key, self.graph[key]))
    return edges

  def get_nodes(self) -> list:

    return list(self.graph.keys())

  def get_neighbors(self) -> dict:
    return self.graph