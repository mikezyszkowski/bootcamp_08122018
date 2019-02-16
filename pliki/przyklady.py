with open("readme.txt") as f:
    for line in f:
        print(f)
        print(f.read())


with open("readme2.txt", 'w') as f:
    f.write("Ala ma kota")
