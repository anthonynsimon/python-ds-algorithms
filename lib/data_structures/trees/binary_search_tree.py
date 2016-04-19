class BSTNode(object):

    def __init__(self, key, value=None, left=None, right=None, parent=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

    def is_leaf(self):
        return self.has_any_children() is False

    def is_root(self):
        return self.parent == None

    def is_left_child(self):
        if self.parent:
            return self.parent.get_left_child() == self
        return False

    def is_right_child(self):
        if self.parent:
            return self.parent.get_right_child() == self
        return False

    def has_any_children(self):
        return self.has_left_child() or self.has_right_child()

    def has_both_children(self):
        return self.has_left_child() and self.has_right_child()

    def has_left_child(self):
        return self.left is not None

    def has_right_child(self):
        return self.right is not None

    def get_left_child(self):
        if self.has_left_child():
            return self.left

    def get_right_child(self):
        if self.has_right_child():
            return self.right

    def get_parent(self):
        if not self.is_root():
            return self.parent

    def get_subtree_size(self):
        left = 0
        right = 0
        if self.has_left_child():
            left += self.get_left_child().get_subtree_size()
        if self.has_right_child():
            right += self.get_right_child().get_subtree_size()
        return 1 + left + right

    def get_subtree_height(self):
        left = 0
        right = 0
        if self.has_left_child():
            left += 1
            left += self.get_left_child().get_subtree_height()
        if self.has_right_child():
            right += 1
            right += self.get_right_child().get_subtree_height()
        return max(left, right)

    def __repr__(self):
        return "'{0}' : {1}".format(self.key,self.value)

    def __iter__(self):
        if self.has_left_child():
            yield self.left
        if self.has_right_child():
            yield self.right


class BinarySearchTree(object):

    def __init__(self):
        self.root = None
        self.count = 0

    def put(self, key, value):
        if self.root is None:
            self.root = BSTNode(key, value)
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
                        current_node.left = BSTNode(key, value, None, None, current_node)
                        done = True
                elif current_node.key < key:
                    if current_node.has_right_child():
                        current_node = current_node.get_right_child()
                    else:
                        current_node.right = BSTNode(key, value, None, None, current_node)
                        done = True
            self.count += 1

    def get(self, key):
        if key is not None:
            current_node = self.root
        done = False
        while not done:
            if current_node.key == key:
                done = True
            elif current_node.has_any_children():
                if current_node.key > key:
                    if current_node.has_left_child():
                        current_node = current_node.get_left_child()
                    else:
                        done = True
                elif current_node.key < key:
                    if current_node.has_right_child():
                        current_node = current_node.get_right_child()
                    else:
                        done = True
            else:
                done = True

        if current_node.key == key:
            return current_node
        return None

    def remove(self, key):
        node_to_remove = self.get(key)
        if node_to_remove:
            # If it has no children
            if node_to_remove.is_leaf():
                if node_to_remove == self.root:
                    self.root = None
                elif node_to_remove == node_to_remove.parent.get_left_child():
                    node_to_remove.parent.left = None
                else:
                    node_to_remove.parent.right = None

            # If it has both children
            elif node_to_remove.has_both_children():
                successor_node = self.get_successor(node_to_remove)
                temp_key = successor_node.key
                temp_value = successor_node.value
                self.remove(successor_node.key) # must clear it before changing the BST path
                node_to_remove.key = temp_key
                node_to_remove.value = temp_value

            # If it has only one child
            else:
                if node_to_remove.has_left_child():
                    left = node_to_remove.get_left_child()
                    if node_to_remove == self.root:
                        left.parent = None
                        self.root = left
                    else:
                        if node_to_remove.is_left_child():
                            node_to_remove.parent.left = left
                        elif node_to_remove.is_right_child():
                            node_to_remove.parent.right = left
                        left.parent = node_to_remove.parent
                else:
                    right = node_to_remove.get_right_child()
                    if node_to_remove == self.root:
                        right.parent = None
                        self.root = right
                    else:
                        if node_to_remove.is_left_child():
                            node_to_remove.parent.left = right
                        elif node_to_remove.is_right_child():
                            node_to_remove.parent.right = right
                        right.parent = node_to_remove.parent
            self.count -= 1

    def get_min(self):
        if self.root:
            current_node = self.root
            while current_node.has_left_child():
                current_node = current_node.get_left_child()
            return current_node

    def get_max(self):
        if self.root:
            current_node = self.root
            while current_node.has_right_child():
                current_node = current_node.get_right_child()
            return current_node

    def get_successor(self, start_node):
        successor_node = start_node.get_right_child()
        while successor_node.has_left_child():
            successor_node = successor_node.get_left_child()
        return successor_node

    def get_predecessor(self, start_node):
        predecessor = start_node.get_left_child()
        while predecessor.has_right_child():
            predecessor = predecessor.get_right_child()
        return predecessor

    def __getitem__(self, item):
        result = self.get(item)
        if result:
            return result.value

    def __setitem__(self, key, value):
        self.put(key,value)

    def __delitem__(self, key):
        self.remove(key)

    def __len__(self):
        return self.count

    def __contains__(self, key):
        if self.get(key):
            return True

    def __repr__(self):
        if self.root is not None:
            def repr_helper(node, items):
                if node:
                    if node.has_left_child():
                        repr_helper(node.get_left_child(), items)
                    items.append(node)
                    if node.has_right_child():
                        repr_helper(node.get_right_child(), items)
            items = []
            repr_helper(self.root, items)
            return str(items)
        return "[]"

    def __iter__(self):
        if self.root:
            start_node = self.root
            items = []
            self.__iterate_helper(start_node, items)
            for item in items:
                yield item

    def __iterate_helper(self, node, items):
        if node.has_left_child():
            self.__iterate_helper(node.get_left_child(), items)
        items.append(node)
        if node.has_right_child():
            self.__iterate_helper(node.get_right_child(), items)

    def visualize_horizontal(self, level=0, node=None):
        if node is None:
            node = self.root
        adder = "Root = "
        if node.is_left_child():
            adder = "Left = "
        elif node.is_right_child():
            adder = "Right = "
        print ('\t' * level + adder + repr(node))
        for child in node:
            self.visualize(level + 1, child)

    def visualize_vertical(self):
        if self.root is None: return '<empty tree>'

        def recurse(node):
            if node is None: return [], 0, 0
            label = str(node.key)
            left_lines, left_pos, left_width = recurse(node.get_left_child())
            right_lines, right_pos, right_width = recurse(node.get_right_child())
            middle = max(right_pos + left_width - left_pos + 1, len(label), 2)
            pos = left_pos + middle // 2
            width = left_pos + middle + right_width - right_pos

            while len(left_lines) < len(right_lines):
                left_lines.append(' ' * left_width)

            while len(right_lines) < len(left_lines):
                right_lines.append(' ' * right_width)

            if (middle - len(label)) % 2 == 1 and node.parent is not None and \
               node is node.parent.get_left_child() and len(label) < middle:
                label += '.'

            label = label.center(middle, '.')

            if label[0] == '.': label = ' ' + label[1:]
            if label[-1] == '.': label = label[:-1] + ' '

            lines = [' ' * left_pos + label + ' ' * (right_width - right_pos),
                     ' ' * left_pos + '/' + ' ' * (middle-2) +
                     '\\' + ' ' * (right_width - right_pos)] + \
              [left_line + ' ' * (width - left_width - right_width) +
               right_line
               for left_line, right_line in zip(left_lines, right_lines)]

            return lines, pos, width

        print("\n")
        print ('\n'.join(recurse(self.root)[0]))
        print("\n")