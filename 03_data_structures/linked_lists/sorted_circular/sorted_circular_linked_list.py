
from node import Node

class SortedCircularLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)

        # Case 1: List is empty
        if self.head is None:
            self.head = new_node
            new_node.next = self.head  # Circular reference to itself
            return

        # Case 2: Insert at the beginning
        if new_node.data < self.head.data:
            # Find the last node to update its next pointer
            last = self.head
            while last.next != self.head:
                last = last.next

            new_node.next = self.head
            self.head = new_node
            last.next = self.head  # Update last node's next to new head
            return

        # Case 3: Insert in the middle or end
        current = self.head
        while current.next != self.head and current.next.data < new_node.data:
            current = current.next

        new_node.next = current.next
        current.next = new_node

    def print_list(self):
        if self.head is None:
            print("[]")
            return

        current = self.head
        result = []
        # We use a loop to print until we complete the circle
        while True:
            result.append(f"[{current.data}]")
            current = current.next
            if current == self.head:
                break

        print(" -> ".join(result))

