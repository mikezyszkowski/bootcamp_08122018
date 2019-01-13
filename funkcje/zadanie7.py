def przytnij(data, start, stop):
    out = []
    for el in data:
        if start(el):
            out.append(el)
            if stop(el):
                break
    return out





def test_przytnij():
    wynik = przytnij(
        data=[1, 2, 3, 4, 5, 6, 7]
        start=lambda x: x > 3,
        stop=lambda x: x == 6,
    )
    assert wynik = [4, 5, 6]








