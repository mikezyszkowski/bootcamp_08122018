liczby = [1, 2, 3, 4]
liczby2 = [5, 6, 7, 8]
liczby3 = [9, 16, 17, 18]

for i, l in enumerate(liczby):
    print(f'Pozycja={i}, wartość={l}')

for i, l in enumerate(liczby2):
    print(f'Pozycja={i}, wartość={l}')

for i, l in enumerate(liczby3):
    print(f'Indeks={i}, wartość={l}')


def drukuj(lista):
    for i, l in enumerate(lista):
        print(f'Pozycja={i}, wartość={l}')


drukuj(liczby)
drukuj(liczby2)
drukuj(liczby3)


def foo():
    bar()

def bar():
    print("haha")

foo()
bar()
print(bar())

a = 3
b = 3

def dodaj_a_b(a, b):
    if a == 2:
        return 4
    wynik = a + b
    print(globals())
    print(locals())
    return wynik


print(dodaj_a_b(10, 20))
wynik = dodaj_a_b(20, 50)
print(wynik)

print(a, b)
print(globals())
print(locals())

print(foo)

def potega(podstawa, wykladnik=2):
    return podstawa ** wykladnik

print(potega(4))
print(potega(4, 2))
print(potega(4, 3))


def foo(a, b, c, d=1, e=2):
    print(a, b, c, d, e)

foo(1, 2, 3)
foo(1, 2, 3, 3)
foo(1, 2, 3, 3, 2)

# złe
# foo(1, 2, 3, 3, 2, 6)
# foo(1, 2)

foo(c=40, b=20, a=30, d=50, e=70 )

def wykonaj_operacje(operacja, *args):
    print(args)
    print(type(args))
    return operacja(args)

print(wykonaj_operacje(min, 10, 20, 20, 30, 50))

def upper(napis):
    return napis.upper()


