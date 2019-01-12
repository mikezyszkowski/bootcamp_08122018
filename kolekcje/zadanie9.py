produkty = {
    'cebula': 2,
    'papryka': 10,
    'pomidor': 4,
    'salata': 3,
}
magazyn = {
    'cebula': 100,
    'papryka': 15,
    'pomidor': 30,
    'salata': 12,
}
while True:
    rola = input("Czy jesteś [klient]em [k], czy [dostawca] [d]?, [q] by zakończyć ")
    if rola.lower() in ['klient', 'k']:
        print("Na sprzedaż: ")
        for produkt, cena in produkty.items():
            print(f' - {produkt} - {cena:2f}')
        zakup = input("Co chcesz kupić? [k] by zakończyć ")
        if zakup.lower() == 'k':
            print("Zapraszamy ponownie!")
            break
        if zakup not in produkty:
            print("Brak produktu")
            continue
        waga = float(input(f"Ile chcesz kupić - [{zakup}]"))
        if waga > magazyn[zakup]:
            print("Nie ma tyle towaru")
            print(f"W magazynie pozostało: {magazyn[zakup]}")
        else:
            cena = produkty.get(zakup)
            if cena:
                koszt = waga * produkty[zakup]
                print(f"Za [{zakup}] zapłacisz: {koszt:.2f}")
                magazyn[zakup] -= waga
            else:
                print("Brak tego produktu")
    elif rola.lower() in ['dostawca', 'd']:
        while True:
            do_dodania = input("Podaj produkt w formacie [nazwa ilosc cena]: ")
            if len(do_dodania.split()) == 3:
                nazwa, ilosc, cena = do_dodania.split()
                try:
                    ilosc = float(ilosc)
                    cena = float(cena)
                    produkty[nazwa] = cena
                    break
                except ValueError:
                    print("Niepoprawna cena lub ilosc")


            else:
                print("Podałeś produkt w niepoprawnym formacie")
        if nazwa in magazyn:
            magazyn[nazwa] = magazyn[nazwa] + ilosc
        else:
            magazyn[nazwa] = ilosc

        magazyn[nazwa] = magazyn.get(nazwa, 0) + ilosc

        print("Dziekuję. Produkt Dodany")
    elif rola.lower() == 'q':
        print("Program przestaje działać")
    break

