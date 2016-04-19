class BinaryTree(object):
    def __init__(self, key):
        self.__key = key
        self.__left = None
        self.__right = None

    def insert_left_child(self, node):
        if self.__left is None:
            self.__left = BinaryTree(node)
        else:
            branch = BinaryTree(node)
            branch.__left = self.__left
            self.__left = branch

    def insert_right_child(self, node):
        if self.__right is None:
            self.__right = BinaryTree(node)
        else:
            branch = BinaryTree(node)
            branch.__right = self.__right
            self.__right = branch

    def get_left_child(self):
        return self.__left

    def get_right_child(self):
        return self.__right

    def set_root_key(self, rootKey):
        self.__key = rootKey

    def get_root_key(self):
        return self.__key

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