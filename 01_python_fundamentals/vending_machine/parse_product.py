
from drink import Drink
from snack import Snack
from candy import Candy

def create_product(line):

    parts = line.strip().split(',')
    product_type, product_name, product_price, product_attribute = parts

    if product_type == 'Drink':
        return Drink(product_name, product_price, product_attribute)
    elif product_type == 'Snack':
        return Snack(product_name, product_price, product_attribute)
    elif product_type == 'Candy':
        return Candy(product_name, product_price, product_attribute)
