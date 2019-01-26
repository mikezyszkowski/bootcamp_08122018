class BasketEntry:

    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def count_price(self):
        return self.product.price * self.quantity


class Basket:

    def __init__(self):
        self.entries = []

    def add_product(self, product, quantity):
        basket_entry = BasketEntry(product, quantity)
        for be in self.entries:
            if be.product == product:
                be.quantity += quantity
                break
        else:
            self.entries.append(product, quantity)

    def count_total_price(self):
        total = 0
        for e in self.entries:
            total += e.count_price()
        return total

    def generate_report(self):
        report = "Products in basket:\n"
        for e in self.entries:
            report += f'- {e.product.name} ({e.product.id}), price: {e.product.price} x {e.quantity}\n'
        report += f'Total: {self.count_total_price()}'
        return report


class Product:

    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    def printinfo(self):
        print(f"Product {self.name}, id: {self.id}, price: {self.price} PLN")

    def _str_(self):
        return f"<Product {self.name}, id: {self.id}>"
