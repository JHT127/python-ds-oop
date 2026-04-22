
from abc import ABC, abstractmethod
from datetime import datetime
from exceptions.custom_exceptions import ItemNotAvailableError, ItemAlreadyAvailableError

class LibraryItem(ABC):
    def __init__(self, item_id, title, author, year):
        self.item_id = item_id
        self.title = title
        self.author = author
        self.year = year
        self.is_available = True
        self.borrowed_by = None
        self.borrow_date = None

    @abstractmethod
    def display_info(self):
        pass

    def check_availability(self):
        return self.is_available

    def borrow(self, user_id):
        if not self.is_available:
            raise ItemNotAvailableError(f"Item {self.item_id} is not available for borrowing")
        self.is_available = False
        self.borrowed_by = user_id
        self.borrow_date = datetime.now().strftime("%Y-%m-%d")
        return True

    def return_item(self):
        if self.is_available:
            raise ItemAlreadyAvailableError(f"Item {self.item_id} is already available")
        self.is_available = True
        self.borrowed_by = None
        self.borrow_date = None
        return True