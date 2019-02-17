class Product:

    def __init__(self, id, nazwa, cena):
        self.cena = cena
        self.nazwa = nazwa
        self.id = id

    def printinfo(self):
        print(f"Product {self.nazwa}, id: {self.id}, cena: {self.cena} PLN")


produkt = Product(1, "Woda", 2.99)
produkt.printinfo()
