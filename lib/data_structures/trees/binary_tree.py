class BinaryTree(object):
    def __init__(self, key):
        self.__rootKey = key
        self.__leftChild = None
        self.__rightChild = None

    def insert_left_child(self, node):
        if self.__leftChild is None:
            self.__leftChild = BinaryTree(node)
        else:
            branch = BinaryTree(node)
            branch.__leftChild = self.__leftChild
            self.__leftChild = branch

    def insert_right_child(self, node):
        if self.__rightChild is None:
            self.__rightChild = BinaryTree(node)
        else:
            branch = BinaryTree(node)
            branch.__rightChild = self.__rightChild
            self.__rightChild = branch

    def get_left_child(self):
        return self.__leftChild

    def get_right_child(self):
        return self.__rightChild

    def set_root_key(self, rootKey):
        self.__rootKey = rootKey

    def get_root_key(self):
        return self.__rootKey

    def __repr__(self):
        return str(self.traverse_preorder(self))

    def traverse_preorder(self, tree):
        items = [tree.get_root_key()]

        left = tree.get_left_child()
        right = tree.get_right_child()

        if left:
            items.append(self.traverse_preorder(left))
        if right:
            items.append(self.traverse_preorder(right))

        return items

    def traverse_inorder(self, tree):
        left = tree.get_left_child()
        right = tree.get_right_child()
        items = []

        if left:
            items.append(self.traverse_inorder(left))

        items.append(tree.get_root_key())

        if right:
            items.append(self.traverse_inorder(right))

        return items

    def traverse_postorder(self, tree):
        left = tree.get_left_child()
        right = tree.get_right_child()
        items = []

        if left:
            items.append(self.traverse_postorder(left))
        if right:
            items.append(self.traverse_postorder(right))

        items.append(tree.get_root_key())
        return items