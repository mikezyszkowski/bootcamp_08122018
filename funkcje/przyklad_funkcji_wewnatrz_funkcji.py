def a():
    print("Jestem w funkcji a")

    def int():
        return 10

    def b():
        print("Jestem w funkcji b")

    def c():
        print("Jestem w funkcji c")

    b()
    c()
    print(int)

print(int())
a()
