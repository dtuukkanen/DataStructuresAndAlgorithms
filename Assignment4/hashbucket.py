class HashBucket:
    def __init__(self, M, B):
        self.M = M
        self.B = B
        self.T = [None] * M
        self.overflow = [None] * M

    def hash(self, data):
        # Hash is sum of ASCII values of characters in data
        # Which is then modded by the size of the table
        sum = 0
        for i in range(len(data)):
            sum += ord(data[i])
        return sum % self.B

    def insert(self, data):
        bucket = self.hash(data)

        # Create index
        index = bucket * (self.M // self.B)

        for i in range(index, index + (self.M // self.B)):
            # Check if the index is empty or already has the data
            if self.T[i] is None or self.T[i] == data:
                self.T[i] = data
                return

        # If not, use overflow
        else:
            for i in range(self.M - 1, -1, -1):
                if self.overflow[i] is None or self.overflow[i] == data:
                    self.overflow[i] = data
                    return

    def delete(self, data):
        bucket = self.hash(data)

        # Create index
        index = bucket * (self.M // self.B)

        for i in range(index, index + (self.M // self.B)):
            # Check if the index has the data
            if self.T[i] == data:
                self.T[i] = None
                return

        # If not, find the next position that might have the data
        else:
            # If not, check overflow
            overflow_index = None

            # Search for data in overflow
            # And save the index if found
            for i in range(self.M):
                # Search for data in overflow
                if self.overflow[i] == data:
                    overflow_index = i
                    break

            # If data is found, delete it
            if overflow_index is not None:
                for i in range(overflow_index, 0, -1):
                    self.overflow[i] = self.overflow[i - 1]
                self.overflow[0] = None

    def print(self):
        # Hashtable
        for i in range(self.M):
            if self.T[i] is not None:
                print(self.T[i], end=" ")

        # Overflow
        for i in range(self.M - 1, -1, -1):
            if self.overflow[i] is not None:
                print(self.overflow[i], end=" ")
        print()


if __name__ == "__main__":
    table = HashBucket(10, 5)
    table.insert("buttermilk")
    table.insert("shim")
    table.insert("resolvend")
    table.insert("cheiromegaly")
    table.insert("premillennialise")
    table.insert("finebent")
    table.print()
    table.delete("buttermilk")
    table.delete("cores")
    table.delete("cheiromegaly")
    table.delete("iodations")
    table.print()
    table.insert("iodations")
    table.insert("tirrlie")
    table.insert("comous")
    table.insert("discursiveness")
    table.insert("flabbergasts")
    table.insert("rename")
    table.insert("softhead")
    table.print()
