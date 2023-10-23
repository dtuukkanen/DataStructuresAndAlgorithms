import heapq


class MinHeap:

    # Initialization
    def __init__(self, list):
        self.heap = list
        heapq.heapify(self.heap)

    # Pushing
    def push(self, key):
        heapq.heappush(self.heap, key)

    def pop(self):
        return heapq.heappop(self.heap)

    def print(self):
        for key in self.heap:
            print(key, end=" ")
        print()


if __name__ == "__main__":
    heap = MinHeap([4, 8, 6, 5, 1, 2, 3])
    heap.print()        # 1 4 2 5 8 6 3
    print(heap.pop())   # 1
    heap.push(9)
    heap.print()        # 2 4 3 5 8 6 9
