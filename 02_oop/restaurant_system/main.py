
from restaurant import Restaurant

class Main:
    """Main application class that handles user interaction"""

    # Constructor creates Restaurant instance (Composition)
    def __init__(self):
        self.restaurant = Restaurant()

    # Displays options and gets user choice (Abstraction)
    def show_options(self):
        print("\nWelcome to the Restaurant Management System!")
        print("1. Add menu item")
        print("2. View menu")
        print("3. Create new order")
        print("4. List all orders")
        print("5. Exit")
        choice = input("Choose an option: ")
        if choice.isdigit() and 1 <= int(choice) <= 5:
            return int(choice)
        print("Please enter a number from 1 to 5 only!")
        return self.show_options()

    # Handles adding new menu item (Abstraction)
    def add_menu_item(self):
        print("\nAdd New Menu Item")
        name = input("Enter item name: ")
        price = float(input("Enter item price: "))
        category = input("Enter item category: ")
        self.restaurant.add_menu_item(name, price, category)
        print("Menu item added!")

    # Displays current menu (Abstraction)
    def show_menu(self):
        menu = self.restaurant.get_menu()
        if len(menu) == 0:
            print("\nMenu is empty")
            return

        print("\nCurrent Menu:")
        count = 1
        for item in menu:
            print(f"{count}. {item.get_info_menu_item()}")
            count += 1

    # Handles creating new order (Abstraction)
    def make_order(self):
        menu = self.restaurant.get_menu()
        if len(menu) == 0:
            print("\nCan't order - menu is empty!")
            return

        self.show_menu()
        selections = input("\nEnter item numbers (comma separated): ")
        items = []
        for num in selections.split(','):
            if num.strip().isdigit():
                items.append(int(num.strip()))

        if len(items) > 0:
            order = self.restaurant.create_order(items)
            self.restaurant.add_order(order)
            print("Order created!")
        else:
            print("Invalid items. Try again.")

    # Displays all orders (Abstraction)
    def show_orders(self):
        self.restaurant.list_orders()

    # Main program loop (Control flow)
    def run(self):
        while True:
            choice = self.show_options()

            if choice == 1:
                self.add_menu_item()
            elif choice == 2:
                self.show_menu()
            elif choice == 3:
                self.make_order()
            elif choice == 4:
                self.show_orders()
            elif choice == 5:
                print("\nThank you for using the Restaurant Management System!")
                break
            else:
                print("Invalid choice")


# Program entry point
if __name__ == "__main__":
    system = Main()
    system.run()