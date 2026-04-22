
class MenuItem:
    """Represents a single item on the restaurant menu"""

    # Constructor initializes the menu item attributes (Encapsulation)
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    # Returns formatted information about the menu item (Abstraction)
    def get_info_menu_item(self):
        return f"{self.name} (${self.price:.2f}) [{self.category}]"