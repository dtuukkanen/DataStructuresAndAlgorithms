import math
from enum import Enum


class Visited(Enum):
    UNVISITED = False
    VISITED = True


class Graph:
    def __init__(self, n):
        self.graph_matrix = [[math.inf] *
                             n for _ in range(n)]  # Adjacency matrix
        self.graph_list = [[] for _ in range(n)]  # Adjacency list
        self.visited = [Visited.UNVISITED] * n
        self.n = n

    def add(self, u, v, w):
        # Return if u or v is out of range
        if u >= self.n or v >= self.n:
            return

        self.graph_matrix[u][v] = w
        self.graph_matrix[v][u] = w

        if v not in self.graph_list[u]:
            self.graph_list[u].append(v)
        if u not in self.graph_list[v]:
            self.graph_list[v].append(u)

    def remove(self, u, v):
        # Return if u or v is out of range
        if u >= self.n or v >= self.n:
            return

        self.graph_matrix[u][v] = math.inf
        self.graph_matrix[v][u] = math.inf

        if v in self.graph_list[u] and u in self.graph_list[v]:
            self.graph_list[u].remove(v)
            self.graph_list[v].remove(u)

    def min_expense(self):
        total_cost = 0

        mcst = self.prim(0)
        # Count sum of weights in key
        for weight in mcst:
            if weight != math.inf:  # Ignore unreachable vertices
                total_cost += weight

        return total_cost

    def prim(self, s):
        D = [math.inf] * self.n  # Initialize
        self.visited = [Visited.UNVISITED] * self.n  # Reset visited status

        D[s] = 0  # Start from the first vertex
        for i in range(self.n):
            v = self._min_vertex(D)
            self.visited[v] = Visited.VISITED
            for w in range(self.n):
                if D[w] > self.graph_matrix[v][w] and self.graph_matrix[v][w] != math.inf and self.visited[w] == Visited.UNVISITED:
                    D[w] = self.graph_matrix[v][w]

        return D

    def _min_vertex(self, D):
        min_value = math.inf
        min_index = -1

        for i in range(self.n):
            if D[i] < min_value and self.visited[i] == Visited.UNVISITED:
                min_value = D[i]
                min_index = i

        return min_index


if __name__ == "__main__":
    graph = Graph(6)
    edges = ((0, 2, 7), (0, 4, 9), (2, 1, 5),
             (2, 3, 1), (2, 5, 2), (3, 0, 6),
             (3, 5, 2), (4, 5, 1), (5, 1, 6))
    for u, v, w in edges:
        graph.add(u, v, w)

    print(graph.min_expense())  # 15

    graph.remove(2, 3)

    print(graph.min_expense())  # 16
