
from avl_tree import AVLTree

def main():
    avl1 = AVLTree()
    root1 = None

    # Insert some values
    keys = [10, 20, 30, 40, 50, 25]
    for key1 in keys:
        root1 = avl1.insert(root1, key1)

    # Print inorder traversal (should be sorted)
    print("Testing AVL Tree Implementation:\nInorder traversal after insertions:")
    avl1.inorder_traversal(root1)
    print()

    # Delete a value
    root1 = avl1.delete(root1, 30)

    # Print inorder traversal after deletion
    print("Inorder traversal after deleting 30:")
    avl1.inorder_traversal(root1)
    print()

    # Check if tree is still AVL after deletion
    print("\nExercise 1: Is it still an AVL tree after deletion (balanced)?", avl1.is_avl(root1))

    # Range search
    avl2 = AVLTree()
    root2 = None

    print("\nExercise 2: Range search")
    # Insert values: 40, 20, 60, 10, 30, 50, 70
    keys = [40, 20, 60, 10, 30, 50, 70]
    for key2 in keys:
        root2 = avl2.insert(root2, key2)

    # Print inorder traversal to show sorted order
    print("Inorder traversal:")
    avl2.inorder_traversal(root2)
    print("\n")

    # Test range search
    print("Range search (25, 65):", avl2.range_search(root2, 25, 65))
    print("Range search (10, 30):", avl2.range_search(root2, 10, 30))
    print("Range search (50, 70):", avl2.range_search(root2, 50, 70))
    print("Range search (5, 15):", avl2.range_search(root2, 5, 15))

    # Check if tree is still AVL after range search
    print("Is it still an AVL tree after range search (balanced)?", avl2.is_avl(root2))

    # Exercise 3: k-th smallest element using inorder traversal
    avl3 = AVLTree()
    root3 = None

    print("\nExercise 3: k-th smallest element")
    # Insert values: [50, 30, 70, 20, 40, 60, 80]
    keys = [50, 30, 70, 20, 40, 60, 80]
    for key3 in keys:
        root3 = avl3.insert(root3, key3)

    # Print inorder traversal to show sorted order
    print("Inorder traversal:")
    avl3.inorder_traversal(root3)
    print("\n")

    # Test k-th smallest
    print("4th smallest element:", avl3.kth_smallest(root3, 4))
    print("1st smallest element:", avl3.kth_smallest(root3, 1))
    print("7th smallest element:", avl3.kth_smallest(root3, 7))
    print("Test out of bounds (k=0):", avl3.kth_smallest(root3, 0))
    print("Test out of bounds (k=8):", avl3.kth_smallest(root3, 8))

    # Check if tree is still AVL
    print("Is it still an AVL tree after k-th smallest search (balanced)?", avl3.is_avl(root3))

if __name__ == "__main__":
    main()