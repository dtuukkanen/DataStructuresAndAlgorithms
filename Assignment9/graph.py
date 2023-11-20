from enum import Enum


class Visited(Enum):
    UNVISITED = False
    VISITED = True


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        return self.queue.pop(0)

    def length(self):
        return len(self.queue)


class Graph:
    # Must have blocks
    def __init__(self, n):
        self.graph_matrix = [[0] * n for _ in range(n)]  # Adjacency matrix
        self.graph_list = [[] for _ in range(n)]  # Adjacency list
        self.value = [Visited.UNVISITED] * n  # Node values

    def add(self, u, v):
        self.graph_matrix[u][v] = 1
        self.graph_matrix[v][u] = 1

        self.graph_list[u].append(v)
        self.graph_list[v].append(u)

    def remove(self, u, v):
        self.graph_matrix[u][v] = 0
        self.graph_matrix[v][u] = 0

        if v in self.graph_list[u] and u in self.graph_list[v]:
            self.graph_list[u].remove(v)
            self.graph_list[v].remove(u)

    def dft(self, start):
        for v in range(self.node_count()):  # Initialize
            self.set_value(v, Visited.UNVISITED)

        # Start at the start node
        self.dft_helper(start)
        print()

    def bft(self, start):
        for v in range(self.node_count()):  # Initialize
            self.set_value(v, Visited.UNVISITED)

        # Start at the start node
        self.bft_helper(start)
        print()

    # Helper methods
    def dft_helper(self, v):
        self.pre_visit(v)
        self.set_value(v, Visited.VISITED)
        for n in sorted(self.neighbors(v)):
            if self.get_value(n) != Visited.VISITED:
                self.dft_helper(n)
        self.post_visit(v)

    def bft_helper(self, v):
        Q = Queue()
        Q.enqueue(v)
        self.set_value(v, Visited.VISITED)
        while Q.length() > 0:
            v = Q.dequeue()
            self.pre_visit(v)
            for n in sorted(self.neighbors(v)):
                if self.get_value(n) != Visited.VISITED:
                    Q.enqueue(n)
                    self.set_value(n, Visited.VISITED)
            self.post_visit(v)

    # Visit methods
    def pre_visit(self, v):
        print(v, end=' ')

    def post_visit(self, v):
        pass

    # Additional methods
    def node_count(self):
        return len(self.graph_list)

    def set_value(self, v, value):
        self.value[v] = value

    def get_value(self, v):
        return self.value[v]

    def neighbors(self, v):
        return self.graph_list[v]


if __name__ == "__main__":
    graph = Graph(6)
    edges = ((0, 2), (0, 4), (2, 1),
             (2, 3), (2, 5), (3, 0),
             (3, 5), (4, 5), (5, 1))
    for u, v in edges:
        graph.add(u, v)

    graph.dft(0)           # 0 2 1 5 3 4
    graph.bft(0)           # 0 2 3 4 1 5

    graph.remove(0, 2)
    graph.remove(2, 5)
    graph.remove(1, 4)

    graph.dft(0)           # 0 3 2 1 5 4
    graph.bft(0)           # 0 3 4 2 5 1
