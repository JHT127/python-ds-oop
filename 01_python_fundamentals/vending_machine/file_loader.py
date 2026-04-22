
from parse_product import create_product

def load_products_from_file(filename):
    products = []
    with open(filename, 'r') as file:
        for line in file:
            product = create_product(line)
            products.append(product)
    return products