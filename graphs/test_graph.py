from graph import Graph

if __name__ == "__main__":
    g = Graph()
    for vertex in ["X", "Y", "Z"]:
        g.add_vertex(vertex)
    g.add_edge("X", "Y")
    g.add_edge("Y", "Z")
    g.display()

