import re

with open("re_zadanie_input.txt") as f:
        string = f.read()

        print(re.findall(r'\b\d\d-\d{3}\b', string))
        print(re.findall(r'[\w\-.]+@[\w\-.]+', string))
        print(re.findall(r'\d{1,2}\s[A-Z][a-z]{2} \d{4}', string))