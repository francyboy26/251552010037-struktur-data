from tracemalloc import start


class graph:
    def __init__(self):
        self.graph = {
            "A": ["B", "C"],
            "B": ["A"],
            "C": ["B"]
        }
    def search(self, start, target):
         visited = set ()
         def dfs(v):
             if v == target:
                return True
                visited.add(v)
                for neighbor in self.graph.get(v, []):
                    if neighbor not in visited:
                        if dfs(neighbor):
                            return True
                return False
                return dfs(start)
             
g = graph()
print("A ke C?", g.search("A", "C"))
print("A ke D?", g.search("A", "D"))