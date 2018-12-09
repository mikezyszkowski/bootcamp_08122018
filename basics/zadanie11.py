x = int(input("Podaj pozycję gracza X: "))
y = int(input("Podaj pozycję gracza Y: "))

if x > 100 or y > 100:
    print("Gracz poza planszą")

if x <= 10 and y <= 10:
    print("Lewy dolny róg")

if x >= 90 and y <= 10:
    print("Prawy dolny róg")

if x >= 90 and y >= 90:
    print("Prawy górny róg")

if x >= 10 and y >= 90:
    print("Lewy górny róg")

if x == 50 and y == 50
    print("Centrum")

if