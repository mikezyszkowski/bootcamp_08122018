def foo():
    bar()

def bar():
    print('gg')

foo()
bar()
print(bar())


print(locals())

print(foo)

def potega(podstawa, wykladnik=2):
    return podstawa ** wykladnik

print(potega(4))