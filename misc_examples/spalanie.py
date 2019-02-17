import tkinter


def policz_spalanie():
    d = int(distance.get())
    c = float(cena.get())
    s = int(spalanie.get())

    w = d*c*s*0.01
    wynik.configure(text=w)

root = tkinter.Tk

distance_label = tkinter.Label(master=root, text="Dystans: ")
distance.grid(row=0, column=0)
distance = tkinter.Entry(master=root)
distance.grid(row=0, column=1)

spalanie_label = tkinter.Label(master=root, text="Spalanie: ")
spalanie.grid(row=1, column=0)
spalanie = tkinter.Entry(master=root)
spalanie.grid(row=1, column=1)

cena_label = tkinter.Label(master=root, text="Cena: ")
cena.grid(row = )

root.mainloop()