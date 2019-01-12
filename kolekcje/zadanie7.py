napis = input("Podaj tekst: ")

ile_samoglosek = 0
SAMOGLOSKI = "aeiouy"

for litera in napis:
    if litera in SAMOGLOSKI:
        ile_samoglosek += 1

print(ile_samoglosek)
