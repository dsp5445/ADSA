lass Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        if not node:
            return 0
        return node.height

    def balance_factor(self, node):
        if not node:
            return 0
        return self.height(node.left) - self.height(node.right)

    def rotate_left(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = max(self.height(z.left), self.height(z.right)) + 1
        y.height = max(self.height(y.left), self.height(y.right)) + 1
        return y

    def rotate_right(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = max(self.height(z.left), self.height(z.right)) + 1
        y.height = max(self.height(y.left), self.height(y.right)) + 1
        return y

    def insert(self, root, key):
        if not root:
            return Node(key)

        if key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = max(self.height(root.left), self.height(root.right)) + 1

        balance = self.balance_factor(root)

        if balance > 1 and key < root.left.key:
            return self.rotate_right(root)

        if balance < -1 and key > root.right.key:
            return self.rotate_left(root)

        if balance > 1 and key > root.left.key:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)

        if balance < -1 and key < root.right.key:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

    def preorder(self, root):
        if root:
            print(root.key, end=' ')
            self.preorder(root.left)
            self.preorder(root.right)

    def insert_key(self, key):
        self.root = self.insert(self.root, key)

    def print_preorder(self):
        self.preorder(self.root)
        print()

avl = AVLTree()
keys = [50, 30, 20, 40, 70, 60, 80]
for key in keys:
    avl.insert_key(key)

print("Preorder traversal of the AVL tree is:")
avl.print_preorder()
