
from heap_max_class import MaxHeap

def max_heap_sort(a):
    h = MaxHeap(a)
    result = []
    while len(h) > 0:
        result.append(h.pop())
    return result

# Testing MaxHeap operations
h = MaxHeap(arr=[22, 13, 17, 11, 6, 7, 3, 5])
print("\nInitial heap:", h.data)
h.push(30)
print("After pushing 30:", h.data)
print("Popped max:", h.pop())
print("Heap after pop:", h.data)

# Sorting in descending order using MaxHeap
print("\nSorting in descending order:")
print(max_heap_sort(h.data))  # O(n logn)