class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

    def add_edge(self, v1, v2):
        if v1 in self.adj_list and v2 in self.adj_list:
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)  # for undirected graph

    def display(self):
        for vertex, edges in self.adj_list.items():
            print(f"{vertex} -> {edges}")

# Example usage
if __name__ == "__main__":
    g = Graph()
    for vertex in ["A", "B", "C", "D"]:
        g.add_vertex(vertex)
    g.add_edge("A", "B")
    g.add_edge("A", "C")
    g.add_edge("B", "D")
    g.display()

