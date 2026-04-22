from node import Node


class BST:
    def __init__(self):
        self.root = None

    def _insert(self, node, data):
        if node is None:
            return Node(data)
        if data < node.data:
            node.left = self._insert(node.left, data)
        else:
            node.right = self._insert(node.right, data)
        return node

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self.root = self._insert(self.root, data)

    def _search(self, node, target):
        if node is None:
            return False
        if node.data == target:
            return True
        elif target < node.data:
            return self._search(node.left, target)
        else:
            return self._search(node.right, target)

    def search(self, target):
        return self._search(self.root, target)

    def _delete(self, root, key):
        if root is None:
            return None
        if key < root.data:
            root.left = self._delete(root.left, key)
        elif key > root.data:
            root.right = self._delete(root.right, key)
        else:
            # Case 1: Node with no child
            if not root.left and not root.right:
                return None
            # Case 2: Node with only one child
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            # Case 3: Node with two children - replace with inorder successor
            succ_parent = root
            succ = root.right
            while succ.left:
                succ_parent = succ
                succ = succ.left
            if succ_parent != root:
                succ_parent.left = succ.right
            else:
                succ_parent.right = succ.right
            root.data = succ.data
            return root
        return root

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _inorder(self, node):
        if node:
            self._inorder(node.left)
            print(node.data, end=' ')
            self._inorder(node.right)

    def inorder(self):
        self._inorder(self.root)

    def _preorder(self, node):
        if node:
            print(node.data, end=' ')
            self._preorder(node.left)
            self._preorder(node.right)

    def preorder(self):
        self._preorder(self.root)

    def _postorder(self, node):
        if node:
            self._postorder(node.left)
            self._postorder(node.right)
            print(node.data, end=' ')

    def postorder(self):
        self._postorder(self.root)

    def _findMin(self, node):
        """Protected method to find minimum in a subtree"""
        if node is None:
            return None
        current = node
        while current.left:
            current = current.left
        return current

    def findMin(self):
        """
        Assignment: Find the minimum value in the BST
        Returns the node with minimum value, or None if tree is empty
        """
        return self._findMin(self.root)

    def _findMax(self, node):
        """Protected method to find maximum in a subtree"""
        if node is None:
            return None
        current = node
        while current.right:
            current = current.right
        return current

    def findMax(self):
        """
        Assignment: Find the maximum value in the BST
        Returns the node with maximum value, or None if tree is empty
        """
        return self._findMax(self.root)

    def _height(self, node):
        """Protected method to calculate height of a subtree"""
        if node is None:
            return 0
        left_height = self._height(node.left)
        right_height = self._height(node.right)
        return max(left_height, right_height) + 1

    def height(self):
        """Calculate the height of the BST"""
        return self._height(self.root)

    def _validate_bst(self, node, prev_val):
        """Protected method to validate if tree maintains BST property using inorder"""
        if node is None:
            return True, prev_val

        # Check left subtree
        is_left_valid, prev_val = self._validate_bst(node.left, prev_val)
        if not is_left_valid:
            return False, prev_val

        # Current node should be greater than previous inorder value
        if prev_val is not None and node.data <= prev_val:
            return False, prev_val

        # Update previous value to current node
        prev_val = node.data

        # Check right subtree
        return self._validate_bst(node.right, prev_val)

    def is_valid_bst(self):
        """Check if the tree is a valid BST - inorder should give sorted sequence"""
        is_valid, _ = self._validate_bst(self.root, None)
        return is_valid