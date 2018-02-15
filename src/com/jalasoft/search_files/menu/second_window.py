from tkinter import *

def text_get_textbox_varible():
    print("Este es el path: "+path_search.get())


root=Tk()
root.title("ADVANCE SEARCH MENU")
root.geometry("500x500")

path_search=StringVar()
name_search=StringVar()
size_search=IntVar()


label_path=Label(root,text="Enter the Path: ").place(x=20, y=30)
box_path=Entry(root,text=path_search).place(x=120,y=30)

label_search_in=Label(root,text="Search in...").place(x=20, y=60)
option_file=Radiobutton(root,value = 1 ,text= "File").place(x=20, y=85)
option_folder=Radiobutton(root,value = 2 ,text= "Folder").place(x=100, y=85)
option_both=Radiobutton(root,value = 3 ,text= "Folder and File").place(x=180, y=85)

label_search_by=Label(root,text="Search by: ").place(x=20, y=120)
option_name=Radiobutton(root,value = 4 ,text= "By Name").place(x=20, y=145)
label_name=Label(root, text="Name: ").place(x=20,y=170)
box_name =Entry(root,text=name_search).place(x=150,y=170)

label_size=Label(root, text="by Size: ").place(x=20,y=200)
option_mega=Radiobutton(root, value=5,text="MB ").place(x=40,y=230)
option_giga=Radiobutton(root, value=5,text="GB ").place(x=80,y=230)
box_size=Entry(root,text=size_search).place(x=120,y=260)

button_search=Button(root,text="Search", command=text_get_textbox_varible).place(x=300,y= 300)
button_quit=Button(root,text="Return Menu").place(x=380,y=300)
button_clear=Button(root,text="CLean").place(x=220,y=300)


root.mainloop()