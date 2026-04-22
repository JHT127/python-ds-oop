
from sorted_circular_linked_list import SortedCircularLinkedList

# Example
if __name__ == "__main__":
    sorted_cll = SortedCircularLinkedList()

    print("After inserting 7:", end=" ")
    sorted_cll.insert(7)
    sorted_cll.print_list()

    print("After inserting 3:", end=" ")
    sorted_cll.insert(3)
    sorted_cll.print_list()

    print("After inserting 9:", end=" ")
    sorted_cll.insert(9)
    sorted_cll.print_list()

    print("After inserting 1:", end=" ")
    sorted_cll.insert(1)
    sorted_cll.print_list()

    print("After inserting 4:", end=" ")
    sorted_cll.insert(4)
    sorted_cll.print_list()