
from models.library_item import LibraryItem
from models.reservable import Reservable
from typing import Optional
from exceptions.custom_exceptions import ItemAvailableError, ItemAlreadyReservedError, ItemNotReservedError

class Book(LibraryItem, Reservable):
    """A book in the library."""

    def __init__(self, item_id, title, author, year, isbn, pages):
        """Initialize a Book object.

        Args:
            item_id (str): The ID of the book.
            title (str): The title of the book.
            author (str): The author of the book.
            year (int): The year the book was published.
            isbn (str): The ISBN of the book.
            pages (int): The number of pages in the book.
        """
        super().__init__(item_id, title, author, year)
        self.isbn = isbn
        self.pages = pages
        self._is_reserved = False
        self._reserved_by = None

    @property
    def is_reserved(self):
        """Whether the book is reserved or not."""
        return self._is_reserved

    @property
    def reserved_by(self) -> Optional[str]:
        """The user ID of the user who reserved the book or None if not reserved."""
        return self._reserved_by

    def display_info(self):
        """Return a string with information about the book."""
        status = "Available" if self.is_available else f"Borrowed by {self.borrowed_by}"
        reserved_status = f", Reserved by {self.reserved_by}" if self.is_reserved else ""
        return (f"Book: {self.title} by {self.author} ({self.year})\n"
                f"ISBN: {self.isbn}, Pages: {self.pages}\n"
                f"Status: {status}{reserved_status}")

    def reserve(self, user_id):
        """Reserve the book for a user.

        Args:
            user_id (str): The ID of the user who wants to reserve the book.

        Returns:
            bool: Whether the book was reserved successfully or not.

        Raises:
            ItemAlreadyReservedError: If the book is already reserved.
            ItemAvailableError: If the book is available and cannot be reserved.
        """
        if self.is_reserved:
            raise ItemAlreadyReservedError(f"Item {self.item_id} is already reserved")
        if self.is_available:
            raise ItemAvailableError(f"Cannot reserve available item {self.item_id}. Please borrow instead.")
        self._is_reserved = True
        self._reserved_by = user_id
        return True

    def cancel_reservation(self, user_id):
        """Cancel a reservation of the book.

        Args:
            user_id (str): The ID of the user who wants to cancel the reservation.

        Returns:
            bool: Whether the reservation was cancelled successfully or not.

        Raises:
            ItemNotReservedError: If the book is not reserved.
            ItemAvailableError: If the book is not reserved by the given user.
        """
        if not self.is_reserved:
            raise ItemNotReservedError(f"Book {self.item_id} is not reserved")
        if self.reserved_by != user_id:
            raise ItemAvailableError(f"Book {self.item_id} is not reserved by user {user_id}")
        self._is_reserved = False
        self._reserved_by = None
        return True
