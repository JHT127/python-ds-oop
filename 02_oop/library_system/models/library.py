
from typing import Dict
from models.library_item import LibraryItem
from models.reservable import Reservable
from models.user import User
from exceptions.custom_exceptions import *

class Library:

    def __init__(self, items=None, users=None):
        self.items: Dict[str, LibraryItem] = items if items is not None else {}
        self.users: Dict[str, User] = users if users is not None else {}

    def add_item(self, item: LibraryItem) -> None:
        """Add a new item to the library"""
        if item.item_id in self.items:
            raise ValueError(f"Item with ID {item.item_id} already exists")
        self.items[item.item_id] = item

    def remove_item(self, item_id: str) -> None:
        """Remove an item from the library"""
        if item_id not in self.items:
            raise ItemNotFoundError(f"Item with ID {item_id} not found")
        del self.items[item_id]

    def register_user(self, user_id: str, name: str, email: str) -> User:
        """Register a new user"""
        if user_id in self.users:
            raise ValueError(f"User with ID {user_id} already exists")
        user = User(user_id, name, email)
        self.users[user_id] = user
        return user

    def remove_user(self, user_id: str) -> None:
        """Remove a user from the library"""
        if user_id not in self.users:
            raise UserNotFoundError(f"User with ID {user_id} not found")
        del self.users[user_id]

    def get_user(self, user_id: str) -> User:
        """Get a user by ID"""
        if user_id not in self.users:
            raise UserNotFoundError(f"User with ID {user_id} not found")
        return self.users[user_id]

    def get_item(self, item_id: str) -> LibraryItem:
        """Get an item by ID"""
        if item_id not in self.items:
            raise ItemNotFoundError(f"Item with ID {item_id} not found")
        return self.items[item_id]

    def borrow_item(self, user_id: str, item_id: str) -> None:
        """Borrow an item with proper error handling"""
        try:
            user = self.get_user(user_id)
            item = self.get_item(item_id)

            if not item.is_available:
                raise ItemNotAvailableError(f"Item {item_id} is not available")

            # Perform the borrow operation
            item.borrow(user_id)
            user.add_borrowed_item(item_id)

        except Exception as e:
            raise LibraryError(f"Error borrowing item: {str(e)}")

    def return_item(self, user_id: str, item_id: str) -> None:
        """Return an item"""
        user = self.get_user(user_id)
        item = self.get_item(item_id)

        if item.return_item():
            user.return_item(item_id)

    def reserve_item(self, user_id: str, item_id: str) -> None:
        """Reserve an item"""
        user = self.get_user(user_id)
        item = self.get_item(item_id)

        if not isinstance(item, Reservable):
            raise LibraryError(f"Item {item_id} does not support reservations")

        if item.reserve(user_id):
            user.add_reserved_item(item_id)