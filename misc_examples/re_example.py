import re

string = "Ala ma kota! Kot ma Ale. Kot lubi mleko. Nie lubi ryb"

print(re.findall('.{3} ma', string))

print(re.findall(r'[A-Z]', string))