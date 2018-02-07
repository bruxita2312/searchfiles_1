from tkinter import *
from tkinter import messagebox

ventana = Tk()

path = StringVar()
name = StringVar()

ventana.title("test lista")
ventana.geometry("750x500")

label1 = Label(ventana, text="MIAUUUUUU").place(x=350, y=20)
buton_salir = Button(ventana, text="Salir", command=ventana.quit).place(x=670, y=450)
# listaaaa

list_search = Listbox(ventana, width=50).place(x=250, y=50)
list_search.insert(0, "Pilimon")

ventana.mainloop()
