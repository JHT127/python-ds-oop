
class Order:
    """Represents a customer's food order"""

    # Constructor creates empty list for order items (Encapsulation)
    def __init__(self):
        self.items = []

    # Adds an item to the order (Abstraction)
    def add_item(self, item):
        self.items.append(item)

    # Calculates the total price of all items in order (Abstraction)
    def total(self):
        total_price = 0.0
        for item in self.items:
            total_price += item.price
        return total_price

    # Returns formatted information about the order (Abstraction)
    def get_info_order(self):
        info = "Order items:\n"
        for item in self.items:
            info += f"- {item.get_info_menu_item()}\n"
        info += f"Total: ${self.total():.2f}"
        return info