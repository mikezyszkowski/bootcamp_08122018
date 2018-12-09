# ctrl + alt + L = pep8 (styl)
# ctrl + / = # przed wszystkim


# tekst = "Ala ma kota"
# #
# # i = 0
# # while i < len(tekst):
# #     print(tekst[i])
# #     i += 1

# for i, litera in enumerate(tekst):
#     print(i, litera)

# tuple = ("Napis 1", "Napis 2", "Napis 1", 1, 2, 3)
# print(tuple.index("Napis 1"))

lista = [1, 2, 3, 4, 5, 6, 7, 8]
print(type(lista))
print(dir(lista))
print(lista)
lista.append(12)
print(lista)
lista.extend([888, 333])
print(lista[-1][-1])
print(lista)

print("Jak działa pop")
print(lista.pop())
print(lista)

print("Sortowanie")
print(lista.sort())
print(lista)