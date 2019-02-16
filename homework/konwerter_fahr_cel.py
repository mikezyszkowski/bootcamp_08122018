class Konwerter():

    def fahr_to_cel(self, value):
        cel = (value-32) * 5 / 9
        return cel

    @staticmethod
    def cel_to_fahr(value):
        fahr = value * 9 / 5 + 32
        return fahr


assert Konwerter().fahr_to_cel(32) == 0
assert Konwerter().cel_to_fahr(0) == 32
