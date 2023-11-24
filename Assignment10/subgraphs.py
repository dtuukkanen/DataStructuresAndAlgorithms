class Graph:
    def __init__(self, n):
        self.graph_matrix = [[0] * n for _ in range(n)]  # Adjacency matrix
        self.graph_list = [[] for _ in range(n)]  # Adjacency list
        self.n = n

    def add(self, u, v):
        self.graph_matrix[u][v] = 1
        self.graph_matrix[v][u] = 1

        if v not in self.graph_list[u]:
            self.graph_list[u].append(v)
        if u not in self.graph_list[v]:
            self.graph_list[v].append(u)

    def remove(self, u, v):
        self.graph_matrix[u][v] = 0
        self.graph_matrix[v][u] = 0

        if v in self.graph_list[u] and u in self.graph_list[v]:
            self.graph_list[u].remove(v)
            self.graph_list[v].remove(u)

    def subgraphs(self):
        visited = [False] * self.n
        subgraphs = 0

        for v in range(self.n):
            if not visited[v]:
                self.dfs(v, visited)
                subgraphs += 1

        return subgraphs

    def dfs(self, v, visited):
        visited[v] = True

        for neighbour in self.graph_list[v]:
            if not visited[neighbour]:
                self.dfs(neighbour, visited)


if __name__ == "__main__":
    graph = Graph(6)
    edges = ((0, 4), (2, 1),
             (2, 5), (3, 0),
             (5, 1))
    for u, v in edges:
        graph.add(u, v)

    print(graph.subgraphs())  # 2

    more_connections = ((0, 2), (2, 3),
                        (3, 5), (4, 5))
    for u, v in more_connections:
        graph.add(u, v)

    print(graph.subgraphs())  # 1
