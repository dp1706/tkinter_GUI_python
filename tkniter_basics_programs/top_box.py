from tkinter import *

root=Tk()
root.title('Welcome to LikeGeeks app')
root.geometry('350x200')

tb=Toplevel(root)

#spinbox

sp=Spinbox(root,from_=0,to=40)
sp.pack()

root.mainloop()
