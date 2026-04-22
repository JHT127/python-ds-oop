# Python · Data Structures & OOP — GSG SkillStack

My solutions to all assignments from the **Gaza Sky Geeks SkillStack** program (Python track), covering Python fundamentals, Object-Oriented Programming, and Data Structures & Algorithms from scratch through advanced self-balancing trees and graph traversal.

> **Program:** [Gaza Sky Geeks SkillStack](https://gazaskygeeks.com/)
> **Course materials:** [courses-library](https://github.com/GazaSkyGeeks/courses-library) (instructor's repo)
> **Duration:** ~4 months | **Language:** Python 3

---

## 📁 Repository Structure

```
gsg-python-ds-oop/
│
├── 01_python_fundamentals/
│   ├── leap_year/              — Conditional logic, two implementation approaches
│   ├── file_analysis/          — File I/O, word frequency counting, prime analysis
│   └── vending_machine/        — OOP + file parsing, inheritance warm-up
│
├── 02_oop/
│   ├── restaurant_system/      — Composition, abstraction, encapsulation
│   └── library_system/         — Full OOP project: abstract classes, interfaces,
│                                 custom exceptions, JSON persistence
│
└── 03_data_structures/
    ├── linked_lists/
    │   ├── singly_reverse/     — Singly linked list with reversal algorithm
    │   └── sorted_circular/    — Sorted insertion in circular linked list
    ├── stacks/                 — Array-based stack, balanced brackets problem
    ├── queues/                 — Linked queue + customer service simulation
    ├── trees/
    │   ├── binary_and_bst/     — Binary tree, BST insert/search/delete + tests
    │   └── avl_tree/           — Self-balancing AVL tree: rotations, range search, kth smallest
    ├── graphs/                 — Adjacency list graph, BFS, DFS, city map app
    ├── heaps/                  — Max-heap with heapify-up/down, build_heap O(n)
    └── hash_tables/            — Chaining hash table, collision handling
```

---

## 🔑 Highlights

| Project | Concepts | Complexity |
|---|---|---|
| [Library System](./02_oop/library_system/) | Abstract classes, interfaces, custom exceptions, JSON I/O | ⭐⭐⭐ |
| [AVL Tree](./03_data_structures/trees/avl_tree/) | Self-balancing, rotations, range search, kth-smallest | ⭐⭐⭐ |
| [City Map Graph](./03_data_structures/graphs/) | BFS, DFS, DFS post-order, weighted edges | ⭐⭐⭐ |
| [BST](./03_data_structures/trees/binary_and_bst/) | Insert, search, delete (all 3 cases), unit tests | ⭐⭐ |
| [Max Heap](./03_data_structures/heaps/) | heapify-up/down, O(n) build_heap, push/pop/peek | ⭐⭐ |
| [Restaurant System](./02_oop/restaurant_system/) | Composition, encapsulation, CLI interface | ⭐⭐ |

---

## 🚀 Running Any Project

Each folder is self-contained. Example:

```bash
# Clone the repo
git clone https://github.com/YOUR_USERNAME/gsg-python-ds-oop.git
cd gsg-python-ds-oop

# Run any project
python 02_oop/library_system/main.py
python 03_data_structures/trees/avl_tree/main.py
python 03_data_structures/graphs/main.py
```

No external dependencies — standard Python 3 only.

---

## 📈 Learning Progression

```
Python Basics → OOP Fundamentals → OOP Project →
Linked Lists → Stacks & Queues → Trees (Binary → BST → AVL) →
Graphs (BFS/DFS) → Heaps → Hash Tables
```

This progression maps directly to the standard CS fundamentals curriculum taught in university DS&A courses.

---

## 🧠 Key Algorithms Implemented

- **Linked List Reversal** — iterative pointer manipulation
- **AVL Rotations** — left, right, left-right, right-left
- **BST Deletion** — all three cases including inorder successor
- **BFS & DFS** — both iterative, plus DFS post-order
- **Heapify** — up and down, used in push/pop/build
- **Hash Chaining** — separate chaining for collision resolution

---

*Completed as part of Gaza Sky Geeks SkillStack · 2025*
