class HashLinear:
    def __init__(self, M):
        self.M = M
        self.T = [None] * M

    # Hash retuns index of the table
    def hash(self, data):
        sum = 0
        for i in range(len(data)):
            sum += ord(data[i])
        return sum % self.M

    # Inserts data into the table
    def insert(self, data):
        counter = 0

        i = self.hash(data)
        # If the position is occupied, find the next empty position
        while self.T[i] != None:
            # If the table is full, return
            if counter == self.M:
                return
            # If the data is already in the table, return
            if self.T[i] == data:
                return
            # Else, find the next empty position
            i = (i + 1) % self.M
            counter += 1
        self.T[i] = data

    # Delete data from the table
    def delete(self, data):
        i = self.hash(data)
        while self.T[i] != None:
            if self.T[i] == data:
                self.T[i] = None
                return
            i = (i + 1) % self.M

    def print(self):
        for i in range(self.M):
            if self.T[i] != None:
                print(self.T[i], end=" ")
        print()


if __name__ == "__main__":
    table = HashLinear(10)
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
