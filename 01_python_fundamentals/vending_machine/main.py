
from file_loader import load_products_from_file

class Main:
    products = load_products_from_file("products.txt")

    @staticmethod
    def display_menu(products):
        print("\nWelcome to the Vending Machine!")
        print("Please select what you want:")

        i = 0
        while i < len(products):
            product = products[i]
            print(str(i + 1) + ". " + type(product).__name__ + " - " + product.name)
            i = i + 1

    def main(self):
        products = load_products_from_file("products.txt")

        if len(products) == 0:
            print("No products found.")
            return

        while True:
            self.display_menu(products)

            choice = input("Enter your choice: ")

            if choice.isdigit():
                order_num = int(choice)
                if 1 <= order_num <= len(products):
                    print("\nProduct Information:")
                    products[order_num - 1].display_info()
                else:
                    print("Invalid choice. Try again.")
            else:
                print("Please enter a number.")

            again = input("Do you want to choose another product? (y/n): ")
            if again.lower() != "y":
                print("\nThank you for using our vending machine, Goodbye!")
                break

if __name__ == "__main__":
    m = Main()
    m.main()

