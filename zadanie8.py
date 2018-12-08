x = float(input("Długość: "))
y = float(input("Szerokość: "))
h = float(input("Wysokość: "))
l = x * y * h

print(f"Objętość: {l} cm")
print(l > 1000)

if l > 2000:
    print("Objętość jest większa niż 2 litry")
elif l > 1000:
    print("Objętość jest większa niż 1 litr")
else:
    print("Objętość jest mniejsza niż 1 litr")