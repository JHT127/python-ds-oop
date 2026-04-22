
from models.library_item import LibraryItem
from models.reservable import Reservable
from typing import Optional
from exceptions.custom_exceptions import ItemAvailableError, ItemAlreadyReservedError, ItemNotReservedError

class DVD(LibraryItem, Reservable):
    def __init__(self, item_id, title, author, year, runtime, formats):
        super().__init__(item_id, title, author, year)
        self._is_reserved = False
        self._reserved_by = None
        self.runtime = runtime
        self.formats = formats

    @property
    def reserved_by(self) -> Optional[str]:
        return self._reserved_by

    @property
    def is_reserved(self):
        return self._is_reserved

    def display_info(self):
        status = "Available" if self.is_available else f"Borrowed by {self.borrowed_by}"
        reserved_status = f", Reserved by {self.reserved_by}" if self.is_reserved else ""
        return (f"DVD: {self.title} ({self.year})\n"
                f"Director: {self.author}, Runtime: {self.runtime} minutes\n"
                f"Format: {self.formats}\n"
                f"Status: {status}{reserved_status}")

    def reserve(self, user_id):
        if self.is_reserved:
            raise ItemAlreadyReservedError(f"DVD {self.item_id} is already reserved")
        if self.is_available:
            raise ItemAvailableError(f"Cannot reserve available item {self.item_id}. Please borrow instead.")
        self._is_reserved = True
        self._reserved_by = user_id
        return True

    def cancel_reservation(self, user_id):
        if not self.is_reserved:
            raise ItemNotReservedError(f"DVD {self.item_id} is not reserved")
        if self.reserved_by != user_id:
            raise ItemAvailableError(f"DVD {self.item_id} is not reserved by user {user_id}")
        self._is_reserved = False
        self._reserved_by = None
        return True