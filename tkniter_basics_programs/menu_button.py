from tkinter import *

root=Tk()
root.title('Welcome to LikeGeeks app')
root.geometry('350x200')

mb=Menubutton(root,text="Menubutton",relief=RAISED)
mb.grid()

s=  Menu ( mb, tearoff = 0 )
mb["menu"] =  s

mayoVar = IntVar()
ketchVar = IntVar()

s.add_checkbutton ( label="mayo",
                          variable=mayoVar )
s.add_checkbutton ( label="ketchup",
                          variable=ketchVar )

mb.pack()

root.mainloop()
