
import os
import json
from typing import Dict
from models.library import Library
from models.library_item import LibraryItem
from models.user import User
from models.book import Book
from models.magazine import Magazine
from models.dvd import DVD
from exceptions.custom_exceptions import *


class Main:
    def __init__(self):
        # Define file paths for items and users
        self.ITEMS_FILE = "data/items.json"
        self.USERS_FILE = "data/users.json"

        # Initialize the library
        self.library = Library()
        self.library.items = self.load_items()
        self.library.users = self.load_users()

        # Ensure data directory exists
        os.makedirs('data', exist_ok=True)

    @staticmethod
    def _create_item_from_data(item_data: Dict) -> LibraryItem:
        """Create library items from data"""
        item_type = item_data['type']
        if item_type == 'Book':
            return Book(
                item_id=item_data['item_id'],
                title=item_data['title'],
                author=item_data['author'],
                year=item_data['year'],
                isbn=item_data['isbn'],
                pages=item_data['pages']
            )
        elif item_type == 'Magazine':
            return Magazine(
                item_id=item_data['item_id'],
                title=item_data['title'],
                publisher=item_data['author'],
                year=item_data['year'],
                issue_number=item_data['issue'],
                pages=item_data['pages']
            )

        elif item_type == 'DVD':
            return DVD(
                item_id=item_data['item_id'],
                title=item_data['title'],
                author=item_data['author'],
                year=item_data['year'],
                runtime=item_data['runtime'],
                formats=item_data['format']
            )
        else:
            raise InvalidItemTypeError(f"Unknown item type: {item_type}")

    def load_items(self) -> Dict[str, LibraryItem]:
        """Load items from JSON file"""
        items = {}
        items_file_handle = None
        try:
            # Open and read items file
            items_file_handle = open(self.ITEMS_FILE, 'r')
            items_data = json.load(items_file_handle)

            # Create and store items in library
            for item_data in items_data:
                try:
                    item = self._create_item_from_data(item_data)
                    items[item.item_id] = item
                except InvalidItemTypeError as e:
                    print(f"Error creating item: {e}")
                except KeyError as e:
                    print(f"Missing required field in item data: {e}")

        except FileNotFoundError:
            print("Items file not found. Starting with empty library.")
        except json.JSONDecodeError:
            print("Error decoding items JSON. Starting with empty library.")
        except Exception as e:
            print(f"Unexpected error loading items: {e}")
        finally:
            if items_file_handle is not None:
                items_file_handle.close()

        return items

    def load_users(self) -> Dict[str, User]:
        """Load users from JSON file"""
        users = {}
        users_file_handle = None
        try:
            # Open and read users file
            users_file_handle = open(self.USERS_FILE, 'r')
            users_data = json.load(users_file_handle)

            # Create and store users in library
            for user_data in users_data:
                try:
                    user = User(
                        user_id=user_data['user_id'],
                        name=user_data['name'],
                        email=user_data['email'],
                        membership_date=user_data.get('membership_date')
                    )
                    user.borrowed_items = user_data.get('borrowed_items', [])
                    user.reserved_items = user_data.get('reserved_items', [])
                    users[user.user_id] = user
                except KeyError as e:
                    print(f"Missing required field in user data: {e}")

        except FileNotFoundError:
            print("Users file not found. Starting with no users.")
        except json.JSONDecodeError:
            print("Error decoding users JSON. Starting with no users.")
        except Exception as e:
            print(f"Unexpected error loading users: {e}")
        finally:
            if users_file_handle is not None:
                users_file_handle.close()

        return users

    def initialize_library(self) -> Library:
        """Initialize the library with loaded data"""
        items = self.load_items()
        users = self.load_users()
        return Library(items, users)

    def _save_items(self) -> bool:
        """Save items to JSON file"""
        items_file_handle = None
        try:
            items_data = []
            # Prepare items data for saving
            for item in self.library.items.values():
                item_dict = {
                    'item_id': item.item_id,
                    'type': item.__class__.__name__,
                    'title': item.title,
                    'author': item.author,
                    'year': item.year,
                    'is_available': item.is_available,
                    'borrowed_by': item.borrowed_by,
                    'borrow_date': item.borrow_date
                }

                if isinstance(item, Book):
                    item_dict.update({
                        'isbn': item.isbn,
                        'pages': item.pages,
                        'is_reserved': item.is_reserved,
                        'reserved_by': item.reserved_by
                    })
                elif isinstance(item, Magazine):
                    item_dict.update({
                        'issue': item.issue_number,
                        'pages': item.pages,
                    })
                elif isinstance(item, DVD):
                    item_dict.update({
                        'runtime': item.runtime,
                        'format': item.formats,
                        'is_reserved': item.is_reserved,
                        'reserved_by': item.reserved_by
                    })

                items_data.append(item_dict)

            # Write items data to JSON file
            items_file_handle = open(self.ITEMS_FILE, 'w')
            json.dump(items_data, items_file_handle, indent=4)
            return True

        except Exception as e:
            print(f"Error saving items: {e}")
            return False
        finally:
            if items_file_handle is not None:
                items_file_handle.close()

    def _save_users(self) -> bool:
        """Save users to JSON file"""
        users_file_handle = None
        try:
            users_data = []
            # Prepare users data for saving
            for user in self.library.users.values():
                users_data.append({
                    'user_id': user.user_id,
                    'name': user.name,
                    'email': user.email,
                    'membership_date': user.membership_date,
                    'borrowed_items': user.borrowed_items,
                    'reserved_items': user.reserved_items
                })

            # Write users data to JSON file
            users_file_handle = open(self.USERS_FILE, 'w')
            json.dump(users_data, users_file_handle, indent=4)
            return True

        except Exception as e:
            print(f"Error saving users: {e}")
            return False
        finally:
            if users_file_handle is not None:
                users_file_handle.close()

    def save_data(self) -> bool:
        """Save all library data to files"""
        success = True
        if not self._save_items():
            success = False
        if not self._save_users():
            success = False
        return success


    @staticmethod
    def display_menu():
        """Display the main menu options"""
        print("\nWelcome to the Library System")
        print("1. View all available items")
        print("2. Search item by title or type")
        print("3. Register as a new user")
        print("4. Borrow an item")
        print("5. Reserve an item")
        print("6. Return an item")
        print("7. Exit and Save")

    def run(self):
        """Run the main application loop"""
        try:
            while True:
                self.display_menu()
                choice = input("Enter your choice (1-7): ")

                try:
                    if choice == '1':
                        # Display all available items
                        print("\nAvailable Items:")
                        for item in self.library.items.values():
                            if item.is_available:
                                print(item.display_info())
                                print("-" * 40)

                    elif choice == '2':
                        # Search for items by title or type
                        search_term = input("Enter search term (title or type - Book/Magazine/DVD): ").lower()
                        print("\nSearch Results:")
                        for item in self.library.items.values():
                            if (search_term in item.title.lower() or
                                    search_term == item.__class__.__name__.lower()):
                                print(item.display_info())
                                print("-" * 40)

                    elif choice == '3':
                        # Register a new user
                        name = input("Enter your name: ")
                        email = input("Enter your email: ")
                        user_id = f"U{len(self.library.users) + 1:03d}"
                        self.library.register_user(user_id, name, email)
                        print(f"\nRegistration successful! Your user ID is: {user_id}")

                    elif choice == '4':
                        # Borrow an item
                        user_id = input("Enter your user ID: ")
                        item_id = input("Enter item ID to borrow: ")
                        self.library.borrow_item(user_id, item_id)
                        print(f"\nItem {item_id} borrowed successfully!")

                    elif choice == '5':
                        # Reserve an item
                        user_id = input("Enter your user ID: ")
                        item_id = input("Enter item ID to reserve: ")
                        self.library.reserve_item(user_id, item_id)
                        print(f"\nItem {item_id} reserved successfully!")

                    elif choice == '6':
                        # Return an item
                        user_id = input("Enter your user ID: ")
                        item_id = input("Enter item ID to return: ")
                        self.library.return_item(user_id, item_id)
                        print(f"\nItem {item_id} returned successfully!")

                    elif choice == '7':
                        # Exit and save data
                        if self.save_data():
                            print("\nData saved successfully. Goodbye!")
                        else:
                            print("\nThere were errors saving data. Please check the files.")
                        break

                    else:
                        print("\nInvalid choice. Please enter a number between 1 and 7.")

                except LibraryError as e:
                    print(f"\nLibrary Error: {e}")
                except Exception as e:
                    print(f"\nAn unexpected error occurred: {e}")

        except KeyboardInterrupt:
            print("\n\nProgram interrupted by user")
            if self.save_data():
                print("Data saved successfully before exit.")
            else:
                print("There were errors saving data before exit.")


if __name__ == "__main__":
    main = Main()
    main.run()
