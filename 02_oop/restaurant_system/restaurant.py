
from menu_item import MenuItem
from order import Order

class Restaurant:
    """Main restaurant class that manages menu and orders"""

    # Constructor initializes empty menu and orders lists (Encapsulation)
    def __init__(self):
        self.menu = []
        self.orders = []

    # Creates and adds new item to the menu (Abstraction)
    def add_menu_item(self, name, price, category):
        new_item = MenuItem(name, price, category)
        self.menu.append(new_item)
        return new_item

    # Returns current menu items (Abstraction)
    def get_menu(self):
        return self.menu

    # Creates new order from selected menu items (Abstraction)
    def create_order(self, item_numbers):
        new_order = Order()
        for num in item_numbers:
            index = num - 1
            if 0 <= index < len(self.menu):
                new_order.add_item(self.menu[index])
        return new_order

    # Adds completed order to restaurant records (Abstraction)
    def add_order(self, order):
        self.orders.append(order)

    # Displays all placed orders (Abstraction)
    def list_orders(self):
        if not self.orders:
            print("No orders have been placed yet.")
            return

        print("\nAll Orders:")
        order_number = 1
        for order in self.orders:
            print(f"Order #{order_number}:")
            print(order.get_info_order())
            print("-" * 20)
            order_number += 1