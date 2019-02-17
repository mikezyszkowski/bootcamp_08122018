import tkinter
from tkinter import messagebox


def suma():
    print("Naciśnieto przycisk")
    try:
        a = int(a_entry.get())
        b = int(b_entry.get())
        wynik = a+b
        wynik_label.configure(text=f"Wynik to {wynik}")
    except ValueError:
        messagebox.showerror("Błędne dane!", "Popraw dane - powinny być liczbami!")


root = tkinter.Tk()

a_label = tkinter.Label(master=root, text="argument a")
a_label.grid(row=0, column=0)
a_entry = tkinter.Entry(master=root)
a_entry.grid(row=0, column=1)

b_label = tkinter.Label(master=root, text="argument b")
b_label.grid(row=1, column=0)
b_entry = tkinter.Entry(master=root)
b_entry.grid(row=1, column=1)


button = tkinter.Button(master=root, text="Sum", command=suma)
button.grid(row=2, column=1)

wynik_label = tkinter.Label(master=root)
wynik_label.grid(row=1, column=2)

root.mainloop()