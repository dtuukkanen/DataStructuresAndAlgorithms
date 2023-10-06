class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    # Insert
    def __inserthelp(self, node, key):
        if node is None:
            return Node(key)
        elif node.key > key:
            node.left = self.__inserthelp(node.left, key)
        elif node.key < key:
            node.right = self.__inserthelp(node.right, key)
        return node

    def insert(self, key):
        self.root = self.__inserthelp(self.root, key)

    # Search
    def __searchhelp(self, node, key):
        if node is None:
            return False
        elif node.key > key:
            return self.__searchhelp(node.left, key)
        elif node.key < key:
            return self.__searchhelp(node.right, key)
        return True

    def search(self, key):
        return self.__searchhelp(self.root, key)

    # Remove
    def __getmax(self, node):
        if node.right is None:
            return node.key
        return self.__getmax(node.right)

    def __removemax(self, node):
        if node.right is None:
            return node.left
        node.right = self.__removemax(node.right)
        return node

    def __removehelp(self, node, key):
        if node is None:
            return node
        elif node.key > key:
            node.left = self.__removehelp(node.left, key)
        elif node.key < key:
            node.right = self.__removehelp(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                node.key = self.__getmax(node.left)
                node.left = self.__removemax(node.left)
        return node

    def remove(self, key):
        self.root = self.__removehelp(self.root, key)

    # Printing
    def __preorder(self, node):
        if node is None:
            return
        print(node.key, end=" ")
        self.__preorder(node.left)
        self.__preorder(node.right)

    def preorder(self):
        self.__preorder(self.root)
        print()


if __name__ == "__main__":
    Tree = BST()
    keys = [5, 9, 1, 3, 7, 7, 4, 6, 2]

    for key in keys:
        Tree.insert(key)

    Tree.preorder()         # 5 1 3 2 4 9 7 6

    print(Tree.search(6))   # True
    print(Tree.search(8))   # False

    Tree.remove(1)
    Tree.preorder()         # 5 3 2 4 9 7 6
    Tree.remove(9)
    Tree.preorder()         # 5 3 2 4 7 6
    Tree.remove(3)
    Tree.preorder()         # 5 2 4 7 6
