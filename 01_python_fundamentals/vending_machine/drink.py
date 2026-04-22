
from product import Product

class Drink(Product):
    def __init__(self,name, price, volume):
        super().__init__(name, price)
        self.volume = volume

    def display_info(self):
        super().display_info()
        print(f"The volume of {self.name} is {self.volume}ml")

