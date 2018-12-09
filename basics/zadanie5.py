miasto_a = input("Miasto A: ")
miasto_b = input("Miasto B: ")
dystans = int(input(f"Dystans {miasto_a} {miasto_b}: "))
cena_paliwa = float(input("Cena Paliwa: "))
spalanie = float(input("Spalanie na 100km: "))

koszt = dystans / 100 * spalanie * cena_paliwa

print(f"Koszt przejazdu {miasto_a} {miasto_b}:", koszt)