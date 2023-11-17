from enum import Enum
from math import inf


class Visited(Enum):
    UNVISITED = None
    VISITED = True


class Graph:
    # Must have blocks
    def __init__(self, n):
        self.graph_matrix = [[0] * n for _ in range(n)]  # Adjacency matrix
        self.graph_list = [[] for _ in range(n)]  # Adjacency list
        self.value = [Visited.UNVISITED] * n  # Node values
        self.predecessor = [-1] * n

    def add(self, u, v, w):
        self.graph_matrix[u][v] = w
        self.graph_list[u].append(v)

    def remove(self, u, v):
        self.graph_matrix[u][v] = 0

        try:
            self.graph_list[u].remove(v)
        except ValueError:
            pass

    def shortest_path(self, start, end):
        # Initialize D
        D = [inf] * self.node_count()

        # Reset visited status
        self.value = [Visited.UNVISITED] * self.node_count()

        # Reset predecessors
        self.predecessor = [-1] * self.node_count()

        self.dijkstra(start, D)
        if D[end] == inf:
            print(-1)
        else:
            self.print_path(end)
            print()

    def dijkstra(self, start, D):
        D[start] = 0
        for _ in range(self.node_count()):  # Process the vertices
            v = self.min_vertex(D)  # Find next-closest vertex
            if v == -1:
                break  # No more vertices to process
            self.set_value(v, Visited.VISITED)
            if D[v] == inf:
                break  # Unreachable
            for w in self.neighbors(v):
                if self.value[w] == Visited.UNVISITED and D[w] > D[v] + self.weight(v, w):
                    D[w] = D[v] + self.weight(v, w)
                    self.predecessor[w] = v

    # Helper methods
    def min_vertex(self, D):
        min_dist = inf
        min_vertex = -1

        for i in range(self.node_count()):
            if self.value[i] == Visited.UNVISITED and D[i] < min_dist:
                min_dist = D[i]
                min_vertex = i
        return min_vertex

    def print_path(self, v):
        if self.predecessor[v] != -1:
            self.print_path(self.predecessor[v])
        print(v, end=" ")

    # Additional methods
    def node_count(self):
        return len(self.graph_list)

    def weight(self, u, v):
        return self.graph_matrix[u][v]

    def set_value(self, v, value):
        self.value[v] = value

    def neighbors(self, v):
        return self.graph_list[v]


if __name__ == "__main__":

    graph = Graph(10)
    edges = ((0, 1, 25), (0, 2,  6), (1, 3, 10),
             (1, 4,  3), (2, 3,  7), (2, 5, 25),
             (3, 4, 12), (3, 5, 15), (3, 6,  4),
             (3, 7, 15), (3, 8, 20), (4, 7,  2),
             (5, 8,  2), (6, 7,  8), (6, 8, 13),
             (6, 9, 15), (7, 9,  5), (8, 9,  1))
    for u, v, w in edges:
        graph.add(u, v, w)

    graph.shortest_path(0, 9)   # 0 2 3 6 7 9
    graph.remove(3, 6)
    graph.remove(5, 6)
    graph.shortest_path(0, 9)   # 0 2 3 5 8 9
