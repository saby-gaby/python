class Catalogue:

    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product_name: str):
        self.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        result = [product for product in self.products if product.startswith(first_letter)]
        return result

    def __repr__(self):
        result = f'Items in the {self.name} catalogue:\n'
        sorted_list = sorted(self.products)
        result += "\n".join(sorted_list)
        return result

# test
# catalogue = Catalogue("Furniture")
# catalogue.add_product("Sofa")
# catalogue.add_product("Mirror")
# catalogue.add_product("Desk")
# catalogue.add_product("Chair")
# catalogue.add_product("Carpet")
# print(catalogue.get_by_letter("C"))
# print(catalogue)