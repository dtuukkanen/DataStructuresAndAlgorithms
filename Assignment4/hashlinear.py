class HashLinear:
    def __init__(self, M):
        self.M = M
        self.T = [None] * M

    def hash(self, data):
        # Hash is sum of ASCII values of characters in data
        # Which is then modded by the size of the table
        sum = 0
        for i in range(len(data)):
            sum += ord(data[i])
        return sum % self.M

    def insert(self, data):
        # Find index by hashing
        index = self.hash(data)

        # Check if the index is empty or already has the data
        if self.T[index] is None or self.T[index] == data:
            self.T[index] = data

        # If not, find the next empty position
        else:
            i = 1
            done = False
            while not done:
                # Probing
                new_index = (index + i) % self.M

                # Check and make sure that table is not full
                if new_index == index:
                    done = True

                # Check if the index is empty or already has the data
                if self.T[new_index] is None or self.T[new_index] == data:
                    self.T[new_index] = data
                    done = True

                # If not, keep probing
                else:
                    i += 1

    def delete(self, data):
        # Find index by hashing
        index = self.hash(data)

        # Check if the index has the data
        if self.T[index] == data:
            self.T[index] = None

        # If not, find the next position that might have the data
        else:
            i = 1
            done = False
            while not done:
                # Probing
                new_index = (index + i) % self.M

                # End if there isn't item to be deleted
                if new_index == index:
                    done = True

                # Check if the index has the data
                # If so, delete it
                if self.T[new_index] == data:
                    self.T[new_index] = None
                    done = True

                # If not, keep probing
                else:
                    i += 1

    def print(self):
        # Print value if it is not None
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
    table.print()  # buttermilk shim cheiromegaly finebent resolvend premillennialise
    table.delete("buttermilk")
    table.delete("cores")
    table.delete("cheiromegaly")
    table.delete("iodations")
    table.print()  # shim finebent resolvend premillennialise
    table.insert("iodations")
    table.insert("tirrlie")
    table.insert("comous")
    table.insert("discursiveness")
    table.insert("flabbergasts")
    table.insert("rename")
    table.insert("softhead")
    table.print()  # iodations discursiveness comous shim tirrlie finebent flabbergasts rename resolvend premillennialise
