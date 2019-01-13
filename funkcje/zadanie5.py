import pytest


def silnia(wartosc):
    if wartosc < 0:
        raise ValueError("Argument musi być >= 0")
    if wartosc == 0:
        return 1
    else:
        return wartosc * silnia(wartosc-1)


def test_silnia_dla_zera():
    assert silnia(0) == 1

def test_silnia_dla_wieksze_od_0():
    assert silnia(5) == 120

def test_silnia_dla_mniejsze_od_0():
    with pytest.raises(ValueError) as e:
        silnia(-10)