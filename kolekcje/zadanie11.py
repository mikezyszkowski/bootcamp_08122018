liczby = set()
parzyste = set(range(0, 100, 2))
while True:
    komenda = input("Podaj liczbę lub [k] by zakończyć: ")
    if komenda == 'k':
        break
    else:
        liczby.add(int(komenda))

print(liczby)
print("Liczb unikalnych jest: ", len(liczby))
print("Z tego parzystych jest: ", len(liczby & parzyste))
