class graph:
    def __init__(self):
        self.graph = {
            "A": ["B", "C"],
            "B": ["A"],
            "C": ["A"]
        }
    
    def remove_vertex(self, vertex):
        if vertex in self.graph:
            self.graph.pop(vertex)
            for v in self.graph:
                if vertex in self.graph[v]:
                    self.graph[v].remove(vertex)

    def print_graph(self):
        print(self.graph)


g = graph()
g.remove_vertex('A')
g.print_graph()