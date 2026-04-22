
from datetime import datetime
from exceptions.custom_exceptions import ItemAlreadyBorrowedError, ItemNotBorrowedError

class User:
    def __init__(self, user_id, name, email, membership_date = None):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.membership_date = membership_date or datetime.now().strftime("%Y-%m-%d")
        self.borrowed_items = []
        self.reserved_items = []

    def display_info(self):
        return (f"User ID: {self.user_id}\n"
                f"Name: {self.name}\n"
                f"Email: {self.email}\n"
                f"Member since: {self.membership_date}\n"
                f"Borrowed items: {len(self.borrowed_items)}\n"
                f"Reserved items: {len(self.reserved_items)}")

    def add_borrowed_item(self, item_id):
        if item_id in self.borrowed_items:
            raise ItemAlreadyBorrowedError(f"Item {item_id} is already borrowed by user {self.user_id}")
        self.borrowed_items.append(item_id)

    def add_reserved_item(self, item_id):
        if item_id in self.reserved_items:
            raise ItemAlreadyBorrowedError(f"Item {item_id} is already reserved by user {self.user_id}")
        self.reserved_items.append(item_id)

    def return_item(self, item_id):
        if item_id not in self.borrowed_items:
            raise ItemNotBorrowedError(f"Item {item_id} is not borrowed by user {self.user_id}")
        self.borrowed_items.remove(item_id)

    def cancel_reservation(self, item_id):
        if item_id not in self.reserved_items:
            raise ItemNotBorrowedError(f"Item {item_id} is not reserved by user {self.user_id}")
        self.reserved_items.remove(item_id)


