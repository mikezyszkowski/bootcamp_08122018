
def czy_jest_pierwsza(a):
    for i in range(2, a//2 + 1):
        if a % i == 0:
            return False
        return True



assert czy_jest_pierwsza(17) == True
assert not czy_jest_pierwsza(10) == False