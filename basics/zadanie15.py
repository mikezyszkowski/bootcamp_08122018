from random import randint

position_x = randint(1, 10)
position_y = randint(1, 10)
treasure_x = randint(1, 10)
treasure_y = randint(1, 10)

min_l_krokow_po_wyl = abs(treasure_x - position_x) + abs(treasure_y - position_y)
liczba_krokow = 0

DEBUG = False

while True:
    min_1_krokow_przed_ruchem = abs(treasure_x - position_x) + abs(treasure_y - position_y)

    print("Twoja pozycja: ", position_x, position_y)
    print("Położenie skarbu: ", treasure_x, treasure_y)

    W = 1
    S = -1
    A = -1
    D = 1

    komenda = input("Twój ruch: ")
    if komenda == 'W':
        position_y += 1
    elif komenda == 'S':
        position_y -= 1
    elif komenda == 'A':
        position_x -= 1
    elif komenda == 'D':
        position_x += 1

    liczba_krokow += 1
    min_l_krokow_po_ruchu = abs(treasure_y - position_y) + abs(treasure_x - position_x)

    if position_y > 10 or position_x > 10 or position_y < 0 or position_x < 0:
        print("Fail")
        break
    if min_l_krokow_po_ruchu < min_1_krokow_przed_ruchem:
        print("Ciepło")
    if min_l_krokow_po_ruchu > min_1_krokow_przed_ruchem:
        print("Zimno")

    if liczba_krokow >= min_l_krokow_po_wyl * 2:
        treasure_y = randint(1, 10)
        treasure_x = randint(1, 10)
        min_l_krokow_po_wyl = abs(treasure_x - position_x) + abs(treasure_y - position_y)
        print("Skarb zmienił położenie")

    if (position_x, position_y) == (treasure_x, treasure_y):
        print("GG")
        break
