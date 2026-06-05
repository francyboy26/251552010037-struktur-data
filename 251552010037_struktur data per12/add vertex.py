class graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
    
    def print_graph(self):
        print(self.graph)

g = graph()
g.add_vertex('A')
g.add_vertex('B')
g.print_graph()