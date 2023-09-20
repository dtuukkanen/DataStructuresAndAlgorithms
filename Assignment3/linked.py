class Node:
    def __init__(self, data=None):
        self.data = data
        self.link = None


class LinkedList:
    def __init__(self):
        self.linkedList = None

    def append(self, data):
        current = self.linkedList
        new_node = Node(data)

        # if linked list is empty
        if current is None:
            self.linkedList = new_node
        # if linked list is not empty
        else:
            # go to the end of the linked list
            while current.link is not None:
                current = current.link
            current.link = new_node

    def insert(self, data, i):
        current = self.linkedList
        new_node = Node(data)

        # if inserted at the beginning
        if i == 0:
            new_node.link = current
            self.linkedList = new_node
        else:
            # go to the i-1th node
            for j in range(i - 1):
                if current.link is None:
                    return None
                current = current.link
            next = current.link  # Save the next node
            current.link = new_node  # Insert the new node
            new_node.link = next    # Link the new node to the next node

    def delete(self, i):
        current = self.linkedList
        removed = None

        # if deleted at the beginning
        # Basically just forgets the first node
        if i == 0:
            removed = current.data
            self.linkedList = current.link
        else:
            # go to the i-1th node
            for j in range(i - 1):
                if current.link is None:
                    return None
                current = current.link
            # Forget the ith node by linking the i-1th node to the i+1th node
            if current.link is None:    # If node doesn't exist
                return None
            removed = current.link.data
            current.link = current.link.link    # Skip node in between
        return removed  # Return data from index

    def print(self):
        current = self.linkedList
        print(current.data, end='')
        while current.link != None:
            current = current.link
            print(' ->', current.data, end='')
        print()

    def index(self, data):
        current = self.linkedList
        i = 0   # Start at 0

        while current is not None:
            if current.data == data:
                return i
            current = current.link
            i += 1
        return -1

    def swap(self, i, j):
        current = self.linkedList
        swap_i = None
        swap_j = None
        bigger = None

        if i > j:
            bigger = i
        else:
            bigger = j

        for index in range(bigger + 1):
            if current is None:
                return None
            if index == i:
                swap_i = current.data
            if index == j:
                swap_j = current.data
            current = current.link

        current = self.linkedList
        for index in range(bigger + 1):
            if index == i:
                current.data = swap_j
            if index == j:
                current.data = swap_i
            current = current.link

    def isort(self):
        current = self.linkedList
        current_index = 0
        next = current.link
        next_index = 1

        while next is not None:
            if current.data > next.data:
                self.swap(current_index, next_index)
                current = self.linkedList
                current_index = 0
                next = current.link
                next_index = 1
            else:
                current = next
                current_index = next_index
                next = current.link
                next_index += 1


if __name__ == "__main__":
    L = LinkedList()
    for num in (3, 5, 2, 7, 8, 10, 6):
        L.append(num)
    L.print()   # 3 -> 5 -> 2 -> 7 -> 8 -> 10 -> 6
    L.isort()
    L.print()   # 2 -> 3 -> 5 -> 6 -> 7 -> 8 -> 10
