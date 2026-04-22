from linkedlist import LinkedList

# --- Example Usage ---
ls = LinkedList()

# Build the list: [7] -> [5] -> [8] -> [90] -> [12] -> None
ls.insert_at_start(5)
ls.insert_at_start(7)
ls.insert_at_end(90)
ls.insert_at_end(12)
ls.insert_at_index(8, 2)  # Insert 8 at index 2

print("\nOriginal list:", ls)  # [7]->[5]->[8]->[90]->[12]->None

# --- Function 1: Reverse the original list (in-place) ---
def reverse_same_list(head):
    """Reverses the linked list in-place by modifying node pointers."""
    current = head
    previous = None
    while current is not None:
        next_node = current.next  # Store next node temporarily
        current.next = previous  # Reverse the link
        previous = current       # Move previous forward
        current = next_node      # Move current forward
    return previous  # New head of the reversed list

ls.head = reverse_same_list(ls.head)
print("\nAfter reversing the original list itself:", ls)  # [12]->[90]->[8]->[5]->[7]->None

# --- Function 2: Create a new reversed list (original unchanged) ---
def reverse_using_new_list(head):
    """Returns a new LinkedList with elements in reverse order."""
    new_list = LinkedList()
    current = head
    while current is not None:
        new_list.insert_at_start(current.data)  # Insert at start to reverse
        current = current.next
    return new_list

# Reset list to original for testing (since we modified it earlier)
ls.head = reverse_same_list(ls.head)  # Reverse again to restore original
print("\nRestored original:", ls)  # [7]->[5]->[8]->[90]->[12]->None

# Now test reverse_using_new_list
reversed_list = reverse_using_new_list(ls.head)
print("\nReversing using new list:", reversed_list)  # [12]->[90]->[8]->[5]->[7]->None
print("Original list (unchanged using the second function):", ls)  # [7]->[5]->[8]->[90]->[12]->None