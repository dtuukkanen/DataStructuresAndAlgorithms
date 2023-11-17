from enum import Enum


class Visited(Enum):
    UNVISITED = False
    VISITED = True


class Queue:
    def __init__(self, size):
        self.queue = [] * size

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

        try:
            self.graph_list[u].remove(v)
            self.graph_list[v].remove(u)
        except ValueError:
            pass

    def dft(self, start):
        for v in range(self.node_count()):  # Initialize
            self.set_value(v, Visited.UNVISITED)
        for v in range(self.node_count()):  # Traverse
            if self.get_value(v) != Visited.VISITED:
                self.dft_helper(v)
        print()

    def bft(self, start):
        for v in range(self.node_count()):  # Initialize
            self.set_value(v, Visited.UNVISITED)
        for v in range(self.node_count()):  # Traverse
            if self.get_value(v) != Visited.VISITED:
                self.bft_helper(v)
        print()

    # Helper methods
    def dft_helper(self, v):
        self.pre_visit(v)
        self.set_value(v, Visited.VISITED)
        for n in self.neighbors(v):
            if self.get_value(n) != Visited.VISITED:
                self.dft_helper(n)
        self.post_visit(v)

    def bft_helper(self, v):
        Q = Queue(self.node_count())
        Q.enqueue(v)
        self.set_value(v, Visited.VISITED)
        while Q.length() > 0:
            v = Q.dequeue()
            self.pre_visit(v)
            for n in self.neighbors(v):
                if self.get_value(n) != Visited.VISITED:
                    Q.enqueue(n)
                    self.set_value(n, Visited.VISITED)
            self.post_visit(v)

    # Visit methods
    def pre_visit(self, v):
        print(v, end=' ')
        # self.set_value(v, Visited.UNVISITED)

    def post_visit(self, v):
        # self.set_value(v, Visited.VISITED)
        # print(v, end=' ')
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

    # Debuggers
    def print_matrix(self):
        for row in self.graph_matrix:
            print(row)
        print()

    def does_edge_exist(self, u, v):
        return self.graph_matrix[u][v] == 1


if __name__ == "__main__":
    graph = Graph(6)
    edges = ((0, 2), (0, 4), (2, 1),
             (2, 3), (2, 5), (3, 0),
             (3, 5), (4, 5), (5, 1))
    for u, v in edges:
        graph.add(u, v)
        graph.print_matrix()

    graph.dft(0)           # 0 2 1 5 3 4
    graph.bft(0)           # 0 2 3 4 1 5

    graph.remove(0, 2)
    graph.remove(2, 5)
    graph.remove(1, 4)

    graph.dft(0)           # 0 3 2 1 5 4
    graph.bft(0)           # 0 3 4 2 5 1
