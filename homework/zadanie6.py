def liczba_doskonala(liczba):
    total = 0
    for i in range(1, liczba):
        if liczba % i == 0:
            total += i

    return total == liczba


assert liczba_doskonala(6) == True
assert liczba_doskonala(7) == False
assert liczba_doskonala(28) == True
assert liczba_doskonala(496) == True