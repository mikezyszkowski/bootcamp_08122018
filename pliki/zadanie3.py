#program filtrujący z pliku adresy email

import sys

try:
    f_name = sys.argv[1]
except IndexError:
    print("Nie podałeś nazwy pliku")
    exit()

cleaned_emails = set()

try:
    with open("cleaned_emails.txt", "w") as f:
        for line in f:
            line = line.strip().lower()
            if line.count("@") == 1:
                cleaned_emails.add(line)









except FileNotFoundError:
    print("Nie ma takiego pliku")