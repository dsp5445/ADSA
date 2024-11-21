class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, node):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
                node.left.parent = node
            else:
                self._insert(value, node.left)
        elif value > node.value:
            if node.right is None:
                node.right = Node(value)
                node.right.parent = node
            else:
                self._insert(value, node.right)

    def print_tree(self):
        self._print_tree(self.root)

    def _print_tree(self, node):
        if node:
            self._print_tree(node.left)
            print(node.value,end=" ")
            self._print_tree(node.right)

    def height(self):
        return self._height(self.root) if self.root else 0

    def _height(self, node):
        if node is None:
            return 0
        return max(self._height(node.left), self._height(node.right)) + 1

    def find(self, value):
        return self._find(value, self.root) if self.root else None

    def _find(self, value, node):
        if node is None or node.value == value:
            return node
        elif value < node.value:
            return self._find(value, node.left)
        else:
            return self._find(value, node.right)

    def delete_value(self, value):
        node = self.find(value)
        if node:
            self._delete_node(node)

    def _delete_node(self, node):
        if node is None:
            return
        parent = node.parent
        if node.left is None and node.right is None:  # No children
            if parent:
                if parent.left == node:
                    parent.left = None
                else:
                    parent.right = None
            else:
                self.root = None
        elif node.left is None or node.right is None:  # One child
            child = node.left if node.left else node.right
            if parent:
                if parent.left == node:
                    parent.left = child
                else:
                    parent.right = child
            else:
                self.root = child
            child.parent = parent
        else:  # Two children
            successor = self._min_value_node(node.right)
            node.value = successor.value
            self._delete_node(successor)

    def _min_value_node(self, node):
        while node.left:
            node = node.left
        return node

    def search(self, value):
        return self._search(value, self.root) if self.root else False

    def _search(self, value, node):
        if node is None:
            return False
        if value == node.value:
            return True
        elif value < node.value:
            return self._search(value, node.left)
        else:
            return self._search(value, node.right)
bst = BinarySearchTree()

bst.insert(50)
bst.insert(30)
bst.insert(20)
bst.insert(40)
bst.insert(70)
bst.insert(60)
bst.insert(80)

bst.print_tree()

print(bst.search(40))
bst.delete_value(20)
bst.print_tree()
