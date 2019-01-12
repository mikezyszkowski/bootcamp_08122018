


znaki = {}
text = input("Tekst:")

for z in text:
    if z in znaki:
        znaki[z] += 1
    else:
        znaki[z] = 1

print("Statystyka: ")

for z, c in znaki.items():
    print(f" - {z} wystąpił {c} razy")