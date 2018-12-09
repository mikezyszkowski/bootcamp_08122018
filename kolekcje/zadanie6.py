liczby = [5, 2, 4, 3]

indeks_min, indeks_max = None, None

for indeks in range(len(liczby)):
    if indeks_min is None or liczby[indeks] < liczby[indeks_min]:
        indeks_min = indeks
    if indeks_max is None or liczby[indeks] > liczby[indeks_max]:
        indeks_max = indeks

liczby[indeks_max], liczby[indeks_min] = liczby[indeks_min], liczby[indeks_max]

assert liczby == [2, 5, 4, 3]