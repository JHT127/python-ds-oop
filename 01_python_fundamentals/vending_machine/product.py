
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display_info(self):
        print(f"The name of the product is {self.name}.")
        print(f"The price of the product is ${self.price}.")
