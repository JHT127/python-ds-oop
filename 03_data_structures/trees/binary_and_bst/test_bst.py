from binary_tree import BinaryTree
from bst import BST
from node import Node

"""
Note that the assignment does not require test cases, but I have included some test cases from the AI 
to test the code myself and thought it would be useful to show them so that you can see the 
expected results for different scenarios.
"""
def test_binary_tree_balance():
    print("=== Testing Binary Tree Balance ===")

    # Test 1: Balanced tree
    bt1 = BinaryTree()
    bt1.insert(1)
    bt1.insert(2)
    bt1.insert(3)
    bt1.insert(4)

    print("Tree 1 (balanced):")
    print("    1")
    print("   / \\")
    print("  2   3")
    print(" /")
    print("4")
    print(f"Is balanced: {bt1.is_balanced()}")
    print()

    # Test 2: Balanced tree
    bt2 = BinaryTree()
    bt2.insert(5)
    bt2.insert(6)
    bt2.insert(7)

    print("Tree 2 (balanced):")
    print("  5")
    print(" / \\")
    print("6   7")
    print(f"Is balanced: {bt2.is_balanced()}")
    print()

    # Test 3: Manually create an unbalanced tree - left skewed
    bt3 = BinaryTree()
    bt3.root = Node(10)
    bt3.root.left = Node(5)
    bt3.root.left.left = Node(3)
    bt3.root.left.left.left = Node(1)

    print("Tree 3 (unbalanced - left skewed):")
    print("10")
    print("/")
    print("5")
    print("/")
    print("3")
    print("/")
    print("1")
    print(f"Is balanced: {bt3.is_balanced()}")
    print()

    # Test 4: Manually create unbalanced tree - right skewed
    bt4 = BinaryTree()
    bt4.root = Node(1)
    bt4.root.right = Node(2)
    bt4.root.right.right = Node(3)
    bt4.root.right.right.right = Node(4)
    bt4.root.right.right.right.right = Node(5)

    print("Tree 4 (unbalanced - right skewed):")
    print("1")
    print(" \\")
    print("  2")
    print("   \\")
    print("    3")
    print("     \\")
    print("      4")
    print("       \\")
    print("        5")
    print(f"Is balanced: {bt4.is_balanced()}")
    print()

    # Test 5: Complex unbalanced case
    bt5 = BinaryTree()
    bt5.root = Node(1)
    bt5.root.left = Node(2)
    bt5.root.right = Node(3)
    bt5.root.left.left = Node(4)
    bt5.root.left.left.left = Node(5)
    bt5.root.left.left.left.left = Node(6)

    print("Tree 5 (unbalanced - complex):")
    print("    1")
    print("   / \\")
    print("  2   3")
    print(" /")
    print("4")
    print("/")
    print("5")
    print("/")
    print("6")
    print(f"Is balanced: {bt5.is_balanced()}")
    print()


def test_bst_min_max():
    print("=== Testing BST findMin and findMax ===")

    # Create BST and insert some values
    bst = BST()
    values = [50, 30, 70, 20, 40, 60, 80]

    print("Inserting values:", values)
    for val in values:
        bst.insert(val)

    print("BST structure:")
    print("       50")
    print("      /  \\")
    print("    30    70")
    print("   / \\   / \\")
    print("  20 40 60 80")
    print()

    # Test findMin
    min_node = bst.findMin()
    if min_node:
        print(f"Minimum value: {min_node.data}")
    else:
        print("Tree is empty")

    # Test findMax
    max_node = bst.findMax()
    if max_node:
        print(f"Maximum value: {max_node.data}")
    else:
        print("Tree is empty")

    print()
    print("Inorder traversal:", end=" ")
    bst.inorder()
    print()
    print("Preorder traversal:", end=" ")
    bst.preorder()
    print()
    print("Postorder traversal:", end=" ")
    bst.postorder()
    print()

    # Test other methods
    print(f"BST height: {bst.height()}")
    print(f"Is valid BST: {bst.is_valid_bst()}")

    # Test search
    print(f"Search for 40: {bst.search(40)}")
    print(f"Search for 100: {bst.search(100)}")

    # Test delete
    print("\nDeleting 30...")
    bst.delete(30)
    print("After deletion, inorder:", end=" ")
    bst.inorder()
    print()

    # Test on empty tree
    print("\n--- Testing on empty BST ---")
    empty_bst = BST()
    min_empty = empty_bst.findMin()
    max_empty = empty_bst.findMax()
    print(f"Min of empty tree: {min_empty}")
    print(f"Max of empty tree: {max_empty}")
    print(f"Height of empty tree: {empty_bst.height()}")


def test_bst_comprehensive():
    print("\n=== Comprehensive BST Test ===")

    bst = BST()

    # Test insertions
    print("Inserting: 8, 3, 10, 1, 6, 14, 4, 7, 13")
    values = [8, 3, 10, 1, 6, 14, 4, 7, 13]
    for val in values:
        bst.insert(val)

    print("Final BST structure:")
    print("         8")
    print("       /   \\")
    print("      3     10")
    print("     / \\      \\")
    print("    1   6      14")
    print("       / \\    /")
    print("      4   7  13")
    print()

    # Test all traversals
    print("Inorder (sorted):", end=" ")
    bst.inorder()
    print()

    print("Preorder:", end=" ")
    bst.preorder()
    print()

    print("Postorder:", end=" ")
    bst.postorder()
    print()

    # Test min/max
    min_node = bst.findMin()
    max_node = bst.findMax()
    print(f"Minimum: {min_node.data if min_node else None}")
    print(f"Maximum: {max_node.data if max_node else None}")

    # Test height and validation
    print(f"Height: {bst.height()}")
    print(f"Valid BST: {bst.is_valid_bst()}")


if __name__ == "__main__":
    test_binary_tree_balance()
    print()
    test_bst_min_max()
    test_bst_comprehensive()