import math


class Graph:
    def __init__(self, n):
        self.graph_matrix = [[0] * n for _ in range(n)]  # Adjacency matrix
        self.graph_list = [[] for _ in range(n)]  # Adjacency list
        self.n = n
        self.distances = [[math.inf] * n for _ in range(n)]

    def add(self, u, v, w):
        # Return if u or v is out of range
        if u >= self.n or v >= self.n:
            return

        self.graph_matrix[u][v] = w

        if v not in self.graph_list[u]:
            self.graph_list[u].append(v)

    def remove(self, u, v):
        self.graph_matrix[u][v] = 0

        if v in self.graph_list[u]:
            self.graph_list[u].remove(v)

    def all_paths(self):
        # Initialize distance matrix
        self.initialize_distances()

        # Floyd-Warshall algorithm
        self.floyd()

        # Replace 'inf' with -1 for non-reachable vertices
        self.replace_inf()

        return self.distances

    # Initialize distance matrix
    def initialize_distances(self):
        self.distances = [[math.inf] * self.n for _ in range(self.n)]
        for i in range(self.n):
            self.distances[i][i] = 0
        for u in range(self.n):
            for v in self.graph_list[u]:
                self.distances[u][v] = self.weight(u, v)

    # Floyd-Warshall algorithm
    def floyd(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.weight(i, j) != 0:
                    self.distances[i][j] = self.weight(i, j)

        for k in range(self.n):
            for i in range(self.n):
                for j in range(self.n):
                    if (self.distances[i][k] != math.inf and self.distances[k][j] != math.inf and self.distances[i][j] > self.distances[i][k] + self.distances[k][j]):
                        self.distances[i][j] = self.distances[i][k] + self.distances[k][j]

    # Return weight of edge (u, v)
    def weight(self, u, v):
        return self.graph_matrix[u][v]

    # Replace 'inf' with -1 for non-reachable vertices
    def replace_inf(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.distances[i][j] == math.inf:
                    self.distances[i][j] = -1


if __name__ == "__main__":
    graph = Graph(6)
    edges = ((0, 2, 7), (0, 4, 9), (2, 1, 5),
             (2, 3, 1), (2, 5, 2), (3, 0, 6),
             (3, 5, 2), (4, 5, 1), (5, 1, 6))
    for u, v, w in edges:
        graph.add(u, v, w)

    M = graph.all_paths()
    for weights in M:
        for weight in weights:
            print(f"{weight:3d}", end="")
        print()
    #  0 12  7  8  9  9
    # -1  0 -1 -1 -1 -1
    #  7  5  0  1 16  2
    #  6  8 13  0 15  2
    # -1  7 -1 -1  0  1
    # -1  6 -1 -1 -1  0
