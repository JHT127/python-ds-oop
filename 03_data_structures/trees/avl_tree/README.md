# AVL Tree

A self-balancing Binary Search Tree implementation. The tree automatically rebalances after every insertion and deletion using rotations, guaranteeing O(log n) height at all times.

## Implementation

- `avl_node.py` — Node with `key` and `height` fields
- `avl_tree.py` — AVL tree with all operations
- `main.py` — Usage examples and tests

## Operations

| Method | Description | Time Complexity |
|---|---|---|
| `insert(root, key)` | Insert and rebalance | O(log n) |
| `delete(root, key)` | Delete and rebalance | O(log n) |
| `is_avl(node)` | Validate balance property | O(n) |
| `range_search(root, low, high)` | Return all keys in [low, high] | O(log n + k) |
| `kth_smallest(root, k)` | Return k-th smallest element | O(n) |
| `inorder_traversal(root)` | Print sorted order | O(n) |

## Rotations

Four rotation cases handled automatically:
- **Left-Left** → single right rotation
- **Right-Right** → single left rotation
- **Left-Right** → left rotation on child, then right rotation
- **Right-Left** → right rotation on child, then left rotation

## Example

```python
from avl_tree import AVLTree

tree = AVLTree()
root = None
for val in [10, 20, 30, 40, 50, 25]:
    root = tree.insert(root, val)

tree.inorder_traversal(root)        # 10 20 25 30 40 50
print(tree.range_search(root, 20, 35))  # [20, 25, 30]
print(tree.kth_smallest(root, 3))   # 25
print(tree.is_avl(root))            # True
```
