class graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v) :
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)

    def print_graph(self):
        print(self.graph)

g = graph()
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.print_graph()