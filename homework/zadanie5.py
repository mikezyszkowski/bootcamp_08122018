import string

string.ascii_lowercase


def czy_pangram(napis, alfabet=string.ascii_lowercase):
    napis = "".join(napis.lower().split())
    return set(napis) == set(alfabet)


assert czy_pangram("The quick brown fox jumps over the lazy dog") == True
assert czy_pangram("Ala ma kota") == False

alfabet = "abcdefghijklmnoprstuvwyzóćżźśńąę"
assert czy_pangram("Pchnąć w tę łódź jeża lub ośm skrzyń fig", alfabet=alfabet) == True