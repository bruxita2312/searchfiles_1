from tkinter import *

def print_test():
    print("el boton si funciona")


def open_advance_window():

    root_advance = Tk()
    root_advance.title("ADVANCE SEARCH MENU")
    root_advance.geometry("500x500")

    path_search = StringVar()
    name_search = StringVar()
    size_search = IntVar()

    label_path = Label(root_advance, text="Enter the Path: ").place(x=20, y=30)
    box_path = Entry(root_advance, text=path_search).place(x=120, y=30)

    label_search_in = Label(root_advance, text="Search in...").place(x=20, y=60)
    option_file = Radiobutton(root_advance, value=1, text="File").place(x=20, y=85)
    option_folder = Radiobutton(root_advance, value=2, text="Folder").place(x=100, y=85)
    option_both = Radiobutton(root_advance, value=3, text="Folder and File").place(x=180, y=85)

    label_search_by = Label(root_advance, text="Search by: ").place(x=20, y=120)
    #option_name = Radiobutton(root_advance, value=4, text="By Name").place(x=20, y=145)
    label_name = Label(root_advance, text="by Name: ").place(x=20, y=150)
    box_name = Entry(root_advance, text=name_search).place(x=100, y=150)

    label_size = Label(root_advance, text="by Size: ").place(x=20, y=185)
    box_size = Entry(root_advance, text=size_search).place(x=100, y=185)
    option_mega = Radiobutton(root_advance, value=5, text="MB ").place(x=80, y=230)
    option_giga = Radiobutton(root_advance, value=6, text="GB ").place(x=130, y=230)
    option_kbyte = Radiobutton(root_advance, value=7, text="KB ").place(x=180, y=230)


    button_search = Button(root_advance, text="Search").place(x=300, y=300)
    button_quit = Button(root_advance, text="Return Menu", command=menu_main).place(x=380, y=300)
    button_clear = Button(root_advance, text="Clean").place(x=220, y=300)



def menu_main():
    root=Tk()
    root.title("SEARCH MENU")
    root.geometry("300x200")
    label=Label(root,text="SEARCH MENU").place(x=100,y=20)

    button_basic=Button(root, text="Basic Search", command=print_test).place(x=20,y=70)

    button_advance=Button(root, text="Advance Search", command=open_advance_window).place(x=150,y=70)
    button_quit = Button(root, text="Quit", command=root.quit).place(x=220,y=140)
    root.mainloop()


menu_main()



