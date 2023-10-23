# I used heapq library as part of the solution to this assignment.
# https://github.com/python/cpython/blob/3.12/Lib/heapq.py#L275

class MinHeap:

    # Initialization
    def __init__(self, list):
        self.heap = self.__heapify(list)

    def __heapify(self, list):
        length = len(list)
        for i in reversed(range(length // 2)):
            self.__siftup(list, i)
        return list

    def __siftup(self, heap, pos):
        endpos = len(heap)
        startpos = pos
        newitem = heap[pos]
        # Bubble up the smaller child until hitting a leaf.
        childpos = 2*pos + 1    # leftmost child position
        while childpos < endpos:
            # Set childpos to index of smaller child.
            rightpos = childpos + 1
            if rightpos < endpos and not heap[childpos] < heap[rightpos]:
                childpos = rightpos
            # Move the smaller child up.
            heap[pos] = heap[childpos]
            pos = childpos
            childpos = 2*pos + 1
        # The leaf at pos is empty now.  Put newitem there, and bubble it up
        # to its final resting place (by sifting its parents down).
        heap[pos] = newitem
        self.__siftdown(heap, startpos, pos)

    def __siftdown(self, heap, startpos, pos):
        newitem = heap[pos]
        # Follow the path to the root, moving parents down until finding a place
        # newitem fits.
        while pos > startpos:
            parentpos = (pos - 1) >> 1
            parent = heap[parentpos]
            if newitem < parent:
                heap[pos] = parent
                pos = parentpos
                continue
            break
        heap[pos] = newitem

    # Pushing
    def push(self, key):
        self.heap.append(key)
        self.__siftdown(self.heap, 0, len(self.heap) - 1)

    def pop(self):
        lastelt = self.heap.pop()
        if self.heap:
            returnitem = self.heap[0]
            self.heap[0] = lastelt
            self.__siftup(self.heap, 0)
            return returnitem
        return lastelt

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
