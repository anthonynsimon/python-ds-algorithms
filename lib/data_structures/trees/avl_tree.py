from lib.data_structures.trees.binary_search_tree import BSTNode, BinarySearchTree


class AVLNode(BSTNode):
    def get_balance_factor(self):
        left = 0
        right = 0
        if self.has_left_child():
            left = self.get_left_child().get_subtree_height() + 1
        if self.has_right_child():
            right = self.get_right_child().get_subtree_height() + 1
        return left - right


class AVLTree(BinarySearchTree):

    def __init__(self):
        super(AVLTree, self).__init__()

    def put(self, key, value):
        if self.root is None:
            self.root = AVLNode(key, value)
            self.count = 1
        else:
            current_node = self.root
            done = False
            while not done:
                if current_node.key == key:
                    current_node.value = value
                    done = True
                elif current_node.key > key:
                    if current_node.has_left_child():
                        current_node = current_node.get_left_child()
                    else:
                        current_node.left = AVLNode(key, value, None, None, current_node)
                        done = True
                elif current_node.key < key:
                    if current_node.has_right_child():
                        current_node = current_node.get_right_child()
                    else:
                        current_node.right = AVLNode(key, value, None, None, current_node)
                        done = True
            self.count += 1
            self.rebalance(current_node)

    def remove(self, key):
        current_node = self.get(key)
        if current_node:
            rebalance_node = None

            # If it has no children
            if current_node.is_leaf():
                if current_node.is_root():
                    self.root = None
                else:
                    rebalance_node = current_node.get_parent()
                    if current_node == current_node.parent.get_left_child():
                        current_node.get_parent().left = None
                    else:
                        current_node.get_parent().right = None

            # If it has both children
            elif current_node.has_both_children():
                successor_node = self.get_successor(current_node)
                rebalance_node = successor_node.get_parent()
                temp_key = successor_node.key
                temp_value = successor_node.value
                self.remove(successor_node.key) # must clear it before changing the BST path
                current_node.key = temp_key
                current_node.value = temp_value

            # If it has only one child
            else:
                if current_node.has_left_child():
                    left_node = current_node.get_left_child()
                    rebalance_node = left_node
                    if current_node == self.root:
                        left_node.parent = None
                        self.root = left_node
                    else:
                        if current_node.is_left_child():
                            current_node.parent.left = left_node
                        elif current_node.is_right_child():
                            current_node.parent.right = left_node
                        left_node.parent = current_node.parent
                else:
                    right_node = current_node.get_right_child()
                    rebalance_node = right_node
                    if current_node == self.root:
                        right_node.parent = None
                        self.root = right_node
                    else:
                        if current_node.is_left_child():
                            current_node.parent.left = right_node
                        elif current_node.is_right_child():
                            current_node.parent.right = right_node
                        right_node.parent = current_node.parent
            self.count -= 1
            if rebalance_node:
                self.rebalance(rebalance_node)

    def check_balance_top_down(self, node):
        if node:
            if abs(node.get_balance_factor()) > 1:
                self.rebalance(node)
            elif node.has_any_children():
                self.check_balance_top_down(node.get_left_child())
                self.check_balance_top_down(node.get_right_child())

    def rebalance(self, node):
        #self.visualizeVertical()
        while node is not None:
            # it's right-heavy
            if node.get_balance_factor() < -1:
                if node.has_right_child() and node.get_right_child().get_balance_factor() > 0:
                    self.rotate_right(node.get_right_child())
                self.rotate_left(node)

            # it's left-heavy
            elif node.get_balance_factor() > 1:
                if node.has_left_child() and node.get_left_child().get_balance_factor() < 0:
                    self.rotate_left(node.get_left_child())
                self.rotate_right(node)
            node = node.get_parent()

    def rotate_right(self, node):
        old_node = node
        new_node = node.get_left_child()

        new_node.parent = old_node.get_parent()
        if old_node.get_parent():
            if old_node.is_left_child():
                old_node.get_parent().left = new_node
            else:
                old_node.get_parent().right = new_node
        else:
            self.root = new_node

        old_node.parent = new_node
        old_node.left = new_node.get_right_child()
        if old_node.has_left_child():
            old_node.get_left_child().parent = old_node
        new_node.right = old_node
        #self.visualizeVertical()

    def rotate_left(self, node):
        old_node = node
        new_node = node.get_right_child()

        new_node.parent = old_node.get_parent()
        if new_node.get_parent():
            if old_node.is_left_child():
                old_node.get_parent().left = new_node
            else:
                old_node.get_parent().right = new_node
        else:
            self.root = new_node

        old_node.parent = new_node
        old_node.right = new_node.get_left_child()
        if old_node.has_right_child():
            old_node.get_right_child().parent = old_node
        new_node.left = old_node
        #self.visualizeVertical()