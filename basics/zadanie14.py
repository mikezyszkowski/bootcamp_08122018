i = 0
znaleziono_maksimum = None
znaleziono_minimum = None
liczba = None

while True:
    komenda = input("Podaj liczbę lub k by zakończyć: ")
    if komenda == 'k':
        break
    if komenda[0] == '-' and komenda[1:].isdigit():
        liczba = int(komenda[1:])
        liczba = -liczba
    elif komenda.isdigit():
        liczba = int(komenda)
    else:
        print("Nie podano liczby")
        break

    if znaleziono_maksimum is None or liczba > znaleziono_maksimum:
            znaleziono_maksimum = liczba
    if znaleziono_minimum is None or liczba < znaleziono_minimum:
            znaleziono_minimum = liczba


print("Znalezione maksimum to: ", znaleziono_maksimum)
print("Znalezione minumum to: ", znaleziono_minimum)
