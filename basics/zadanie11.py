x = int(input("Podaj pozycję gracza X: "))
y = int(input("Podaj pozycję gracza Y: "))

if x > 100 or y > 100 or x < 0 or y < 0:
    print("Gracz poza planszą")

elif x <= 10 and y <= 10:
    print("Lewy dolny róg")

elif x >= 90 and y <= 10:
    print("Prawy dolny róg")

elif x >= 90 and y >= 90:
    print("Prawy górny róg")

elif x <= 10 and y >= 90:
    print("Lewy górny róg")

elif y > 90:
    print("Górna krawędź")

elif y < 10:
    print("Dolna krawędź")

elif x < 10:
    print("Lewa krawędź")

elif x > 90:
    print("Prawa krawędź")

else:
    print("Jesteś w centrum")