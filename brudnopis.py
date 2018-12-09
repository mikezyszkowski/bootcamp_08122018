# ctrl + / = # przed wszystkim

# lista = [1, 2, 3, 10, 20, 30]
#
#
# print(len(lista))
# print(sum(lista))
#
# lista.append('a')
# print(lista)

dane = input("Podaje liczby, podziel je spacjami: ")
dane = dane.split()
dane2 = []

for d in dane:
    dane2.append(int(d))

dane = map(int, dane)
print(list(dane))
print(dane2)