from node import Node


class BinaryTree:
    def __init__(self):
        self.root = None

    def _insert(self, node, data):
        if not node.left:
            node.left = Node(data)
        elif not node.right:
            node.right = Node(data)
        else:
            self._insert(node.left, data)  # Simple left-first insertion
            # For complete insertion we can use Queues to track the children

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self._insert(self.root, data)

    def _search(self, node, target):
        if node is None:
            return False
        if node.data == target:
            return True
        return self._search(node.left, target) or self._search(node.right, target)

    def search(self, target):
        return self._search(self.root, target)

    def _delete(self, root, key):
        if root is None:
            return None
        if root.data == key:
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
        root.left = self._delete(root.left, key)
        root.right = self._delete(root.right, key)
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

    # Assignment: Function to check if binary tree is balanced
    def is_balanced(self):
        """
        Returns True if the binary tree is balanced, False otherwise.
        A balanced tree is one where the height difference between left and right subtrees
        is 1 or 0 or -1
        """

        def check_balance(node):
            # Base case: empty tree is balanced
            if node is None:
                return True, 0

            # Check if left subtree is balanced and get its height
            left_balanced, left_height = check_balance(node.left)
            if not left_balanced:
                return False, 0

            # Check if right subtree is balanced and get its height
            right_balanced, right_height = check_balance(node.right)
            if not right_balanced:
                return False, 0

            # Check if current node is balanced
            height_diff = abs(left_height - right_height)
            is_current_balanced = height_diff <= 1

            # Return whether current subtree is balanced and its height
            current_height = max(left_height, right_height) + 1
            return is_current_balanced, current_height

        balanced, _ = check_balance(self.root)  # the - means we don't care about the height
        return balanced