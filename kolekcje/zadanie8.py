napis = input("Wpisz tekst: ")

dlugosc = 0
licz = False

for znak in napis:
    if znak == "<":
        licz = True
    elif znak == ">":
        break
    elif licz:
        dlugosc += 1


print(dlugosc)