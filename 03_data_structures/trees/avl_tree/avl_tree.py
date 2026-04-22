
from avl_node import AVLNode

class AVLTree:

    def get_height(self, node):
        return node.height if node else 0
    def get_balance(self, node):
        return self.get_height(node.left) - self.get_height(node.right) if node else 0

    def rotate_right(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1
        x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1
        return x

    def rotate_left(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1
        return y

    def rebalance(self, node):
        balance = self.get_balance(node)
        if balance > 1:
            if self.get_balance(node.left) < 0:
                node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        if balance < -1:
            if self.get_balance(node.right) > 0:
                node.right = self.rotate_right(node.right)
            return self.rotate_left(node)
        return node

    def insert(self, root, key):
        if not root:
            return AVLNode(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        root.height = max(self.get_height(root.left), self.get_height(root.right)) + 1
        return self.rebalance(root)

    def find_min(self, node):
        while node.left:
            node = node.left
        return node

    def delete(self, root, key):
        if not root:
            return root
        elif key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            temp = self.find_min(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)
        root.height = max(self.get_height(root.left), self.get_height(root.right)) + 1
        return self.rebalance(root)

    # function to print the tree in inorder traversal
    def inorder_traversal(self, root):
        if root:
            self.inorder_traversal(root.left)
            print(root.key, end=' ')
            self.inorder_traversal(root.right)

    # exercise 1 : Validate AVL Tree
    def is_avl(self, node):
        if not node:
            return True
        left_avl = self.is_avl(node.left)
        right_avl = self.is_avl(node.right)
        balance = self.get_balance(node)
        return left_avl and right_avl and abs(balance) <= 1

    # exercise 2 : Range Search
    def range_search(self, root, low, high):
        result = []
        if not root:
            return result
        # If current node is greater than low, then left subtree might have values in range
        if root.key > low:
            result += self.range_search(root.left, low, high)
        # If current node is in range, add to result
        if low <= root.key <= high:
            result.append(root.key)
        # If current node is less than high, then right subtree might have values in range
        if root.key < high:
            result += self.range_search(root.right, low, high)
        return result

    # exercise 3 : k-th smallest element using inorder traversal
    def kth_smallest(self, root, k):
        # We'll collect all elements in order and return the k-th one
        elements = []
        self._inorder_collect(root, elements)
        if 1 <= k <= len(elements):
            return elements[k - 1]
        return None

    def _inorder_collect(self, node, elements):
        if node:
            self._inorder_collect(node.left, elements)
            elements.append(node.key)
            self._inorder_collect(node.right, elements)