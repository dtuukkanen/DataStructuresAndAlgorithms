# Assignment 5.1
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None
        self.mirrored = False

    # Insert
    def __inserthelp(self, node, key):
        if node is None:
            return Node(key)
        elif node.key > key:
            node.left = self.__inserthelp(node.left, key)
        elif node.key < key:
            node.right = self.__inserthelp(node.right, key)
        return node

    # Assignment 5.3
    def __inserthelpmirrored(self, node, key):
        if node is None:
            return Node(key)
        elif node.key > key:
            node.right = self.__inserthelpmirrored(node.right, key)
        elif node.key < key:
            node.left = self.__inserthelpmirrored(node.left, key)
        return node

    def insert(self, key):
        if self.mirrored:
            self.root = self.__inserthelpmirrored(self.root, key)
        else:
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

    # Assignment 5.3
    def __searchhelpmirrored(self, node, key):
        if node is None:
            return False
        elif node.key > key:
            return self.__searchhelpmirrored(node.right, key)
        elif node.key < key:
            return self.__searchhelpmirrored(node.left, key)
        return True

    def search(self, key):
        if self.mirrored:
            return self.__searchhelpmirrored(self.root, key)
        else:
            return self.__searchhelp(self.root, key)

    # Remove
    def __getmax(self, node):
        if node.right is None:
            return node.key
        return self.__getmax(node.right)

    # Assignment 5.3
    def __getmaxmirrored(self, node):
        if node.left is None:
            return node.key
        return self.__getmaxmirrored(node.left)

    def __removemax(self, node):
        if node.right is None:
            return node.left
        node.right = self.__removemax(node.right)
        return node

    # Assignment 5.3
    def __removemaxmirrored(self, node):
        if node.left is None:
            return node.right
        node.left = self.__removemaxmirrored(node.left)
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

    # Assignment 5.3
    def __removehelpmirrored(self, node, key):
        if node is None:
            return node
        elif node.key > key:
            node.right = self.__removehelpmirrored(node.right, key)
        elif node.key < key:
            node.left = self.__removehelpmirrored(node.left, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                node.key = self.__getmaxmirrored(node.right)
                node.right = self.__removemaxmirrored(node.right)
        return node

    def remove(self, key):
        if self.mirrored:
            self.root = self.__removehelpmirrored(self.root, key)
        else:
            self.root = self.__removehelp(self.root, key)

    # Printing
    def __visit(self, node):
        print(node.key, end=" ")

    def __preorder(self, node):
        if node is None:
            return
        self.__visit(node)
        self.__preorder(node.left)
        self.__preorder(node.right)

    def preorder(self):
        self.__preorder(self.root)
        print()

    # Assignment 5.2
    def __inorder(self, node):
        if node is None:
            return
        self.__inorder(node.left)
        self.__visit(node)
        self.__inorder(node.right)

    def inorder(self):
        self.__inorder(self.root)
        print()

    def __postorder(self, node):
        if node is None:
            return
        self.__postorder(node.left)
        self.__postorder(node.right)
        self.__visit(node)

    def postorder(self):
        self.__postorder(self.root)
        print()

    def __breadthfirst(self, node):
        if node is None:
            return
        queue = [node]
        while len(queue) > 0:
            node = queue.pop(0)
            self.__visit(node)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

    def breadthfirst(self):
        self.__breadthfirst(self.root)
        print()

    # Assignment 5.3
    def __mirror(self, node):
        if node is None:
            return
        self.__mirror(node.left)
        self.__mirror(node.right)
        node.left, node.right = node.right, node.left

    def mirror(self):
        self.__mirror(self.root)
        if self.mirrored:
            self.mirrored = False
        else:
            self.mirrored = True


if __name__ == "__main__":
    Tree = BST()
    keys = [5, 9, 1, 3, 7, 7, 4, 6, 2]

    for key in keys:
        Tree.insert(key)

    Tree.preorder()         # 5 1 3 2 4 9 7 6
    Tree.mirror()
    Tree.preorder()         # 5 9 7 6 1 3 4 2

    Tree.insert(8)
    Tree.remove(3)
    print(Tree.search(2))   # True
    Tree.preorder()         # 5 9 7 8 6 1 2 4
    Tree.mirror()
    Tree.preorder()         # 5 1 2 4 9 7 6 8
