lista = [3, 5, -1, -14, 3, 16, -431, 50, -40, -2, -7, 0]

dodatnie = 0
ujemne = 0

for liczba in lista:
    if liczba < 0:
        dodatnie += 1
    elif liczba > 0:
        ujemne += 1

print(f"Liczba dodatnich: {dodatnie}, Liczba ujemnych: {ujemne}")

dodatnie = [x for x in lista if x > 0]
ujemne = [x for x in lista if x < 0]

dodatnie = len(dodatnie)
ujemne = len(ujemne)

print(f"Liczba dodatnich: {dodatnie}, Liczba ujemnych: {ujemne}")
