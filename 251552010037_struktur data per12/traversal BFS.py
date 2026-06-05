class graph:
    def __init__(self):
        self.graph = {
            "A": ["B", "C"],
            "B": ["A", "D"],
            "C": ["A", "E"],
            "D": ["B"],
            "E": ["C"]
        }

    def bfs(self, start):
        visited = set()
        queue = [start]
        result = []

        while queue:
            v = queue.pop(0)
            if v not in visited:
                visited.add(v)
                result.append(v)
                queue.extend([n for n in self.graph[v] if n not in visited])
        return result
    
g = graph()
print("traversal BFS dari A:", g.bfs("A"))